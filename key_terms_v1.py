#!/usr/bin/env python3
"""
Professional Network Terms Learning System
Implements evidence-based learning with clean architecture and excellent UX
Enhanced with glossary lookup functionality
"""

import sqlite3
import json
import random
import logging
import os
import sys
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple, Any, Protocol
from dataclasses import dataclass, field
from enum import Enum
from contextlib import contextmanager
from pathlib import Path
import difflib
import time
import re
import math

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('learning_system.log'),
    ]
)

# Create file handler for debug logging
file_handler = logging.FileHandler('learning_system.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Create console handler for user-facing messages only
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_formatter)

# Configure the main logger
logger = logging.getLogger(__name__)
logger.handlers.clear()
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)

@dataclass
class UserSettings:
    """User preferences and settings"""
    show_debug_info: bool = False
    show_term_metadata: bool = False
    show_progress_details: bool = True
    use_colors: bool = True
    
    def toggle_debug_info(self) -> None:
        self.show_debug_info = not self.show_debug_info
        if self.show_debug_info:
            console_handler = next((h for h in logger.handlers if isinstance(h, logging.StreamHandler)), None)
            if console_handler:
                console_handler.setLevel(logging.DEBUG)
        else:
            console_handler = next((h for h in logger.handlers if isinstance(h, logging.StreamHandler)), None)
            if console_handler:
                console_handler.setLevel(logging.WARNING)
    
    def toggle_metadata(self) -> None:
        self.show_term_metadata = not self.show_term_metadata
    
    def toggle_progress_details(self) -> None:
        self.show_progress_details = not self.show_progress_details

class QuestionType(Enum):
    """Types of questions available"""
    DEFINITION_TO_TERM = "definition_to_term"
    TERM_TO_DEFINITION = "term_to_definition"
    MULTIPLE_CHOICE = "multiple_choice"
    FILL_IN_BLANK = "fill_in_blank"
    CHAPTER_ASSOCIATION = "chapter_association"

class DifficultyLevel(Enum):
    """Learning difficulty levels"""
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

@dataclass
class LearningMetrics:
    """Tracks learning progress using SM-2 algorithm"""
    easiness_factor: float = 2.5
    repetition_count: int = 0
    interval_days: int = 1
    next_review: datetime = field(default_factory=datetime.now)
    last_reviewed: Optional[datetime] = None
    correct_streak: int = 0
    total_attempts: int = 0
    total_correct: int = 0
    average_response_time: float = 0.0
    difficulty_level: DifficultyLevel = DifficultyLevel.BEGINNER

    @property
    def accuracy_rate(self) -> float:
        return self.total_correct / max(1, self.total_attempts)
    
    @property
    def is_due(self) -> bool:
        return datetime.now() >= self.next_review
    
    @property
    def is_mastered(self) -> bool:
        return (self.accuracy_rate >= 0.85 and 
                self.total_attempts >= 3 and 
                self.correct_streak >= 2)

@dataclass
class NetworkTerm:
    """Represents a networking term"""
    id: Optional[int]
    term: str
    definition: str
    chapters: List[int]
    created_at: datetime = field(default_factory=datetime.now)
    metrics: LearningMetrics = field(default_factory=LearningMetrics)

@dataclass
class QuestionData:
    """Represents a quiz question"""
    question_type: QuestionType
    question: str
    correct_answer: Any
    choices: Optional[List[str]] = None
    target_term: Optional[NetworkTerm] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class StudySession:
    """Represents a study session"""
    id: Optional[int]
    start_time: datetime
    end_time: Optional[datetime] = None
    questions_answered: int = 0
    correct_answers: int = 0
    selected_chapters: List[int] = field(default_factory=list)
    
    @property
    def accuracy_rate(self) -> float:
        return self.correct_answers / max(1, self.questions_answered)
    
    @property
    def duration(self) -> timedelta:
        end = self.end_time or datetime.now()
        return end - self.start_time

@dataclass
class SearchResult:
    """Represents a search result for glossary lookup"""
    term: NetworkTerm
    relevance_score: float
    match_type: str  # 'exact', 'partial', 'definition', 'fuzzy'
    matched_text: str = ""

class DatabaseRepository(ABC):
    """Abstract repository for data access"""
    
    @abstractmethod
    def get_all_terms(self) -> List[NetworkTerm]:
        pass
    
    @abstractmethod
    def get_terms_by_chapters(self, chapters: List[int]) -> List[NetworkTerm]:
        pass
    
    @abstractmethod
    def save_term(self, term: NetworkTerm) -> NetworkTerm:
        pass
    
    @abstractmethod
    def update_term_metrics(self, term: NetworkTerm) -> None:
        pass
    
    @abstractmethod
    def create_session(self) -> StudySession:
        pass
    
    @abstractmethod
    def update_session(self, session: StudySession) -> None:
        pass
    
    @abstractmethod
    def get_study_statistics(self) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def load_terms_from_json(self, json_path: str) -> int:
        pass
    
    @abstractmethod
    def test_connection(self) -> bool:
        pass
    
    @abstractmethod
    def rebuild_database(self) -> bool:
        pass
    
    @abstractmethod
    def test_term_update(self, term_id: int) -> bool:
        pass
    
    @abstractmethod
    def search_terms(self, query: str) -> List[SearchResult]:
        pass

class SQLiteRepository(DatabaseRepository):
    """SQLite implementation of repository"""
    
    def __init__(self, db_path: str = "learning_system.db"):
        self.db_path = db_path
        try:
            self._initialize_database()
            logger.info(f"Database initialized successfully at {db_path}")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise Exception(f"Database initialization failed: {e}")
    
    @contextmanager
    def get_connection(self):
        """Get database connection with proper cleanup"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            yield conn
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            logger.error(f"Database error: {e}")
            raise Exception(f"Database operation failed: {e}")
        except Exception as e:
            if conn:
                conn.rollback()
            logger.error(f"Unexpected error: {e}")
            raise
        finally:
            if conn:
                conn.close()
    
    def _initialize_database(self) -> None:
        """Initialize database schema"""
        with self.get_connection() as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS terms (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    term TEXT NOT NULL UNIQUE,
                    definition TEXT NOT NULL,
                    chapters TEXT NOT NULL,
                    created_at TEXT DEFAULT (datetime('now')),
                    easiness_factor REAL DEFAULT 2.5,
                    repetition_count INTEGER DEFAULT 0,
                    interval_days INTEGER DEFAULT 1,
                    next_review TEXT DEFAULT (datetime('now')),
                    last_reviewed TEXT NULL,
                    correct_streak INTEGER DEFAULT 0,
                    total_attempts INTEGER DEFAULT 0,
                    total_correct INTEGER DEFAULT 0,
                    average_response_time REAL DEFAULT 0.0,
                    difficulty_level INTEGER DEFAULT 1
                );
                
                CREATE TABLE IF NOT EXISTS study_sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    start_time TEXT DEFAULT (datetime('now')),
                    end_time TEXT NULL,
                    questions_answered INTEGER DEFAULT 0,
                    correct_answers INTEGER DEFAULT 0,
                    selected_chapters TEXT DEFAULT ''
                );
                
                CREATE TABLE IF NOT EXISTS question_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id INTEGER,
                    term_id INTEGER,
                    question_type TEXT,
                    is_correct BOOLEAN,
                    response_time REAL,
                    quality_rating INTEGER,
                    created_at TEXT DEFAULT (datetime('now')),
                    FOREIGN KEY (session_id) REFERENCES study_sessions(id),
                    FOREIGN KEY (term_id) REFERENCES terms(id)
                );
                
                CREATE INDEX IF NOT EXISTS idx_terms_next_review ON terms(next_review);
                CREATE INDEX IF NOT EXISTS idx_terms_chapters ON terms(chapters);
                CREATE INDEX IF NOT EXISTS idx_question_history_session ON question_history(session_id);
                CREATE INDEX IF NOT EXISTS idx_terms_search ON terms(term);
                CREATE INDEX IF NOT EXISTS idx_terms_definition_search ON terms(definition);
            """)
            conn.commit()
            logger.info("Database schema initialized successfully")
    
    def get_all_terms(self) -> List[NetworkTerm]:
        """Get all terms from database"""
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM terms ORDER BY term")
            return [self._row_to_term(row) for row in cursor.fetchall()]
    
    def get_terms_by_chapters(self, chapters: List[int]) -> List[NetworkTerm]:
        """Get terms filtered by chapters"""
        try:
            with self.get_connection() as conn:
                terms = []
                for chapter in chapters:
                    cursor = conn.execute("""
                        SELECT * FROM terms 
                        WHERE chapters LIKE '%' || ? || '%'
                        ORDER BY next_review ASC, term
                    """, (str(chapter),))
                    
                    for row in cursor.fetchall():
                        try:
                            term = self._row_to_term(row)
                            if any(ch in term.chapters for ch in chapters):
                                terms.append(term)
                        except Exception as e:
                            logger.error(f"Error parsing term from row {dict(row)}: {e}")
                            continue
                
                # Remove duplicates while preserving order
                seen = set()
                unique_terms = []
                for term in terms:
                    if term.id not in seen:
                        seen.add(term.id)
                        unique_terms.append(term)
                
                logger.debug(f"Retrieved {len(unique_terms)} terms for chapters {chapters}")
                return unique_terms
                
        except Exception as e:
            logger.error(f"Error getting terms by chapters {chapters}: {e}")
            return []
    
    def search_terms(self, query: str) -> List[SearchResult]:
        """Search terms in the glossary with multiple match types"""
        if not query or not query.strip():
            return []
        
        query = query.strip()
        results = []
        
        try:
            all_terms = self.get_all_terms()
            
            # Search strategies with different scoring
            for term in all_terms:
                # 1. Exact term match (highest priority)
                if term.term.lower() == query.lower():
                    results.append(SearchResult(
                        term=term,
                        relevance_score=1.0,
                        match_type='exact',
                        matched_text=term.term
                    ))
                    continue
                
                # 2. Partial term match (start of term)
                if term.term.lower().startswith(query.lower()):
                    results.append(SearchResult(
                        term=term,
                        relevance_score=0.9,
                        match_type='partial',
                        matched_text=term.term
                    ))
                    continue
                
                # 3. Term contains query
                if query.lower() in term.term.lower():
                    results.append(SearchResult(
                        term=term,
                        relevance_score=0.8,
                        match_type='partial',
                        matched_text=term.term
                    ))
                    continue
                
                # 4. Definition contains query (word boundaries)
                pattern = r'\b' + re.escape(query.lower()) + r'\b'
                if re.search(pattern, term.definition.lower()):
                    results.append(SearchResult(
                        term=term,
                        relevance_score=0.7,
                        match_type='definition',
                        matched_text=self._extract_context(term.definition, query)
                    ))
                    continue
                
                # 5. Fuzzy matching for terms
                term_similarity = difflib.SequenceMatcher(None, query.lower(), term.term.lower()).ratio()
                if term_similarity > 0.6:
                    results.append(SearchResult(
                        term=term,
                        relevance_score=term_similarity * 0.6,
                        match_type='fuzzy',
                        matched_text=term.term
                    ))
                    continue
                
                # 6. Fuzzy matching in definition (looser)
                def_words = term.definition.lower().split()
                best_word_match = 0
                best_word = ""
                for word in def_words:
                    if len(word) >= 3:  # Only check words of reasonable length
                        similarity = difflib.SequenceMatcher(None, query.lower(), word).ratio()
                        if similarity > best_word_match:
                            best_word_match = similarity
                            best_word = word
                
                if best_word_match > 0.7:
                    results.append(SearchResult(
                        term=term,
                        relevance_score=best_word_match * 0.4,
                        match_type='fuzzy',
                        matched_text=f"Similar to '{best_word}' in definition"
                    ))
            
            # Sort by relevance score (descending) and then by term name
            results.sort(key=lambda x: (-x.relevance_score, x.term.term.lower()))
            
            # Limit results to top 20 to avoid overwhelming the user
            return results[:20]
            
        except Exception as e:
            logger.error(f"Error searching terms: {e}")
            return []
    
    def _extract_context(self, text: str, query: str, context_chars: int = 100) -> str:
        """Extract context around the matched query in text"""
        try:
            text_lower = text.lower()
            query_lower = query.lower()
            
            index = text_lower.find(query_lower)
            if index == -1:
                return text[:context_chars] + "..." if len(text) > context_chars else text
            
            # Calculate context boundaries
            start = max(0, index - context_chars // 2)
            end = min(len(text), index + len(query) + context_chars // 2)
            
            # Try to break at word boundaries
            if start > 0:
                space_index = text.find(' ', start)
                if space_index != -1 and space_index - start < 20:
                    start = space_index + 1
            
            if end < len(text):
                space_index = text.rfind(' ', 0, end)
                if space_index != -1 and end - space_index < 20:
                    end = space_index
            
            context = text[start:end]
            
            # Add ellipsis if we truncated
            if start > 0:
                context = "..." + context
            if end < len(text):
                context = context + "..."
            
            return context
            
        except Exception as e:
            logger.error(f"Error extracting context: {e}")
            return text[:context_chars] + "..."
    
    def save_term(self, term: NetworkTerm) -> NetworkTerm:
        """Save a new term"""
        chapters_json = json.dumps(term.chapters)
        
        with self.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO terms (term, definition, chapters) 
                VALUES (?, ?, ?)
            """, (term.term, term.definition, chapters_json))
            
            term.id = cursor.lastrowid
            conn.commit()
            
        return term
    
    def update_term_metrics(self, term: NetworkTerm) -> None:
        """Update term learning metrics"""
        metrics = term.metrics
        try:
            chapters_json = json.dumps(term.chapters)
            
            if not isinstance(metrics.next_review, datetime):
                logger.warning(f"Invalid next_review type for term {term.term}: {type(metrics.next_review)}")
                metrics.next_review = datetime.now()
            
            next_review_str = metrics.next_review.strftime('%Y-%m-%d %H:%M:%S')
            last_reviewed_str = None
            if metrics.last_reviewed and isinstance(metrics.last_reviewed, datetime):
                last_reviewed_str = metrics.last_reviewed.strftime('%Y-%m-%d %H:%M:%S')
            
            logger.debug(f"Updating term {term.term}")
            
            if term.id is None:
                logger.error(f"Term {term.term} has no ID, cannot update")
                return
            
            with self.get_connection() as conn:
                result = conn.execute("""
                    UPDATE terms SET
                        easiness_factor = ?,
                        repetition_count = ?,
                        interval_days = ?,
                        next_review = ?,
                        last_reviewed = ?,
                        correct_streak = ?,
                        total_attempts = ?,
                        total_correct = ?,
                        average_response_time = ?,
                        difficulty_level = ?,
                        chapters = ?
                    WHERE id = ?
                """, (
                    float(metrics.easiness_factor),
                    int(metrics.repetition_count),
                    int(metrics.interval_days),
                    next_review_str,
                    last_reviewed_str,
                    int(metrics.correct_streak),
                    int(metrics.total_attempts),
                    int(metrics.total_correct),
                    float(metrics.average_response_time),
                    int(metrics.difficulty_level.value),
                    chapters_json,
                    int(term.id)
                ))
                
                if result.rowcount == 0:
                    logger.warning(f"No rows updated for term {term.term} (ID: {term.id})")
                else:
                    logger.debug(f"Successfully updated {result.rowcount} row(s) for term {term.term}")
                
                conn.commit()
                
        except Exception as e:
            logger.error(f"Error updating term metrics for {term.term}: {e}")
            raise Exception(f"Failed to update term metrics: {e}")
    
    def create_session(self) -> StudySession:
        """Create new study session"""
        session = StudySession(
            id=None,
            start_time=datetime.now()
        )
        
        start_time_str = session.start_time.strftime('%Y-%m-%d %H:%M:%S')
        
        with self.get_connection() as conn:
            cursor = conn.execute("""
                INSERT INTO study_sessions (start_time) 
                VALUES (?)
            """, (start_time_str,))
            
            session.id = cursor.lastrowid
            conn.commit()
            
        return session
    
    def update_session(self, session: StudySession) -> None:
        """Update study session"""
        chapters_json = json.dumps(session.selected_chapters)
        end_time_str = session.end_time.strftime('%Y-%m-%d %H:%M:%S') if session.end_time else None
        
        with self.get_connection() as conn:
            conn.execute("""
                UPDATE study_sessions SET
                    end_time = ?,
                    questions_answered = ?,
                    correct_answers = ?,
                    selected_chapters = ?
                WHERE id = ?
            """, (
                end_time_str,
                session.questions_answered,
                session.correct_answers,
                chapters_json,
                session.id
            ))
            conn.commit()
    
    def get_study_statistics(self) -> Dict[str, Any]:
        """Get comprehensive study statistics"""
        with self.get_connection() as conn:
            total_terms = conn.execute("SELECT COUNT(*) as count FROM terms").fetchone()['count']
            studied_terms = conn.execute("SELECT COUNT(*) as count FROM terms WHERE total_attempts > 0").fetchone()['count']
            mastered_terms = conn.execute("""
                SELECT COUNT(*) as count FROM terms 
                WHERE total_attempts >= 3 AND (total_correct * 1.0 / total_attempts) >= 0.85 AND correct_streak >= 2
            """).fetchone()['count']
            
            total_sessions = conn.execute("SELECT COUNT(*) as count FROM study_sessions").fetchone()['count']
            
            recent_accuracy = conn.execute("""
                SELECT AVG(correct_answers * 1.0 / NULLIF(questions_answered, 0)) as accuracy
                FROM study_sessions 
                WHERE start_time >= datetime('now', '-7 days')
            """).fetchone()['accuracy'] or 0
            
            return {
                'total_terms': total_terms,
                'studied_terms': studied_terms,
                'mastered_terms': mastered_terms,
                'completion_rate': (mastered_terms / max(1, total_terms)) * 100,
                'total_sessions': total_sessions,
                'recent_accuracy': recent_accuracy * 100
            }
    
    @staticmethod
    def _parse_datetime(datetime_str: str) -> datetime:
        """Safely parse datetime strings with multiple format fallbacks"""
        if not datetime_str:
            return datetime.now()
        
        formats = [
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M:%S.%f',
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%dT%H:%M:%S.%f',
            '%Y-%m-%d',
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(datetime_str, fmt)
            except ValueError:
                continue
        
        try:
            return datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
        except ValueError:
            logger.warning(f"Could not parse datetime string: {datetime_str}, using current time")
            return datetime.now()
    
    def _row_to_term(self, row: sqlite3.Row) -> NetworkTerm:
        """Convert database row to NetworkTerm"""
        try:
            next_review = self._parse_datetime(row['next_review'])
            last_reviewed = self._parse_datetime(row['last_reviewed']) if row['last_reviewed'] else None
            created_at = self._parse_datetime(row['created_at']) if row['created_at'] else datetime.now()
            
            term_id = int(row['id']) if row['id'] is not None else None
            if term_id is None:
                raise ValueError("Term ID cannot be None")
            
            metrics = LearningMetrics(
                easiness_factor=float(row['easiness_factor']),
                repetition_count=int(row['repetition_count']),
                interval_days=int(row['interval_days']),
                next_review=next_review,
                last_reviewed=last_reviewed,
                correct_streak=int(row['correct_streak']),
                total_attempts=int(row['total_attempts']),
                total_correct=int(row['total_correct']),
                average_response_time=float(row['average_response_time']),
                difficulty_level=DifficultyLevel(int(row['difficulty_level']))
            )
            
            return NetworkTerm(
                id=term_id,
                term=str(row['term']),
                definition=str(row['definition']),
                chapters=json.loads(row['chapters']),
                created_at=created_at,
                metrics=metrics
            )
            
        except Exception as e:
            logger.error(f"Error converting row to term: {e}")
            raise Exception(f"Failed to parse term from database: {e}")
    
    def load_terms_from_json(self, json_path: str) -> int:
        """Load terms from JSON file if database is empty"""
        try:
            with self.get_connection() as conn:
                count = conn.execute("SELECT COUNT(*) as count FROM terms").fetchone()['count']
                
                if count > 0:
                    logger.info(f"Database already contains {count} terms, skipping JSON import")
                    return count
                
                if not os.path.exists(json_path):
                    logger.warning(f"JSON file not found: {json_path}")
                    return 0
                
                with open(json_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                terms_added = 0
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                for card in data['cards']:
                    try:
                        chapters_json = json.dumps(card['chapters'])
                        
                        conn.execute("""
                            INSERT INTO terms (term, definition, chapters, created_at, next_review) 
                            VALUES (?, ?, ?, ?, ?)
                        """, (
                            str(card['term']).strip(),
                            str(card['definition']).strip(),
                            chapters_json,
                            current_time,
                            current_time
                        ))
                        terms_added += 1
                    except sqlite3.IntegrityError as e:
                        logger.warning(f"Duplicate term skipped: {card.get('term', 'unknown')}")
                        continue
                    except Exception as e:
                        logger.error(f"Error loading term {card.get('term', 'unknown')}: {e}")
                        continue
                
                conn.commit()
                logger.info(f"Successfully loaded {terms_added} terms from {json_path}")
                return terms_added
                
        except Exception as e:
            logger.error(f"Failed to load terms from JSON: {e}")
            return 0
    
    def rebuild_database(self) -> bool:
        """Rebuild database with fresh schema"""
        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                logger.info(f"Removed existing database: {self.db_path}")
            
            self._initialize_database()
            logger.info("Database rebuilt successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to rebuild database: {e}")
            return False
    
    def test_connection(self) -> bool:
        """Test database connection and basic operations"""
        try:
            with self.get_connection() as conn:
                cursor = conn.execute("SELECT 1")
                result = cursor.fetchone()
                
                test_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor = conn.execute("SELECT ? as test_time", (test_time,))
                datetime_result = cursor.fetchone()
                
                logger.debug(f"Database connection test passed")
                logger.debug(f"Datetime test: {test_time} -> {datetime_result['test_time']}")
                
                return result is not None and datetime_result is not None
        except Exception as e:
            logger.error(f"Database connection test failed: {e}")
            return False
    
    def test_term_update(self, term_id: int) -> bool:
        """Test updating a specific term"""
        try:
            logger.debug(f"Testing term update for ID: {term_id}")
            
            with self.get_connection() as conn:
                cursor = conn.execute("SELECT * FROM terms WHERE id = ?", (term_id,))
                row = cursor.fetchone()
                
                if not row:
                    logger.error(f"Term with ID {term_id} not found")
                    return False
                
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                logger.debug(f"Testing update with timestamp: {current_time}")
                
                result = conn.execute("""
                    UPDATE terms SET next_review = ? WHERE id = ?
                """, (current_time, term_id))
                
                conn.commit()
                
                logger.debug(f"Update successful, rows affected: {result.rowcount}")
                return result.rowcount > 0
                
        except Exception as e:
            logger.error(f"Term update test failed: {e}")
            return False

class SpacedRepetitionService:
    """Service for managing spaced repetition algorithm"""
    
    @staticmethod
    def update_schedule(term: NetworkTerm, quality: int, response_time: float = 0.0) -> None:
        """Update learning schedule using SM-2 algorithm"""
        metrics = term.metrics
        metrics.total_attempts += 1
        metrics.last_reviewed = datetime.now()
        
        if response_time > 0:
            if metrics.average_response_time == 0:
                metrics.average_response_time = response_time
            else:
                metrics.average_response_time = (metrics.average_response_time * 0.8) + (response_time * 0.2)
        
        # SM-2 Algorithm
        if quality >= 3:
            metrics.total_correct += 1
            metrics.correct_streak += 1
            
            if metrics.repetition_count == 0:
                metrics.interval_days = 1
            elif metrics.repetition_count == 1:
                metrics.interval_days = 6
            else:
                metrics.interval_days = round(metrics.interval_days * metrics.easiness_factor)
            
            metrics.repetition_count += 1
        else:
            metrics.correct_streak = 0
            metrics.repetition_count = 0
            metrics.interval_days = 1
        
        # Update easiness factor
        metrics.easiness_factor = max(1.3, 
            metrics.easiness_factor + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        
        # Schedule next review
        metrics.next_review = datetime.now() + timedelta(days=metrics.interval_days)
        
        # Update difficulty level
        if metrics.accuracy_rate >= 0.9 and metrics.total_attempts >= 5:
            metrics.difficulty_level = DifficultyLevel.ADVANCED
        elif metrics.accuracy_rate >= 0.7 and metrics.total_attempts >= 3:
            metrics.difficulty_level = DifficultyLevel.INTERMEDIATE
        else:
            metrics.difficulty_level = DifficultyLevel.BEGINNER

class QuestionGenerator:
    """Generates questions using various strategies"""
    
    def __init__(self, terms: List[NetworkTerm]):
        self.terms = terms
        self.generators = {
            QuestionType.DEFINITION_TO_TERM: self._definition_to_term,
            QuestionType.TERM_TO_DEFINITION: self._term_to_definition,
            QuestionType.MULTIPLE_CHOICE: self._multiple_choice,
            QuestionType.FILL_IN_BLANK: self._fill_in_blank,
            QuestionType.CHAPTER_ASSOCIATION: self._chapter_association
        }
    
    def generate_question(self, target_term: NetworkTerm, preferred_type: Optional[QuestionType] = None) -> QuestionData:
        """Generate a question for the target term"""
        if preferred_type and preferred_type in self.generators:
            question_type = preferred_type
        else:
            question_type = self._choose_question_type(target_term)
        
        return self.generators[question_type](target_term)
    
    def _choose_question_type(self, term: NetworkTerm) -> QuestionType:
        """Intelligently choose question type"""
        difficulty = term.metrics.difficulty_level
        accuracy = term.metrics.accuracy_rate
        
        if difficulty == DifficultyLevel.BEGINNER or accuracy < 0.5:
            return random.choice([
                QuestionType.MULTIPLE_CHOICE,
                QuestionType.DEFINITION_TO_TERM
            ])
        elif difficulty == DifficultyLevel.INTERMEDIATE:
            return random.choice([
                QuestionType.TERM_TO_DEFINITION,
                QuestionType.FILL_IN_BLANK,
                QuestionType.MULTIPLE_CHOICE
            ])
        else:
            return random.choice([
                QuestionType.TERM_TO_DEFINITION,
                QuestionType.FILL_IN_BLANK,
                QuestionType.CHAPTER_ASSOCIATION
            ])
    
    def _definition_to_term(self, target_term: NetworkTerm) -> QuestionData:
        return QuestionData(
            question_type=QuestionType.DEFINITION_TO_TERM,
            question=f"What term is defined as:\n\n{target_term.definition}",
            correct_answer=target_term.term,
            target_term=target_term
        )
    
    def _term_to_definition(self, target_term: NetworkTerm) -> QuestionData:
        return QuestionData(
            question_type=QuestionType.TERM_TO_DEFINITION,
            question=f"Define the term: {target_term.term}",
            correct_answer=target_term.definition,
            target_term=target_term
        )
    
    def _multiple_choice(self, target_term: NetworkTerm) -> QuestionData:
        other_terms = [t for t in self.terms if t.term != target_term.term]
        wrong_answers = random.sample(other_terms, min(3, len(other_terms)))
        
        choices = [target_term.definition] + [t.definition for t in wrong_answers]
        random.shuffle(choices)
        
        return QuestionData(
            question_type=QuestionType.MULTIPLE_CHOICE,
            question=f"Which definition best describes '{target_term.term}'?",
            choices=choices,
            correct_answer=target_term.definition,
            target_term=target_term
        )
    
    def _fill_in_blank(self, target_term: NetworkTerm) -> QuestionData:
        definition = target_term.definition
        words = definition.split()
        
        key_words = [w for w in words if len(w) > 4 and w.isalpha()]
        if not key_words:
            key_words = [w for w in words if len(w) > 2 and w.isalpha()]
        
        if key_words:
            blanked_word = random.choice(key_words)
            blanked_definition = definition.replace(blanked_word, "______", 1)
            
            return QuestionData(
                question_type=QuestionType.FILL_IN_BLANK,
                question=f"Complete the definition for '{target_term.term}':\n\n{blanked_definition}",
                correct_answer=blanked_word.lower(),
                target_term=target_term
            )
        
        return self._term_to_definition(target_term)
    
    def _chapter_association(self, target_term: NetworkTerm) -> QuestionData:
        return QuestionData(
            question_type=QuestionType.CHAPTER_ASSOCIATION,
            question=f"In which chapter(s) does '{target_term.term}' appear?",
            correct_answer=target_term.chapters,
            target_term=target_term
        )

class UserInterface:
    """Enhanced user interface with better UX"""
    
    def __init__(self):
        self.settings: UserSettings = UserSettings()
        self.colors: Dict[str, str] = {
            'success': '\033[92m',
            'error': '\033[91m',
            'warning': '\033[93m',
            'info': '\033[94m',
            'header': '\033[95m',
            'bold': '\033[1m',
            'underline': '\033[4m',
            'end': '\033[0m'
        }
        self.results_per_page = 8  # Number of search results per page
    
    def clear_screen(self) -> None:
        """Clear the terminal screen"""
        try:
            # Windows
            if os.name == 'nt':
                os.system('cls')
            # Unix/Linux/MacOS
            else:
                os.system('clear')
        except Exception as e:
            # Fallback: print several newlines
            print('\n' * 50)
            logger.debug(f"Could not clear screen: {e}")
    
    def colored_text(self, text: str, color: str) -> str:
        """Return colored text if terminal supports it"""
        try:
            if not self.settings.use_colors or os.name == 'nt' or os.getenv('NO_COLOR'):
                return text
            
            colored = f"{self.colors.get(color, '')}{text}{self.colors['end']}"
            return colored
            
        except Exception as e:
            logger.error(f"Error applying color to text: {e}")
            return text
    
    def print_header(self, text: str) -> None:
        """Print a styled header"""
        border = "=" * len(text)
        print(f"\n{self.colored_text(border, 'header')}")
        print(f"{self.colored_text(text, 'header')}")
        print(f"{self.colored_text(border, 'header')}\n")
    
    def print_success(self, text: str) -> None:
        print(f"{self.colored_text('✓', 'success')} {text}")
    
    def print_error(self, text: str) -> None:
        print(f"{self.colored_text('✗', 'error')} {text}")
    
    def print_warning(self, text: str) -> None:
        print(f"{self.colored_text('⚠', 'warning')} {text}")
    
    def print_info(self, text: str) -> None:
        print(f"{self.colored_text('ℹ', 'info')} {text}")
    
    def get_user_choice(self, prompt: str, choices: List[str], allow_multiple: bool = False) -> List[str]:
        """Get user choice with validation"""
        while True:
            print(f"\n{prompt}")
            for i, choice in enumerate(choices, 1):
                print(f"{i}. {choice}")
            
            if allow_multiple:
                print(f"{len(choices) + 1}. All options")
                user_input = input("\nSelect options (comma-separated numbers): ").strip()
            else:
                user_input = input(f"\nSelect option (1-{len(choices)}): ").strip()
            
            try:
                if allow_multiple:
                    if user_input == str(len(choices) + 1) or user_input.lower() == 'all':
                        return choices
                    
                    selections = [int(x.strip()) for x in user_input.split(',')]
                    if all(1 <= sel <= len(choices) for sel in selections):
                        return [choices[sel-1] for sel in selections]
                else:
                    selection = int(user_input)
                    if 1 <= selection <= len(choices):
                        return [choices[selection-1]]
                
                self.print_error("Invalid selection. Please try again.")
                
            except ValueError:
                self.print_error("Please enter valid numbers.")
    
    def get_quality_rating(self, is_correct: bool) -> int:
        """Get quality rating for spaced repetition"""
        if is_correct:
            print("\n" + self.colored_text("How confident were you?", "info"))
            print("3 = Correct with effort")
            print("4 = Correct easily") 
            print("5 = Perfect recall")
            
            while True:
                try:
                    rating = int(input("Rating (3-5): "))
                    if 3 <= rating <= 5:
                        return rating
                    self.print_error("Please enter 3, 4, or 5")
                except ValueError:
                    self.print_error("Please enter a number")
        else:
            print("\n" + self.colored_text("How close were you?", "info"))
            print("0 = No idea")
            print("1 = Some recognition")
            print("2 = Close but wrong")
            
            while True:
                try:
                    rating = int(input("Rating (0-2): "))
                    if 0 <= rating <= 2:
                        return rating
                    self.print_error("Please enter 0, 1, or 2")
                except ValueError:
                    self.print_error("Please enter a number")
    
    def display_progress_bar(self, current: int, total: int, width: int = 50) -> None:
        """Display a progress bar"""
        try:
            if total == 0:
                return
            
            progress = current / total
            filled = int(width * progress)
            
            bar = "=" * filled + "-" * (width - filled)
            percentage = progress * 100
            
            progress_text = f"\rProgress: [{bar}] {percentage:.1f}% ({current}/{total})"
            print(progress_text, end='', flush=True)
            
        except Exception as e:
            logger.error(f"Error displaying progress bar: {e}")
            try:
                print(f"\rProgress: {current}/{total} ({(current/total)*100:.1f}%)", end='', flush=True)
            except:
                pass
    
    def display_statistics_table(self, stats: Dict[str, Any]) -> None:
        """Display statistics in a formatted table"""
        self.print_header("Learning Statistics")
        
        print(f"{'Metric':<25} {'Value':<15}")
        print("-" * 40)
        print(f"{'Total Terms:':<25} {stats['total_terms']:<15}")
        print(f"{'Terms Studied:':<25} {stats['studied_terms']:<15}")
        print(f"{'Terms Mastered:':<25} {stats['mastered_terms']:<15}")
        print(f"{'Completion Rate:':<25} {stats['completion_rate']:.1f}%")
        print(f"{'Total Sessions:':<25} {stats['total_sessions']:<15}")
        print(f"{'Recent Accuracy:':<25} {stats['recent_accuracy']:.1f}%")
        print()
    
    def display_search_results(self, results: List[SearchResult], query: str, page: int = 1) -> Dict[str, Any]:
        """Display search results with pagination"""
        if not results:
            self.print_warning(f"No results found for '{query}'")
            self.print_info("Try:")
            print("  • Checking spelling")
            print("  • Using shorter search terms")
            print("  • Searching for partial words")
            return {'action': 'none'}
        
        total_pages = math.ceil(len(results) / self.results_per_page)
        page = max(1, min(page, total_pages))  # Ensure page is within bounds
        
        start_idx = (page - 1) * self.results_per_page
        end_idx = min(start_idx + self.results_per_page, len(results))
        page_results = results[start_idx:end_idx]
        
        self.clear_screen()
        self.print_header(f"Search Results for '{query}' ({len(results)} found)")
        
        print(f"{self.colored_text(f'Page {page} of {total_pages}', 'info')} • Results {start_idx + 1}-{end_idx} of {len(results)}")
        print()
        
        # Display results for current page
        for i, result in enumerate(page_results, start_idx + 1):
            print(f"{self.colored_text(f'{i}. {result.term.term}', 'bold')}")
            
            # Show match information
            match_info = f"({result.match_type}"
            if result.relevance_score < 1.0:
                match_info += f", {result.relevance_score:.0%} confidence"
            match_info += ")"
            print(f"   {self.colored_text(match_info, 'info')}")
            
            # Show chapters
            chapters_str = ', '.join(map(str, result.term.chapters))
            print(f"   Chapters: {chapters_str}")
            
            # Show definition (truncated if long)
            definition = result.term.definition
            if len(definition) > 120:
                definition = definition[:117] + "..."
            print(f"   {definition}")
            
            # Show matched context for definition searches
            if result.match_type == 'definition' and result.matched_text:
                print(f"   {self.colored_text('Match:', 'info')} {result.matched_text}")
            print()
        
        # Display navigation options
        self._display_navigation_options(page, total_pages, len(results))
        
        # Get user input for navigation
        return self._get_navigation_input(page, total_pages, start_idx, end_idx)
    
    def _display_navigation_options(self, page: int, total_pages: int, total_results: int) -> None:
        """Display navigation options"""
        nav_options = []
        
        # Add number selection
        nav_options.append("Enter number to view full definition")
        
        # Add pagination controls
        if total_pages > 1:
            if page > 1:
                nav_options.append("'p' or 'prev' for previous page")
            if page < total_pages:
                nav_options.append("'n' or 'next' for next page")
            nav_options.append("'f' or 'first' for first page")
            nav_options.append("'l' or 'last' for last page")
            nav_options.append("'g <page>' to go to specific page")
        
        nav_options.extend([
            "'s' or 'search' for new search",
            "'back' to return to main menu",
            "Enter to continue"
        ])
        
        print(f"{self.colored_text('Navigation:', 'bold')}")
        for option in nav_options:
            print(f"  • {option}")
    
    def _get_navigation_input(self, page: int, total_pages: int, start_idx: int, end_idx: int) -> Dict[str, Any]:
        """Get and process navigation input"""
        while True:
            user_input = input(f"\n{self.colored_text('Command:', 'info')} ").strip().lower()
            
            if not user_input:
                return {'action': 'continue'}
            
            # Check for number selection
            try:
                selection = int(user_input)
                if start_idx + 1 <= selection <= end_idx:
                    return {'action': 'view_term', 'index': selection - 1}
                else:
                    self.print_error(f"Please enter a number between {start_idx + 1} and {end_idx}")
                    continue
            except ValueError:
                pass
            
            # Navigation commands
            if user_input in ['p', 'prev', 'previous'] and page > 1:
                return {'action': 'page', 'page': page - 1}
            elif user_input in ['n', 'next'] and page < total_pages:
                return {'action': 'page', 'page': page + 1}
            elif user_input in ['f', 'first']:
                return {'action': 'page', 'page': 1}
            elif user_input in ['l', 'last']:
                return {'action': 'page', 'page': total_pages}
            elif user_input.startswith('g '):
                try:
                    target_page = int(user_input.split()[1])
                    if 1 <= target_page <= total_pages:
                        return {'action': 'page', 'page': target_page}
                    else:
                        self.print_error(f"Page must be between 1 and {total_pages}")
                        continue
                except (IndexError, ValueError):
                    self.print_error("Usage: 'g <page_number>'")
                    continue
            elif user_input in ['s', 'search']:
                return {'action': 'new_search'}
            elif user_input in ['back', 'exit', 'quit']:
                return {'action': 'back'}
            else:
                self.print_error("Invalid command. Please try again.")
                continue
    
    def display_term_details(self, term: NetworkTerm) -> None:
        """Display detailed information about a term"""
        self.clear_screen()
        self.print_header(f"Term: {term.term}")
        
        # Format definition with proper line wrapping
        definition_lines = self._wrap_text(term.definition, width=80)
        print("Definition:")
        for line in definition_lines:
            print(f"  {line}")
        
        print(f"\nChapters: {', '.join(map(str, term.chapters))}")
        
        # Show learning metrics if the term has been studied
        if term.metrics.total_attempts > 0:
            print(f"\nLearning Progress:")
            print(f"  Accuracy: {term.metrics.accuracy_rate:.1%} ({term.metrics.total_correct}/{term.metrics.total_attempts})")
            print(f"  Difficulty: {term.metrics.difficulty_level.name}")
            print(f"  Current streak: {term.metrics.correct_streak}")
            
            if term.metrics.last_reviewed:
                print(f"  Last reviewed: {term.metrics.last_reviewed.strftime('%Y-%m-%d %H:%M')}")
            
            if term.metrics.is_due:
                self.print_info("This term is due for review!")
            else:
                days_until = (term.metrics.next_review - datetime.now()).days
                print(f"  Next review: {term.metrics.next_review.strftime('%Y-%m-%d')} ({days_until} days)")
        else:
            self.print_info("This term hasn't been studied yet.")
    
    def _wrap_text(self, text: str, width: int = 80) -> List[str]:
        """Wrap text to specified width, preserving word boundaries"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word) + (1 if current_line else 0)
            
            if current_length + word_length <= width:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines if lines else ['']

class LearningSystemController:
    """Main application controller"""
    
    def __init__(self, repository: DatabaseRepository):
        self.repository = repository
        self.settings = UserSettings()
        self.ui = UserInterface()
        self.ui.settings = self.settings  # Assign settings after initialization
        self.current_session: Optional[StudySession] = None
        self.selected_chapters: List[int] = []
        self.question_generator: Optional[QuestionGenerator] = None
        
        # Load initial data
        self._initialize_data()
    
    def _initialize_data(self) -> None:
        """Initialize application data"""
        json_path = "key_terms_vol1.json"
        
        if not os.path.exists(json_path):
            json_path = "data/key_terms_vol1.json"
        
        try:
            if not self.repository.test_connection():
                self.ui.print_warning("Database connection failed, attempting to rebuild...")
                self.repository.rebuild_database()
                
            if os.path.exists(json_path):
                logger.debug(f"Loading terms from: {json_path}")
                terms_loaded = self.repository.load_terms_from_json(json_path)
                if terms_loaded > 0:
                    self.ui.print_success(f"Loaded {terms_loaded} terms from {json_path}")
            else:
                self.ui.print_warning(f"JSON file not found: {json_path}")
            
            all_terms = self.repository.get_all_terms()
            logger.debug(f"Retrieved {len(all_terms)} total terms")
            
            self.available_chapters = sorted(set(
                chapter for term in all_terms 
                for chapter in term.chapters
            ))
            
            if not all_terms:
                self.ui.print_warning("No terms found. Please ensure key_terms_vol1.json exists.")
            else:
                self.ui.print_info(f"Found {len(all_terms)} terms across {len(self.available_chapters)} chapters")
                
        except Exception as e:
            logger.error(f"Error initializing data: {e}")
            self.ui.print_error(f"Failed to initialize application data: {e}")
    
    def run(self) -> None:
        """Main application loop"""
        self.ui.print_header("Network Terms Learning System")
        self.ui.print_info("Using evidence-based spaced repetition for optimal learning")
        
        try:
            while True:
                self._show_main_menu()
                choice = input(f"\n{self.ui.colored_text('Select option:', 'bold')} ").strip()
                
                if choice == '1':
                    self._select_chapters()
                elif choice == '2':
                    self._start_study_session()
                elif choice == '3':
                    self._quick_review()
                elif choice == '4':
                    self._focused_practice()
                elif choice == '5':
                    self._lookup_definition()
                elif choice == '6':
                    self._show_progress()
                elif choice == '7':
                    self._show_statistics()
                elif choice == '8':
                    self._settings_menu()
                elif choice == '9':
                    self._help()
                elif choice == '0' or choice.lower() == 'quit':
                    break
                else:
                    self.ui.print_error("Invalid choice. Please try again.")
                
                input(f"\n{self.ui.colored_text('Press Enter to continue...', 'info')}")
                
        except KeyboardInterrupt:
            self.ui.print_info("\nGoodbye!")
        except Exception as e:
            logger.error(f"Application error: {e}")
            self.ui.print_error(f"An error occurred: {e}")
    
    def _show_main_menu(self) -> None:
        """Display main menu"""
        self.ui.clear_screen()
        self.ui.print_header("Main Menu")
        
        if self.selected_chapters:
            self.ui.print_info(f"Selected chapters: {', '.join(map(str, self.selected_chapters))}")
            due_count = len(self._get_due_terms())
            self.ui.print_info(f"Terms due for review: {due_count}")
        else:
            self.ui.print_warning("No chapters selected")
        
        # Show current settings status briefly
        settings_status = []
        if self.settings.show_debug_info:
            settings_status.append("debug")
        if self.settings.show_term_metadata:
            settings_status.append("metadata")
        if not self.settings.show_progress_details:
            settings_status.append("minimal")
        
        if settings_status:
            self.ui.print_info(f"Settings: {', '.join(settings_status)}")
        
        print("\n1. Select chapters to study")
        print("2. Start study session")
        print("3. Quick review (5 questions)")
        print("4. Focused practice (difficult terms)")
        print("5. Lookup definition")
        print("6. View progress")
        print("7. Statistics & analytics")
        print("8. Settings")
        print("9. Help")
        print("0. Exit")
    
    def _select_chapters(self) -> None:
        """Chapter selection interface"""
        if not self.available_chapters:
            self.ui.print_error("No chapters available")
            return
        
        self.ui.clear_screen()
        self.ui.print_header("Chapter Selection")
        
        chapter_choices = [f"Chapter {ch}" for ch in self.available_chapters]
        selected = self.ui.get_user_choice(
            "Select chapters to study:",
            chapter_choices,
            allow_multiple=True
        )
        
        self.selected_chapters = []
        for choice in selected:
            if choice.startswith("Chapter "):
                self.selected_chapters.append(int(choice.split()[1]))
        
        terms = self.repository.get_terms_by_chapters(self.selected_chapters)
        self.question_generator = QuestionGenerator(terms)
        
        self.ui.print_success(f"Selected {len(self.selected_chapters)} chapters with {len(terms)} terms")
    
    def _lookup_definition(self) -> None:
        """Lookup definitions in the glossary with improved pagination"""
        current_results = []
        current_query = ""
        current_page = 1
        
        while True:
            # If we don't have current results, show search interface
            if not current_results:
                self.ui.clear_screen()
                self.ui.print_header("Glossary Lookup")
                
                print(f"\n{self.ui.colored_text('Search Options:', 'bold')}")
                print("• Enter a term name (e.g., 'OSPF', 'ethernet')")
                print("• Enter part of a definition (e.g., 'routing protocol')")
                print("• Use partial matches (e.g., 'broad' for 'broadcast')")
                print("• Type 'back' to return to main menu")
                
                query = input(f"\n{self.ui.colored_text('Search:', 'info')} ").strip()
                
                if not query:
                    self.ui.print_warning("Please enter a search term")
                    continue
                
                if query.lower() in ['back', 'exit', 'quit']:
                    break
                
                # Perform search
                current_results = self.repository.search_terms(query)
                current_query = query
                current_page = 1
            
            # Display results with pagination
            if current_results:
                navigation = self.ui.display_search_results(current_results, current_query, current_page)
                
                # Handle navigation actions
                action = navigation.get('action', 'none')
                
                if action == 'view_term':
                    # View detailed term information
                    term_index = navigation['index']
                    selected_term = current_results[term_index].term
                    self._show_term_details_with_navigation(selected_term)
                    
                elif action == 'page':
                    # Navigate to different page
                    current_page = navigation['page']
                    
                elif action == 'new_search':
                    # Clear results to trigger new search
                    current_results = []
                    current_query = ""
                    current_page = 1
                    
                elif action == 'back':
                    # Return to main menu
                    break
                    
                elif action == 'continue':
                    # Stay on current page (do nothing)
                    pass
                    
            else:
                # No results found, wait for user input then start new search
                input(f"\n{self.ui.colored_text('Press Enter to search again...', 'info')}")
                current_results = []
    
    def _show_term_details_with_navigation(self, term: NetworkTerm) -> None:
        """Show detailed term information with navigation back to results"""
        self.ui.display_term_details(term)
        
        print(f"\n{self.ui.colored_text('Options:', 'bold')}")
        print("• 'back' to return to search results")
        
        if term.metrics.total_attempts == 0:
            print("• 'study' to add this term to your study session")
        
        print("• Enter to continue")
        
        while True:
            user_input = input(f"\n{self.ui.colored_text('Command:', 'info')} ").strip().lower()
            
            if user_input == 'back' or user_input == '':
                break
            elif user_input == 'study' and term.metrics.total_attempts == 0:
                self.ui.print_info("Term noted for inclusion in your next study session!")
                input(f"\n{self.ui.colored_text('Press Enter to continue...', 'info')}")
                break
            else:
                self.ui.print_error("Invalid command. Try 'back' or 'study'.")
    
    def _show_term_details(self, term: NetworkTerm) -> None:
        """Show detailed information about a specific term"""
        self.ui.display_term_details(term)
        
        if term.metrics.total_attempts == 0:
            study_now = input(f"\n{self.ui.colored_text('Add this term to your study session? (y/n):', 'info')} ").strip().lower()
            if study_now in ['y', 'yes']:
                self.ui.print_info("Term noted for inclusion in your next study session!")
    
    def _start_study_session(self) -> None:
        """Start a customizable study session"""
        if not self.selected_chapters:
            self.ui.print_error("Please select chapters first")
            return
        
        self.ui.clear_screen()
        self.ui.print_header("Study Session")
        
        try:
            num_questions = int(input("Number of questions (default 10): ") or "10")
            if num_questions <= 0:
                raise ValueError("Number must be positive")
        except ValueError:
            self.ui.print_warning("Using default: 10 questions")
            num_questions = 10
        
        self._conduct_quiz_session(num_questions)
    
    def _quick_review(self) -> None:
        """Quick 5-question review"""
        if not self.selected_chapters:
            self.ui.print_error("Please select chapters first")
            return
        
        self.ui.print_header("Quick Review")
        self._conduct_quiz_session(5)
    
    def _focused_practice(self) -> None:
        """Practice difficult terms"""
        if not self.selected_chapters:
            self.ui.print_error("Please select chapters first")
            return
        
        self.ui.print_header("Focused Practice")
        terms = self.repository.get_terms_by_chapters(self.selected_chapters)
        
        difficult_terms = [
            term for term in terms
            if (term.metrics.accuracy_rate < 0.7 and term.metrics.total_attempts > 0) or
               term.metrics.correct_streak == 0
        ]
        
        if not difficult_terms:
            self.ui.print_info("No difficult terms found. Great job!")
            return
        
        self.ui.print_info(f"Found {len(difficult_terms)} terms that need practice")
        self._conduct_quiz_session(min(10, len(difficult_terms)), difficult_terms)
    
    def _conduct_quiz_session(self, num_questions: int, specific_terms: Optional[List[NetworkTerm]] = None) -> None:
        """Conduct a quiz session"""
        try:
            if not self.question_generator:
                self.ui.print_error("Please select chapters first to initialize the question generator")
                return
                
            logger.info(f"Starting quiz session with {num_questions} questions")
            self.current_session = self.repository.create_session()
            self.current_session.selected_chapters = self.selected_chapters[:]
            
            if specific_terms:
                available_terms = specific_terms
            else:
                available_terms = self._get_due_terms()
                if not available_terms:
                    available_terms = self.repository.get_terms_by_chapters(self.selected_chapters)
            
            if not available_terms:
                self.ui.print_error("No terms available for study")
                return
            
            actual_questions = min(num_questions, len(available_terms))
            self.ui.print_info(f"Starting session with {actual_questions} questions")
            self.ui.print_info("Rate your confidence after each answer for optimal scheduling")
            
            for i in range(actual_questions):
                try:
                    self.ui.display_progress_bar(i, actual_questions)
                    
                    if available_terms:
                        term = self._select_next_term(available_terms)
                        
                        if not term.term or not term.definition:
                            logger.error(f"Invalid term data: term='{term.term}', definition='{term.definition[:50]}...'")
                            continue
                        
                        self._ask_question(term, i + 1, actual_questions)
                    else:
                        logger.error("No available terms in question loop")
                        break
                        
                except Exception as e:
                    logger.error(f"Error in question {i+1}: {e}")
                    continue
            
            if self.current_session:
                self.current_session.end_time = datetime.now()
                self.repository.update_session(self.current_session)
            
            self._show_session_summary()
            
        except Exception as e:
            logger.error(f"Quiz session error: {e}")
            self.ui.print_error(f"Session error: {e}")
    
    def _select_next_term(self, available_terms: List[NetworkTerm]) -> NetworkTerm:
        """Intelligently select the next term to study"""
        try:
            if not available_terms:
                raise ValueError("No available terms to select from")
            
            due_terms = [term for term in available_terms if term.metrics.is_due]
            
            if due_terms:
                # Fix: Use datetime comparison instead of timestamp() to avoid Windows issues
                selected_term = max(due_terms, key=lambda t: (
                    5 - t.metrics.difficulty_level.value,
                    -(t.metrics.last_reviewed or datetime(1970, 1, 1)).replace(tzinfo=None).toordinal()
                ))
                return selected_term
            
            unstudied = [term for term in available_terms if term.metrics.total_attempts == 0]
            if unstudied:
                return random.choice(unstudied)
            
            return random.choice(available_terms)
            
        except Exception as e:
            logger.error(f"Error in _select_next_term: {e}")
            if available_terms:
                return available_terms[0]
            else:
                raise Exception("No terms available for selection")
    
    def _ask_question(self, term: NetworkTerm, question_num: int, total_questions: int) -> None:
        """Ask a single question"""
        try:
            print(f"\n{self.ui.colored_text(f'Question {question_num}/{total_questions}', 'header')}")
            
            if self.settings.show_term_metadata:
                print(f"Term: {term.term}")
                print(f"Chapters: {', '.join(map(str, term.chapters))}")
                print(f"Difficulty: {term.metrics.difficulty_level.name}")
            
            if not self.question_generator:
                self.ui.print_error("Question generator not initialized")
                return
            
            # Add some visual separation before the question
            print()
            
            question_data = self.question_generator.generate_question(term)
            
            start_time = time.time()
            is_correct = self._present_question(question_data)
            response_time = time.time() - start_time
            
            quality = self.ui.get_quality_rating(is_correct)
            
            SpacedRepetitionService.update_schedule(term, quality, response_time)
            self.repository.update_term_metrics(term)
            
            if self.current_session:
                self.current_session.questions_answered += 1
                if is_correct:
                    self.current_session.correct_answers += 1
            
            if self.settings.show_progress_details:
                next_review = term.metrics.next_review
                days_until = (next_review - datetime.now()).days
                self.ui.print_info(f"Next review: {next_review.strftime('%Y-%m-%d')} ({days_until} days)")
            
        except Exception as e:
            logger.error(f"Error asking question for term {term.term}: {e}")
            if self.current_session:
                self.current_session.questions_answered += 1
            self.ui.print_error(f"Error with this question: {e}")
    
    def _present_question(self, question_data: QuestionData) -> bool:
        """Present question and get user response"""
        # Format the question text nicely
        formatted_question = self._format_question_text(question_data.question)
        print(formatted_question)
        
        if question_data.question_type == QuestionType.MULTIPLE_CHOICE:
            return self._handle_multiple_choice(question_data)
        elif question_data.question_type == QuestionType.FILL_IN_BLANK:
            return self._handle_fill_in_blank(question_data)
        elif question_data.question_type == QuestionType.CHAPTER_ASSOCIATION:
            return self._handle_chapter_association(question_data)
        else:
            return self._handle_open_ended(question_data)
    
    def _format_question_text(self, text: str, max_width: int = 80) -> str:
        """Format question text with proper wrapping"""
        # Split into paragraphs first (preserve intentional line breaks)
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []
        
        for paragraph in paragraphs:
            if not paragraph.strip():
                continue
                
            # Remove extra whitespace but preserve single line breaks
            clean_paragraph = ' '.join(paragraph.split())
            
            # Wrap the paragraph
            words = clean_paragraph.split()
            if not words:
                continue
                
            lines = []
            current_line = []
            current_length = 0
            
            for word in words:
                word_length = len(word) + (1 if current_line else 0)
                
                if current_length + word_length <= max_width:
                    current_line.append(word)
                    current_length += word_length
                else:
                    if current_line:
                        lines.append(' '.join(current_line))
                    current_line = [word]
                    current_length = len(word)
            
            if current_line:
                lines.append(' '.join(current_line))
            
            formatted_paragraphs.append('\n'.join(lines))
        
        return '\n\n'.join(formatted_paragraphs)
    
    def _handle_multiple_choice(self, question_data: QuestionData) -> bool:
        """Handle multiple choice questions"""
        choices = question_data.choices
        if not choices:
            self.ui.print_error("No choices available for multiple choice question")
            return False
        
        # Display choices with proper formatting and indentation
        for i, choice in enumerate(choices, 1):
            clean_choice = ' '.join(choice.split())  # Remove extra whitespace
            
            # Format with tab indentation and proper wrapping
            formatted_choice = self._format_choice_text(i, clean_choice)
            print(formatted_choice)
        
        while True:
            try:
                answer = int(input(f"\nYour answer (1-{len(choices)}): "))
                if 1 <= answer <= len(choices):
                    selected = choices[answer - 1]
                    is_correct = selected == question_data.correct_answer
                    
                    if is_correct:
                        self.ui.print_success("Correct!")
                    else:
                        self.ui.print_error("Incorrect.")
                        print(f"\nThe correct answer was:")
                        # Format the correct answer nicely too
                        correct_formatted = self._format_answer_text(question_data.correct_answer)
                        print(correct_formatted)
                    
                    return is_correct
                else:
                    self.ui.print_error(f"Please enter a number between 1 and {len(choices)}")
            except ValueError:
                self.ui.print_error("Please enter a number")
    
    def _format_choice_text(self, number: int, text: str, max_width: int = 80) -> str:
        """Format choice text with proper indentation and wrapping"""
        # Calculate available width after "1.\t" (number, period, tab)
        prefix = f"{number}.\t"
        indent = "\t"
        available_width = max_width - len(indent)
        
        # Split text into words
        words = text.split()
        if not words:
            return f"{prefix}"
        
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            # Check if adding this word would exceed the width
            word_length = len(word) + (1 if current_line else 0)  # +1 for space
            
            if current_length + word_length <= available_width:
                current_line.append(word)
                current_length += word_length
            else:
                # Start a new line
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        # Add the last line
        if current_line:
            lines.append(' '.join(current_line))
        
        # Format with proper indentation
        if not lines:
            return prefix
        
        formatted_lines = [f"{prefix}{lines[0]}"]
        for line in lines[1:]:
            formatted_lines.append(f"{indent}{line}")
        
        return '\n'.join(formatted_lines)
    
    def _format_answer_text(self, text: str, max_width: int = 80) -> str:
        """Format answer text with proper indentation"""
        indent = "\t"
        available_width = max_width - len(indent)
        
        # Split text into words
        words = str(text).split()
        if not words:
            return f"{indent}"
        
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            word_length = len(word) + (1 if current_line else 0)
            
            if current_length + word_length <= available_width:
                current_line.append(word)
                current_length += word_length
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        # Format all lines with indentation
        formatted_lines = [f"{indent}{line}" for line in lines]
        return '\n'.join(formatted_lines)
    
    def _handle_fill_in_blank(self, question_data: QuestionData) -> bool:
        """Handle fill-in-the-blank questions"""
        user_answer = input("\nYour answer: ").strip().lower()
        correct_answer = str(question_data.correct_answer).lower()
        
        similarity = difflib.SequenceMatcher(None, user_answer, correct_answer).ratio()
        is_correct = similarity > 0.8
        
        if is_correct:
            self.ui.print_success("Correct!")
        else:
            self.ui.print_error("Incorrect.")
            print(f"\nThe expected answer was:")
            # Format the correct answer with proper indentation
            correct_formatted = self._format_answer_text(question_data.correct_answer)
            print(correct_formatted)
            if similarity > 0.6:
                self.ui.print_info("You were close!")
        
        return is_correct
    
    def _handle_chapter_association(self, question_data: QuestionData) -> bool:
        """Handle chapter association questions"""
        user_input = input("\nYour answer (comma-separated chapter numbers): ").strip()
        
        try:
            user_chapters = set(int(x.strip()) for x in user_input.split(','))
            correct_chapters = set(question_data.correct_answer)
            
            is_correct = user_chapters == correct_chapters
            
            if is_correct:
                self.ui.print_success("Correct!")
            else:
                self.ui.print_error(f"Correct chapters: {', '.join(map(str, sorted(correct_chapters)))}")
            
            return is_correct
        except ValueError:
            self.ui.print_error(f"Invalid input. Correct chapters: {', '.join(map(str, sorted(question_data.correct_answer)))}")
            return False
    
    def _handle_open_ended(self, question_data: QuestionData) -> bool:
        """Handle open-ended questions"""
        user_answer = input("\nYour answer: ").strip()
        
        print(f"\nCorrect answer:")
        # Format the correct answer with proper indentation
        correct_formatted = self._format_answer_text(question_data.correct_answer)
        print(correct_formatted)
        
        while True:
            self_assessment = input("\nWas your answer correct? (y/n): ").strip().lower()
            if self_assessment in ['y', 'yes']:
                return True
            elif self_assessment in ['n', 'no']:
                return False
            else:
                self.ui.print_error("Please answer 'y' or 'n'")
    
    def _get_due_terms(self) -> List[NetworkTerm]:
        """Get terms that are due for review"""
        if not self.selected_chapters:
            return []
        
        terms = self.repository.get_terms_by_chapters(self.selected_chapters)
        due_terms = [term for term in terms if term.metrics.is_due]
        
        if not due_terms:
            return sorted(terms, key=lambda t: t.metrics.last_reviewed or datetime.min)[:10]
        
        return due_terms
    
    def _show_session_summary(self) -> None:
        """Show session summary"""
        if not self.current_session:
            return
        
        self.ui.print_header("Session Complete!")
        
        accuracy = self.current_session.accuracy_rate * 100
        duration = self.current_session.duration
        
        print(f"Questions answered: {self.current_session.questions_answered}")
        print(f"Correct answers: {self.current_session.correct_answers}")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"Duration: {str(duration).split('.')[0]}")
        
        if accuracy >= 90:
            self.ui.print_success("Excellent work! You're mastering these terms!")
        elif accuracy >= 70:
            self.ui.print_success("Good progress! Keep up the great work!")
        else:
            self.ui.print_info("Every mistake is a learning opportunity. Keep practicing!")
    
    def _show_progress(self) -> None:
        """Show detailed progress information"""
        if not self.selected_chapters:
            self.ui.print_error("Please select chapters first")
            return
        
        self.ui.clear_screen()
        self.ui.print_header("Learning Progress")
        
        terms = self.repository.get_terms_by_chapters(self.selected_chapters)
        
        total_terms = len(terms)
        studied_terms = len([t for t in terms if t.metrics.total_attempts > 0])
        mastered_terms = len([t for t in terms if t.metrics.is_mastered])
        
        print(f"Total terms: {total_terms}")
        print(f"Terms studied: {studied_terms}")
        print(f"Terms mastered: {mastered_terms}")
        print(f"Overall progress: {(mastered_terms/max(1, total_terms))*100:.1f}%")
        
        print(f"\n{self.ui.colored_text('Progress by Chapter:', 'bold')}")
        for chapter in self.selected_chapters:
            chapter_terms = [t for t in terms if chapter in t.chapters]
            chapter_mastered = len([t for t in chapter_terms if t.metrics.is_mastered])
            
            progress = (chapter_mastered / max(1, len(chapter_terms))) * 100
            print(f"Chapter {chapter}: {chapter_mastered}/{len(chapter_terms)} ({progress:.1f}%)")
    
    def _show_statistics(self) -> None:
        """Show comprehensive statistics"""
        self.ui.clear_screen()
        stats = self.repository.get_study_statistics()
        self.ui.display_statistics_table(stats)
    
    def _settings_menu(self) -> None:
        """Settings and preferences"""
        while True:
            self.ui.clear_screen()
            self.ui.print_header("Settings")
            
            print(f"Debug info: {'ON' if self.settings.show_debug_info else 'OFF'}")
            print(f"Term metadata: {'ON' if self.settings.show_term_metadata else 'OFF'}")
            print(f"Progress details: {'ON' if self.settings.show_progress_details else 'OFF'}")
            print(f"Colors: {'ON' if self.settings.use_colors else 'OFF'}")
            
            print("\n1. Toggle debug info (logs and detailed output)")
            print("2. Toggle term metadata (term name, chapters, difficulty)")
            print("3. Toggle progress details (next review dates)")
            print("4. Toggle colors")
            print("5. Reset all settings to defaults")
            print("0. Back to main menu")
            
            choice = input("\nSelect option: ").strip()
            
            if choice == '1':
                self.settings.toggle_debug_info()
                status = "enabled" if self.settings.show_debug_info else "disabled"
                self.ui.print_success(f"Debug info {status}")
            elif choice == '2':
                self.settings.toggle_metadata()
                status = "enabled" if self.settings.show_term_metadata else "disabled"
                self.ui.print_success(f"Term metadata {status}")
            elif choice == '3':
                self.settings.toggle_progress_details()
                status = "enabled" if self.settings.show_progress_details else "disabled"
                self.ui.print_success(f"Progress details {status}")
            elif choice == '4':
                self.settings.use_colors = not self.settings.use_colors
                self.ui.settings = self.settings  # Update UI settings reference
                status = "enabled" if self.settings.use_colors else "disabled"
                self.ui.print_success(f"Colors {status}")
            elif choice == '5':
                self.settings = UserSettings()
                self.ui.settings = self.settings  # Update UI settings reference
                self.ui.print_success("Settings reset to defaults")
            elif choice == '0':
                break
            else:
                self.ui.print_error("Invalid choice. Please try again.")
            
            if choice != '0':
                input(f"\n{self.ui.colored_text('Press Enter to continue...', 'info')}")
    
    def _help(self) -> None:
        """Show help information"""
        self.ui.clear_screen()
        self.ui.print_header("Help & Tips")
        
        help_text = """
Learning System Features:
• Spaced Repetition: Terms appear based on when you're likely to forget them
• Multiple Question Types: Different formats keep learning engaging
• Progress Tracking: Monitor your improvement over time
• Focused Practice: Target your weak areas
• Glossary Lookup: Search and browse all networking terms with pagination

Tips for Success:
• Study regularly in short sessions (10-20 minutes)
• Be honest with confidence ratings for optimal scheduling
• Focus on understanding, not just memorization
• Review progress regularly to stay motivated
• Use the lookup feature to explore related terms

Question Types:
• Multiple Choice: Good for recognition and initial learning
• Fill-in-Blank: Tests recall of key concepts
• Open-Ended: Requires complete understanding
• Chapter Association: Tests organizational knowledge

Difficulty Levels:
• Beginner: New or struggling terms get easier questions
• Intermediate: Moderate performance gets mixed questions  
• Advanced: Well-known terms get challenging questions

Glossary Search Tips:
• Search by exact term name (e.g., "OSPF")
• Search by partial terms (e.g., "broad" finds "broadcast")
• Search within definitions (e.g., "routing protocol")
• Use fuzzy matching for approximate spellings

Navigation Commands in Search:
• 'n' or 'next' - Next page of results
• 'p' or 'prev' - Previous page of results
• 'f' or 'first' - Go to first page
• 'l' or 'last' - Go to last page
• 'g <page>' - Go to specific page number
• 's' or 'search' - Start new search
• Enter number - View detailed definition
        """
        
        print(help_text)

def main():
    """Application entry point"""
    try:
        print("Initializing learning system...")
        repository = SQLiteRepository()
        
        if not repository.test_connection():
            print("Failed to connect to database. Please check file permissions and disk space.")
            sys.exit(1)
        
        print("Database connection successful!")
        
        print("Testing database operations...")
        all_terms = repository.get_all_terms()
        if all_terms:
            test_term = all_terms[0]
            print(f"Testing term update with term: {test_term.term}")
            if test_term.id is not None and repository.test_term_update(test_term.id):
                print("Database update test successful!")
            else:
                print("Database update test failed - check logs for details")
                print("Attempting to continue anyway...")
        
        app = LearningSystemController(repository)
        app.run()
        
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"A fatal error occurred: {e}")
        print("\nTroubleshooting tips:")
        print("1. Ensure you have write permissions in the current directory")
        print("2. Check that disk space is available")
        print("3. Try running as administrator if on Windows")
        print("4. Check the learning_system.log file for detailed error information")
        print("5. Delete learning_system.db to force database recreation")
        
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()