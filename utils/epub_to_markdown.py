"""
Script: epub_to_markdown.py

A utility to extract chapters from an EPUB file and save each as a Markdown (.md) file, with image extraction and de-duplicated titles.

Usage:
    pip install markdownify lxml beautifulsoup4 tqdm
    python epub_to_markdown.py --input input.epub --output output_folder [options]
"""

import zipfile
import os
import re
import sys
import tempfile
import shutil
import logging
import argparse
from pathlib import Path
from xml.etree import ElementTree as ET
from markdownify import markdownify as md
from bs4 import BeautifulSoup, FeatureNotFound
from tqdm import tqdm

# Configure logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)


class EPUBToMarkdown:
    def __init__(
        self, epub_path, output_dir, pattern, heading_style, bullets, code_language
    ):
        self.epub_path = epub_path
        self.output_dir = Path(output_dir)
        self.images_dir = self.output_dir / "images"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.images_dir.mkdir(parents=True, exist_ok=True)
        try:
            self.zip = zipfile.ZipFile(self.epub_path, "r")
        except (zipfile.BadZipFile, FileNotFoundError) as e:
            logging.error(f"Failed to open EPUB: {e}")
            sys.exit(1)

        self.pattern = re.compile(pattern)
        self.heading_style = heading_style
        self.bullets = bullets
        self.code_language = code_language
        self.manifest = {}
        self.spine = []
        self._load_spine()
        self._extract_all_images()

    def _load_spine(self):
        # Attempt to load content.opf for correct reading order
        opf_path = None
        for name in self.zip.namelist():
            if name.lower().endswith(".opf"):
                opf_path = name
                break
        if not opf_path:
            logging.warning("No .opf file found; defaulting to filename order.")
            return
        try:
            xml = self.zip.read(opf_path)
            root = ET.fromstring(xml)
            ns = {"ns": root.tag.split("}")[0].strip("{")}
            for item in root.findall(".//ns:manifest/ns:item", ns):
                self.manifest[item.attrib["id"]] = item.attrib["href"]
            for itemref in root.findall(".//ns:spine/ns:itemref", ns):
                ref = itemref.attrib.get("idref")
                href = self.manifest.get(ref)
                if href:
                    base = os.path.dirname(opf_path)
                    self.spine.append(os.path.normpath(os.path.join(base, href)))
        except Exception as e:
            logging.warning(f"Error parsing spine: {e}; defaulting to filename order.")

    def _extract_all_images(self):
        # Extract all image files from EPUB to images_dir
        image_exts = (".png", ".jpg", ".jpeg", ".gif", ".svg")
        for member in self.zip.namelist():
            if member.lower().endswith(image_exts):
                data = self.zip.read(member)
                out_path = self.images_dir / Path(member).name
                with open(out_path, "wb") as img:
                    img.write(data)
        logging.info(f"Extracted images to {self.images_dir}")

    def list_chapters(self):
        files = [f for f in self.zip.namelist() if self.pattern.search(f)]
        if self.spine:
            ordered = [f for f in self.spine if f in files]
            extras = [f for f in files if f not in ordered]
            return ordered + sorted(extras)
        return sorted(files)

    def extract_chapter(self, chapter_path):
        content = self.zip.read(chapter_path)
        try:
            soup = BeautifulSoup(content, "lxml")
        except FeatureNotFound:
            logging.warning(
                "lxml parser not found. Falling back to built-in html.parser."
            )
            soup = BeautifulSoup(content, "html.parser")
        # Extract title
        title_tag = soup.find(re.compile(r"^h[1-6]$")) or soup.find("title")
        title = title_tag.get_text().strip() if title_tag else Path(chapter_path).stem
        body = soup.find("body") or soup
        # Convert to markdown
        html = str(body)
        markdown = md(
            html,
            heading_style=self.heading_style,
            bullets=self.bullets,
            code_language=self.code_language,
        )
        # Remove duplicate leading title if present
        lines = markdown.splitlines()
        if lines and lines[0].strip().lstrip("# ").strip() == title:
            lines = lines[1:]
        # Rewrite image links to point to ./images folder
        img_pattern = re.compile(r"!\[([^]]*)\]\(([^)]+)\)")

        def repl(match):
            alt, src = match.groups()
            fname = Path(src).name
            return f"![{alt}](images/{fname})"

        content_md = "\n".join(lines)
        content_md = img_pattern.sub(repl, content_md)
        return f"# {title}\n\n" + content_md

    def save_all(self):
        chapters = self.list_chapters()
        total = len(chapters)
        for idx, chap in enumerate(
            tqdm(chapters, desc="Converting chapters", unit="chap"), start=1
        ):
            md_text = self.extract_chapter(chap)
            name = Path(chap).stem + ".md"
            temp_fd, temp_path = tempfile.mkstemp(dir=self.output_dir)
            with os.fdopen(temp_fd, "w", encoding="utf-8") as tmp:
                tmp.write(md_text)
            final_path = self.output_dir / name
            shutil.move(temp_path, final_path)
            tqdm.write(f"Saved chapter {idx}/{total}: {final_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert EPUB chapters to Markdown files."
    )
    parser.add_argument("--input", "-i", required=True, help="Path to the EPUB file")
    parser.add_argument(
        "--output", "-o", required=True, help="Directory for Markdown output"
    )
    parser.add_argument(
        "--pattern", default=r".*\.(xhtml|html)$", help="Regex for chapter files"
    )
    parser.add_argument(
        "--heading-style",
        default="ATX",
        choices=["ATX", "Setext"],
        help="Markdown heading style",
    )
    parser.add_argument(
        "--bullets", default="*", choices=["*", "-", "+"], help="Bullet style"
    )
    parser.add_argument(
        "--code-language", default="", help="Default language for code blocks"
    )
    args = parser.parse_args()

    converter = EPUBToMarkdown(
        args.input,
        args.output,
        args.pattern,
        args.heading_style,
        args.bullets,
        args.code_language,
    )
    converter.save_all()


if __name__ == "__main__":
    main()
