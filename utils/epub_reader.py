"""
EPUB Reader for CCNA 200-301 Official Cert Guide Library.
A simple tool to read and extract content from EPUB files using Python's zipfile module.
"""

import zipfile
import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, List


class EPUBReader:
    """Class for reading and extracting content from EPUB files."""

    def __init__(self, epub_path: str):
        """Initialize the EPUB reader with the path to the EPUB file.

        Args:
            epub_path: Path to the EPUB file
        """
        self.epub_path = epub_path
        self.zip_file = None
        self.open_epub()

    def open_epub(self):
        """Open the EPUB file as a ZIP archive."""
        try:
            self.zip_file = zipfile.ZipFile(self.epub_path, "r")
            print(f"Successfully opened {self.epub_path}")
        except zipfile.BadZipFile:
            print(f"Error: {self.epub_path} is not a valid EPUB/ZIP file")
            raise

    def close(self):
        """Close the ZIP file."""
        if self.zip_file:
            self.zip_file.close()
            self.zip_file = None
            print("EPUB file closed")

    def __enter__(self):
        """Enter context manager."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager and ensure ZIP file is closed."""
        self.close()

    def list_contents(self, pattern: Optional[str] = None) -> List[str]:
        """List all files in the EPUB or filter by pattern.

        Args:
            pattern: Regular expression pattern to filter files

        Returns:
            List of file paths in the EPUB
        """
        if not self.zip_file:
            return []

        file_list = self.zip_file.namelist()

        if pattern:
            file_list = [f for f in file_list if re.search(pattern, f)]

        return file_list

    def list_chapters(self) -> List[str]:
        """List all chapter files in the EPUB.

        Returns:
            List of chapter file paths
        """
        chapter_pattern = r"OEBPS/xhtml/vol[0-9]+_ch[0-9]+.xhtml"
        return self.list_contents(chapter_pattern)

    def list_images(self) -> List[str]:
        """List all image files in the EPUB.

        Returns:
            List of image file paths
        """
        image_pattern = r"OEBPS/xhtml/graphics/.*\.jpg"
        return self.list_contents(image_pattern)

    def extract_file(self, file_path: str, output_dir: str = ".") -> Optional[str]:
        """Extract a specific file from the EPUB to the output directory.

        Args:
            file_path: Path to the file in the EPUB
            output_dir: Directory to extract the file to

        Returns:
            Path to the extracted file or None if extraction failed
        """
        if not self.zip_file:
            print("No EPUB file opened")
            return None

        try:
            self.zip_file.extract(file_path, output_dir)
            print(f"Extracted {file_path} to {output_dir}")
            return os.path.join(output_dir, file_path)
        except KeyError:
            print(f"File {file_path} not found in the EPUB")
            return None

    def read_text_content(self, file_path: str) -> Optional[str]:
        """Read and return the text content of a file in the EPUB.

        Args:
            file_path: Path to the file in the EPUB

        Returns:
            Text content of the file or None if reading failed
        """
        if not self.zip_file:
            print("No EPUB file opened")
            return None

        try:
            # Using context manager for file access
            with self.zip_file.open(file_path) as f:
                content = f.read()

            # Parse as XML/HTML and extract text content
            try:
                root = ET.fromstring(content)
                # Extract text content while ignoring tags
                text_content = ET.tostring(root, encoding="unicode", method="text")
                return text_content
            except ET.ParseError:
                # If parsing fails, return raw content
                return content.decode("utf-8")

        except KeyError:
            print(f"File {file_path} not found in the EPUB")
            return None

    def save_image(self, image_path: str, output_dir: str = "images") -> Optional[str]:
        """Save an image from the EPUB to the output directory.

        Args:
            image_path: Path to the image in the EPUB
            output_dir: Directory to save the image to

        Returns:
            Path to the saved image or None if saving failed
        """
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(exist_ok=True)

        return self.extract_file(image_path, output_dir)

    def extract_chapter_text(
        self, chapter_path: str, clean: bool = True
    ) -> Optional[str]:
        """Extract text content from a chapter.

        Args:
            chapter_path: Path to the chapter file in the EPUB
            clean: Whether to clean the extracted text

        Returns:
            Text content of the chapter or None if extraction failed
        """
        text = self.read_text_content(chapter_path)

        if clean and text is not None:
            # Basic cleaning to remove excessive whitespace
            text = re.sub(r"\s+", " ", text)
            text = re.sub(r"\n\s*\n", "\n\n", text)

        return text


def main():
    """Main function to run the EPUB reader."""
    # Replace with your EPUB file path
    epub_path = "ccna-200-301.epub"

    try:
        # Using context manager for EPUBReader ensures it's closed properly
        with EPUBReader(epub_path) as reader:
            # Print basic information
            print("\nEPUB Contents Summary:")
            print(f"Total files: {len(reader.list_contents())}")
            print(f"Chapters: {len(reader.list_chapters())}")
            print(f"Images: {len(reader.list_images())}")

            # Interactive menu
            while True:
                print("\n" + "=" * 50)
                print("EPUB Reader Menu:")
                print("1. List all chapters")
                print("2. Read a specific chapter")
                print("3. List all images")
                print("4. Extract an image")
                print("5. Extract all chapters to text files")
                print("6. Exit")

                choice = input("\nEnter your choice (1-6): ")

                if choice == "1":
                    chapters = reader.list_chapters()
                    for i, chapter in enumerate(chapters):
                        print(f"{i+1}. {chapter}")

                elif choice == "2":
                    chapters = reader.list_chapters()
                    for i, chapter in enumerate(chapters):
                        print(f"{i+1}. {chapter}")

                    chapter_idx = int(input("\nEnter chapter number: ")) - 1
                    if 0 <= chapter_idx < len(chapters):
                        chapter_text = reader.extract_chapter_text(
                            chapters[chapter_idx]
                        )
                        if chapter_text:
                            print("\nChapter Preview (first 500 chars):")
                            print(chapter_text[:500] + "...")

                            save = input("\nSave full chapter to file? (y/n): ").lower()
                            if save == "y":
                                filename = f"chapter_{chapter_idx+1}.txt"
                                # Using context manager for file writing
                                with open(filename, "w", encoding="utf-8") as f:
                                    f.write(chapter_text)
                                print(f"Saved to {filename}")
                        else:
                            print("Failed to extract chapter text")
                    else:
                        print("Invalid chapter number")

                elif choice == "3":
                    images = reader.list_images()
                    # Show first 20 images with option to show more
                    for i, image in enumerate(images[:20]):
                        print(f"{i+1}. {image}")

                    if len(images) > 20:
                        print(f"... and {len(images)-20} more images")

                elif choice == "4":
                    images = reader.list_images()
                    for i, image in enumerate(images[:20]):
                        print(f"{i+1}. {image}")

                    if len(images) > 20:
                        print(f"... and {len(images)-20} more images")

                    image_idx = (
                        int(input("\nEnter image number (or 0 to specify path): ")) - 1
                    )

                    if image_idx == -1:
                        image_path = input("Enter exact image path: ")
                        reader.save_image(image_path)
                    elif 0 <= image_idx < len(images):
                        reader.save_image(images[image_idx])
                    else:
                        print("Invalid image number")

                elif choice == "5":
                    output_dir = "chapters"
                    Path(output_dir).mkdir(exist_ok=True)

                    chapters = reader.list_chapters()
                    for i, chapter in enumerate(chapters):
                        print(f"Processing {i+1}/{len(chapters)}: {chapter}...")
                        chapter_text = reader.extract_chapter_text(chapter)

                        # Create a filename based on the chapter
                        filename = os.path.join(
                            output_dir, f"{os.path.basename(chapter)}.txt"
                        )
                        if chapter_text:
                            # Using context manager for file writing
                            with open(filename, "w", encoding="utf-8") as f:
                                f.write(chapter_text)
                        else:
                            print(
                                f"  Warning: Failed to extract content from {chapter}"
                            )

                    print(f"All chapters extracted to {output_dir}/")

                elif choice == "6":
                    print("Goodbye!")
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")

    except zipfile.BadZipFile:
        print(f"Error: {epub_path} is not a valid EPUB/ZIP file")
    except FileNotFoundError:
        print(f"Error: File {epub_path} not found")
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
