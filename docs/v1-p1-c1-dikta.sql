-- Create quizzes table
CREATE TABLE quizzes (
    quiz_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);

-- Create questions table
CREATE TABLE questions (
    question_id INTEGER PRIMARY KEY,
    quiz_id INTEGER NOT NULL,
    question_number INTEGER NOT NULL,
    question_text TEXT NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quizzes (quiz_id)
);

-- Create options table (optimized - no letter tracking, includes is_correct flag)
CREATE TABLE options (
    option_id INTEGER PRIMARY KEY,
    question_id INTEGER NOT NULL,
    option_text TEXT NOT NULL,
    is_correct BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (question_id) REFERENCES questions (question_id)
);

-- Insert quiz
INSERT INTO quizzes (quiz_id, title)
VALUES (1, 'Do I Know This Already?');

-- Insert questions
INSERT INTO questions (question_id, quiz_id, question_number, question_text)
VALUES (1, 1, 1, 'Which of the following protocols are examples of TCP/IP transport layer protocols? (Choose two answers.)');
INSERT INTO questions (question_id, quiz_id, question_number, question_text)
VALUES (2, 1, 2, 'Which of the following protocols are examples of TCP/IP data-link layer protocols? (Choose two answers.)');
INSERT INTO questions (question_id, quiz_id, question_number, question_text)
VALUES (3, 1, 3, 'The process of HTTP asking TCP to send some data and making sure that it is received correctly is an example of what?');
INSERT INTO questions (question_id, quiz_id, question_number, question_text)
VALUES (4, 1, 4, 'The process of TCP on one computer marking a TCP segment as segment 1 and the receiving computer then acknowledging the receipt of TCP segment 1 is an example of what?');
INSERT INTO questions (question_id, quiz_id, question_number, question_text)
VALUES (5, 1, 5, 'The process of a web server adding a TCP header to the contents of a web page, followed by adding an IP header and then adding a data-link header and trailer, is an example of what?');
INSERT INTO questions (question_id, quiz_id, question_number, question_text)
VALUES (6, 1, 6, 'Which of the following terms is used specifically to identify the entity created when encapsulating data inside data-link layer headers and trailers?');

-- Insert options
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (1, 1, 'Ethernet', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (2, 1, 'HTTP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (3, 1, 'IP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (4, 1, 'UDP', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (5, 1, 'SMTP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (6, 1, 'TCP', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (7, 2, 'Ethernet', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (8, 2, 'HTTP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (9, 2, 'IP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (10, 2, 'UDP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (11, 2, 'SMTP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (12, 2, 'TCP', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (13, 2, '802.11', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (14, 3, 'Same-layer interaction', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (15, 3, 'Adjacent-layer interaction', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (16, 3, 'TCP/IP model', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (17, 3, 'All of these answers are correct.', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (18, 4, 'Data encapsulation', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (19, 4, 'Same-layer interaction', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (20, 4, 'Adjacent-layer interaction', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (21, 4, 'TCP/IP model', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (22, 4, 'All of these answers are correct.', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (23, 5, 'Data encapsulation', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (24, 5, 'Same-layer interaction', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (25, 5, 'TCP/IP model', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (26, 5, 'All of these answers are correct.', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (27, 6, 'Data', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (28, 6, 'Chunk', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (29, 6, 'Segment', 0);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (30, 6, 'Frame', 1);
INSERT INTO options (option_id, question_id, option_text, is_correct)
VALUES (31, 6, 'Packet', 0);

-- Sample queries for the optimized database

-- Query 1: Get all questions with their options (randomized order for display)
SELECT q.question_number, q.question_text, o.option_text, o.is_correct
FROM questions q
JOIN options o ON q.question_id = o.question_id
ORDER BY q.question_number, RANDOM();

-- Query 2: Get all questions with their correct answers
SELECT q.question_number, q.question_text, 
       GROUP_CONCAT(o.option_text, ', ') AS correct_answers
FROM questions q
JOIN options o ON q.question_id = o.question_id
WHERE o.is_correct = 1
GROUP BY q.question_id
ORDER BY q.question_number;

-- Query 3: Check if a user's selected option is correct
SELECT 
    q.question_number,
    q.question_text,
    o.option_text,
    CASE 
        WHEN o.is_correct = 1 THEN 'Correct'
        ELSE 'Incorrect'
    END AS answer_status
FROM options o
JOIN questions q ON o.question_id = q.question_id
WHERE q.question_id = 1 AND o.option_id = 4;
