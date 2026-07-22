# Python Learning Path

A practical, dependency-free Python curriculum. Each chapter contains short, runnable examples followed by a challenge; the final chapter contains complete command-line projects.

## Getting started

Install Python 3.10 or newer, clone this repository, and run any script from the repository root:

```powershell
python 01_Basics/lesson.py
```

Work through the chapters in order. Read a chapter README, run its examples, then solve the challenge without looking at the solution again.

## Curriculum

| Stage | Focus |
| --- | --- |
| 01–06 | Fundamentals: values, control flow, functions, and recursion |
| 07–11 | Core collections: strings, lists, tuples, dictionaries, and sets |
| 12–15 | Practical Python: files, errors, modules, and object-oriented design |
| 16 | Ten self-contained terminal projects |

## Repository structure

```text
Python/
├── 01_Basics/                 # Syntax, variables, input, and types
├── 02_Operators/              # Arithmetic, comparison, logical, and bitwise operators
├── 03_Conditional_Statements/ # Branching and decision making
├── 04_Loops/                  # Iteration, control flow, and patterns
├── 05_Functions/              # Reusable functions, scope, and lambdas
├── 06_Recursion/              # Recursive problem solving
├── 07_Strings/                # Text manipulation and formatting
├── 08_Lists/                  # Mutable sequences
├── 09_Tuples/                 # Immutable sequences and unpacking
├── 10_Dictionaries/           # Key-value data structures
├── 11_Sets/                   # Unique values and set operations
├── 12_File_Handling/          # Text and CSV file operations
├── 13_Exception_Handling/     # Defensive error handling
├── 14_Modules/                # Standard-library and custom modules
├── 15_OOP/                    # Classes, inheritance, and abstractions
├── 16_Projects/               # Complete command-line applications
├── .gitignore                 # Generated local files excluded from Git
└── README.md                  # This roadmap
```

## Principles

- Each learning chapter has one focused `lesson.py` and one `challenge.py`.
- Projects use only the Python standard library.
- Generated data files are ignored so running examples does not dirty the repository.
