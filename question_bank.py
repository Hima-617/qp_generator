from typing import Dict, List


# Structure:
# QUESTION_BANK["Grade X"]["Subject"]["mcq" | "short" | "long"]
QUESTION_BANK: Dict[str, Dict[str, Dict[str, List[dict]]]] = {}


def _create_sample_grade_questions():
    """
    Create sample questions for Grades 1–12.

    Grades 1–3: 4 subjects (English, Mathematics, EVS, GK)
    Grades 4–12: 5 subjects (English, Mathematics, Science,
                              Social Science, Computer Science)

    Each subject has:
        MCQ:   6 questions
        Short: 4 questions
        Long:  3 questions
    """
    # Subjects
    lower_subjects = ["English", "Mathematics", "EVS", "GK"]
    higher_subjects = ["English", "Mathematics", "Science", "Social Science", "Computer Science"]

    for grade_num in range(1, 13):
        grade_key = f"Grade {grade_num}"
        QUESTION_BANK[grade_key] = {}

        if grade_num <= 3:
            subjects = lower_subjects
        else:
            subjects = higher_subjects

        for subject in subjects:
            mcq_list = []
            short_list = []
            long_list = []

            # MCQs (sample / generic)
            for i in range(1, 7):
                question_text = f"Sample Grade {grade_num} {subject} MCQ question {i}?"
                mcq_list.append(
                    {
                        "question": question_text,
                        "options": [
                            "A) Option A",
                            "B) Option B",
                            "C) Option C",
                            "D) Option D",
                        ],
                        "answer": "A",  # placeholder
                    }
                )

            # Short answers (sample / generic)
            for i in range(1, 5):
                question_text = f"Sample Grade {grade_num} {subject} short answer question {i}."
                short_list.append(
                    {
                        "question": question_text,
                        "answer": f"Sample short answer {i} for Grade {grade_num} {subject}.",
                    }
                )

            # Long answers (sample / generic)
            for i in range(1, 4):
                question_text = f"Sample Grade {grade_num} {subject} long answer question {i}."
                long_list.append(
                    {
                        "question": question_text,
                        "answer": f"Sample long answer {i} for Grade {grade_num} {subject}.",
                    }
                )

            QUESTION_BANK[grade_key][subject] = {
                "mcq": mcq_list,
                "short": short_list,
                "long": long_list,
            }


def _create_btech_questions():
    """
    Create REAL-LIKE questions for B.Tech subjects:

    - Python Programming
    - Data Structures
    - DBMS

    Each subject must have:
        MCQs:   min 10
        Shorts: min 6
        Longs:  min 4
    """
    QUESTION_BANK["B.Tech"] = {}

    # ---------- Python Programming ----------
    python_mcq = [
        {
            "question": "Which of the following is the correct file extension for Python files?",
            "options": [
                "A) .pyt",
                "B) .py",
                "C) .pt",
                "D) .python",
            ],
            "answer": "B",
        },
        {
            "question": "What is the output of: len([1, 2, 3, 4])?",
            "options": [
                "A) 3",
                "B) 4",
                "C) 5",
                "D) Error",
            ],
            "answer": "B",
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": [
                "A) func",
                "B) define",
                "C) def",
                "D) function",
            ],
            "answer": "C",
        },
        {
            "question": "Which of the following is an immutable data type in Python?",
            "options": [
                "A) list",
                "B) dict",
                "C) set",
                "D) tuple",
            ],
            "answer": "D",
        },
        {
            "question": "What is the output of: type(3.0)?",
            "options": [
                "A) <class 'int'>",
                "B) <class 'float'>",
                "C) <class 'double'>",
                "D) <class 'number'>",
            ],
            "answer": "B",
        },
        {
            "question": "Which of the following is used for single-line comments in Python?",
            "options": [
                "A) // comment",
                "B) # comment",
                "C) <!-- comment -->",
                "D) /* comment */",
            ],
            "answer": "B",
        },
        {
            "question": "What is the output of: 'Hello' + 'World'?",
            "options": [
                "A) Hello World",
                "B) Hello+World",
                "C) HelloWorld",
                "D) Error",
            ],
            "answer": "C",
        },
        {
            "question": "Which function is used to get input from the user in Python 3?",
            "options": [
                "A) input()",
                "B) scan()",
                "C) gets()",
                "D) read()",
            ],
            "answer": "A",
        },
        {
            "question": "Which statement is used to handle exceptions in Python?",
            "options": [
                "A) catch-except",
                "B) try-catch",
                "C) try-except",
                "D) throw-except",
            ],
            "answer": "C",
        },
        {
            "question": "What is the correct way to open a file 'data.txt' for reading?",
            "options": [
                "A) open('data.txt', 'w')",
                "B) open('data.txt', 'r')",
                "C) open('data.txt', 'rw')",
                "D) open('data.txt') is invalid",
            ],
            "answer": "B",
        },
    ]

    python_short = [
        {
            "question": "What is PEP 8 in Python?",
            "answer": "PEP 8 is the official Python style guide that defines coding conventions and best practices.",
        },
        {
            "question": "Differentiate between list and tuple in Python.",
            "answer": "Lists are mutable sequences, whereas tuples are immutable sequences.",
        },
        {
            "question": "What is a virtual environment in Python?",
            "answer": "A virtual environment is an isolated Python environment that allows separate dependencies for different projects.",
        },
        {
            "question": "What is list comprehension?",
            "answer": "List comprehension is a concise way to create lists using a single line of code with an expression and loop.",
        },
        {
            "question": "Name any two Python built-in data types.",
            "answer": "Examples: int, float, str, list, tuple, dict, set.",
        },
        {
            "question": "What is the use of 'self' in Python classes?",
            "answer": "'self' refers to the instance of the class and is used to access instance variables and methods.",
        },
    ]

    python_long = [
        {
            "question": "Explain the concept of inheritance in Python with an example.",
            "answer": (
                "Inheritance allows a class (child) to acquire properties and methods of another class (parent). "
                "For example, class Car(Vehicle) can inherit attributes like wheels and methods like start() from Vehicle."
            ),
        },
        {
            "question": "Describe different ways to handle exceptions in Python with suitable code snippets.",
            "answer": (
                "Exceptions can be handled using try-except blocks, optionally with else and finally. "
                "Multiple except blocks can catch specific exceptions, and a generic except can handle others."
            ),
        },
        {
            "question": "Explain the concept of decorators in Python with an example.",
            "answer": (
                "Decorators are functions that modify the behavior of another function. "
                "They are applied using the @decorator_name syntax above a function definition."
            ),
        },
        {
            "question": "Discuss file handling operations in Python and demonstrate reading and writing text files.",
            "answer": (
                "File handling uses open(), read(), write(), and close(). "
                "With 'with open(...) as f' syntax, files are automatically closed. "
                "Modes include 'r', 'w', 'a', and 'b' for binary."
            ),
        },
    ]

    QUESTION_BANK["B.Tech"]["Python Programming"] = {
        "mcq": python_mcq,
        "short": python_short,
        "long": python_long,
    }

    # ---------- Data Structures ----------
    ds_mcq = [
        {
            "question": "Which data structure uses LIFO (Last In First Out)?",
            "options": [
                "A) Queue",
                "B) Stack",
                "C) Linked List",
                "D) Tree",
            ],
            "answer": "B",
        },
        {
            "question": "Which of the following is not a linear data structure?",
            "options": [
                "A) Array",
                "B) Linked List",
                "C) Tree",
                "D) Stack",
            ],
            "answer": "C",
        },
        {
            "question": "The time complexity of searching in a balanced binary search tree is:",
            "options": [
                "A) O(1)",
                "B) O(log n)",
                "C) O(n)",
                "D) O(n log n)",
            ],
            "answer": "B",
        },
        {
            "question": "Which of the following operations is fastest in an array?",
            "options": [
                "A) Insertion at beginning",
                "B) Deletion at beginning",
                "C) Random access",
                "D) Insertion in middle",
            ],
            "answer": "C",
        },
        {
            "question": "Which data structure is used for implementing recursion?",
            "options": [
                "A) Queue",
                "B) Stack",
                "C) Deque",
                "D) Graph",
            ],
            "answer": "B",
        },
        {
            "question": "In a max-heap, the largest element is found at:",
            "options": [
                "A) Any leaf node",
                "B) Rightmost leaf",
                "C) Root node",
                "D) Middle node",
            ],
            "answer": "C",
        },
        {
            "question": "Which traversal of a binary search tree results in sorted order?",
            "options": [
                "A) Pre-order",
                "B) In-order",
                "C) Post-order",
                "D) Level-order",
            ],
            "answer": "B",
        },
        {
            "question": "Which hash collision resolution technique uses a linked list?",
            "options": [
                "A) Linear probing",
                "B) Quadratic probing",
                "C) Separate chaining",
                "D) Double hashing",
            ],
            "answer": "C",
        },
        {
            "question": "What is the worst-case time complexity of Quick Sort?",
            "options": [
                "A) O(n)",
                "B) O(n log n)",
                "C) O(n^2)",
                "D) O(log n)",
            ],
            "answer": "C",
        },
        {
            "question": "Which data structure is best suited for implementing a priority queue?",
            "options": [
                "A) Array",
                "B) Linked List",
                "C) Heap",
                "D) Stack",
            ],
            "answer": "C",
        },
    ]

    ds_short = [
        {
            "question": "Define a binary search tree.",
            "answer": "A binary search tree is a binary tree where each node's left subtree has smaller keys and the right subtree has larger keys.",
        },
        {
            "question": "What is a circular queue?",
            "answer": "A circular queue connects the last position back to the first to form a circle, efficiently using array space.",
        },
        {
            "question": "Differentiate between stack and queue.",
            "answer": "A stack is LIFO, where the last element inserted is removed first, while a queue is FIFO, where the first element inserted is removed first.",
        },
        {
            "question": "What is a linked list?",
            "answer": "A linked list is a linear data structure where each element (node) contains data and a reference to the next node.",
        },
        {
            "question": "What is a hash function?",
            "answer": "A hash function maps keys to indices in a hash table, ideally distributing keys uniformly.",
        },
        {
            "question": "Define time complexity.",
            "answer": "Time complexity is a measure of the amount of time an algorithm takes as a function of input size.",
        },
    ]

    ds_long = [
        {
            "question": "Explain the operations of insertion and deletion in a singly linked list with diagrams.",
            "answer": "Describe node structure, head pointer updates, and pointer adjustments for inserting and deleting at various positions.",
        },
        {
            "question": "Describe the algorithm for binary search and discuss its time complexity.",
            "answer": "Binary search repeatedly divides the search interval in half, operating in O(log n) time for sorted arrays.",
        },
        {
            "question": "Explain different tree traversal techniques with examples.",
            "answer": "Pre-order, in-order, post-order, and level-order traversals visit nodes in different orders suited to various tasks.",
        },
        {
            "question": "Discuss the working of heap sort algorithm.",
            "answer": "Heap sort builds a heap from the input data and repeatedly extracts the maximum (or minimum) to produce a sorted list.",
        },
    ]

    QUESTION_BANK["B.Tech"]["Data Structures"] = {
        "mcq": ds_mcq,
        "short": ds_short,
        "long": ds_long,
    }

    # ---------- DBMS ----------
    dbms_mcq = [
        {
            "question": "Which of the following is not a valid SQL command?",
            "options": [
                "A) SELECT",
                "B) UPDATE",
                "C) REMOVE",
                "D) INSERT",
            ],
            "answer": "C",
        },
        {
            "question": "Which normal form removes partial dependencies?",
            "options": [
                "A) 1NF",
                "B) 2NF",
                "C) 3NF",
                "D) BCNF",
            ],
            "answer": "B",
        },
        {
            "question": "Which of these is a DDL command?",
            "options": [
                "A) SELECT",
                "B) UPDATE",
                "C) INSERT",
                "D) CREATE",
            ],
            "answer": "D",
        },
        {
            "question": "What does ACID stand for in the context of transactions?",
            "options": [
                "A) Atomicity, Consistency, Isolation, Durability",
                "B) Accuracy, Consistency, Integrity, Durability",
                "C) Atomicity, Correctness, Isolation, Durability",
                "D) None of the above",
            ],
            "answer": "A",
        },
        {
            "question": "Which key uniquely identifies a record in a table?",
            "options": [
                "A) Foreign key",
                "B) Candidate key",
                "C) Primary key",
                "D) Alternate key",
            ],
            "answer": "C",
        },
        {
            "question": "Which SQL clause is used to filter rows?",
            "options": [
                "A) WHERE",
                "B) GROUP BY",
                "C) ORDER BY",
                "D) HAVING",
            ],
            "answer": "A",
        },
        {
            "question": "Which type of join returns rows that have matching values in both tables?",
            "options": [
                "A) INNER JOIN",
                "B) LEFT JOIN",
                "C) RIGHT JOIN",
                "D) FULL OUTER JOIN",
            ],
            "answer": "A",
        },
        {
            "question": "The process of organizing data to reduce redundancy is called:",
            "options": [
                "A) Decomposition",
                "B) Normalization",
                "C) Aggregation",
                "D) Integration",
            ],
            "answer": "B",
        },
        {
            "question": "Which of the following is a non-relational database?",
            "options": [
                "A) MySQL",
                "B) PostgreSQL",
                "C) MongoDB",
                "D) Oracle",
            ],
            "answer": "C",
        },
        {
            "question": "Which of the following can be used to enforce referential integrity?",
            "options": [
                "A) Primary key",
                "B) Foreign key",
                "C) Unique key",
                "D) Check constraint",
            ],
            "answer": "B",
        },
    ]

    dbms_short = [
        {
            "question": "Define DBMS.",
            "answer": "DBMS (Database Management System) is software that manages and organizes databases and provides access to stored data.",
        },
        {
            "question": "What is a primary key?",
            "answer": "A primary key is a column or set of columns that uniquely identifies each row in a table.",
        },
        {
            "question": "What is a foreign key?",
            "answer": "A foreign key is a field that links one table to the primary key of another table to maintain referential integrity.",
        },
        {
            "question": "Define normalization.",
            "answer": "Normalization is the process of organizing data to minimize redundancy and improve data integrity.",
        },
        {
            "question": "What is a transaction in DBMS?",
            "answer": "A transaction is a logical unit of work that must be either fully completed or fully rolled back.",
        },
        {
            "question": "What is a view in SQL?",
            "answer": "A view is a virtual table based on the result of a SQL query.",
        },
    ]

    dbms_long = [
        {
            "question": "Explain the ACID properties of a transaction with examples.",
            "answer": "ACID stands for Atomicity, Consistency, Isolation, Durability. Each property ensures reliable transaction processing.",
        },
        {
            "question": "Describe the differences between 1NF, 2NF, and 3NF with examples.",
            "answer": "Describe removal of repeating groups (1NF), partial dependencies (2NF), and transitive dependencies (3NF).",
        },
        {
            "question": "Explain different types of SQL joins with examples.",
            "answer": "Inner, left, right, and full outer joins combine rows from two or more tables based on related columns.",
        },
        {
            "question": "Discuss the architecture of a DBMS with a neat diagram.",
            "answer": "Explain components such as query processor, storage manager, transaction manager, and buffer manager.",
        },
    ]

    QUESTION_BANK["B.Tech"]["DBMS"] = {
        "mcq": dbms_mcq,
        "short": dbms_short,
        "long": dbms_long,
    }


def get_subjects_for_grade(grade: str):
    return list(QUESTION_BANK.get(grade, {}).keys())


def get_question_type_counts(grade: str, subject: str):
    data = QUESTION_BANK.get(grade, {}).get(subject, {})
    return {
        "mcq": len(data.get("mcq", [])),
        "short": len(data.get("short", [])),
        "long": len(data.get("long", [])),
    }


# Build the question bank on import
_create_sample_grade_questions()
_create_btech_questions()
