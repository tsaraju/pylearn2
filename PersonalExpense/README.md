# Personal Expense Tracker

A small command-line Python application for recording and reviewing personal
expenses. It is designed as a beginner-friendly college assignment that
demonstrates modules, package imports, JSON file storage, custom exceptions,
logging, and command-line input.

## Features

- Add an expense with an amount, category, description, and date
- View all saved expenses
- Calculate the total expense amount
- Filter expenses by category
- Store expenses in a JSON file
- Validate invalid amounts and empty required fields
- Handle missing or invalid data files
- Log application events and errors to a file
- Handle `Ctrl+C` gracefully

## Project Structure

```text
PersonalExpense/
├── main.py
├── README.md
├── data/
│   └── expenses.json
├── logs/
│   └── expense_tracker.log
└── expense_tracker/
    ├── exceptions.py
    ├── logger.py
    ├── manager.py
    ├── models.py
    └── storage.py
```

### Module Responsibilities

- `main.py` provides the command-line menu and collects user input.
- `expense_tracker/models.py` defines the `Expense` model.
- `expense_tracker/manager.py` validates expenses and performs calculations,
  listing, and category filtering.
- `expense_tracker/storage.py` saves and loads expenses as JSON.
- `expense_tracker/exceptions.py` defines `InvalidExpenseError`.
- `expense_tracker/logger.py` configures file logging.

## Requirements

- Python 3.10 or newer
- No third-party packages are required.

## Running the Application

Open a terminal in the project directory and run:

```powershell
python main.py
```

The application displays this menu:

```text
1. Add an expense
2. View expenses
3. View total expenses
4. Filter expenses by category
5. Exit
```

When adding an expense, enter a positive numeric amount, a category, a
description, and a date such as `2026-09-13`.

## Data and Logs

Expenses are stored in `data/expenses.json`. If the file does not exist, the
application starts with an empty list and creates the file when expenses are
saved.

Application logs are written to `logs/expense_tracker.log`. The log entries
include a timestamp, log level, and message.

## Error Handling

The application reports invalid input without terminating the menu. It handles
non-numeric and negative amounts, empty categories, invalid JSON data, file
errors, unexpected runtime errors, and keyboard interruption with `Ctrl+C`.

Github Copilot AI prompts:

Prompt1:
I need to build a small command-line Python application for a college assignment. I have chosen a Personal Expense Tracker.
The application should allow a user to add expenses, view expenses, calculate total expenses, and optionally filter expenses by category.
The final project must contain:
At least 4 Python files/modules
At least one Python package
Imports between modules
try/except/finally
At least one custom exception
Logging to a file
README.md
A command-line interface
Do not generate any code yet. First, analyze the requirements, identify the main features, and suggest a reasonable implementation approach.

Prompt2:
Based on the requirements we discussed, suggest a Python package/module structure for the Personal Expense Tracker.
Explain the responsibility of each Python file and how the modules should import and interact with each other.
Do not generate the implementation code yet.

Prompt3:
Generate only expense_tracker/models.py for the Personal Expense Tracker.
Create an Expense class containing an ID, amount, category, description, and date.
Keep the implementation simple and suitable for a beginner Python CLI project.
Do not generate any other files.

Prompt4:
Now generate only expense_tracker/storage.py.
It should save and load Expense objects using a JSON file.
Import the Expense model from expense_tracker.models.
Include basic error handling for missing or invalid files.
Do not modify or generate any other modules.

Prompt5:
Create expense_tracker/exceptions.py.
Define appropriate custom exceptions for the Personal Expense Tracker. At minimum, create an exception for invalid expense data.
Keep the implementation simple and explain where this exception should be used.

Prompt6:
Generate only expense_tracker/manager.py.
It should provide functionality to:
add an expense
list expenses
calculate total expenses
filter expenses by category
Import and use the Expense model from models.py.
Import and use the custom exception from exceptions.py.
Keep the code simple and modular. Do not generate other files.

Prompt7:
Create expense_tracker/logger.py.
Configure Python's logging module so that application logs are written to logs/expense_tracker.log.
Include timestamps, log levels, and messages.
The logger should be reusable by other modules in the application.
Do not generate any other files.

Prompt8:
Generate main.py for my existing Personal Expense Tracker project.
It should provide a simple command-line menu allowing the user to:
Add an expense
View expenses
View total expenses
Filter expenses by category
Exit
Import the required classes/functions from the expense_tracker package.
Do not duplicate business logic in main.py. The manager module should handle application logic.
Include appropriate user input validation.

Prompt9:
Review the current CLI structure of my Personal Expense Tracker.
Add appropriate try/except/finally handling without unnecessarily rewriting the application.
The application should handle invalid user input, invalid expense data, file errors, the custom InvalidExpenseError, and unexpected exceptions.
Also handle KeyboardInterrupt gracefully.
Explain exactly where the finally block is useful.

Prompt10:
Review my Personal Expense Tracker code for unnecessary duplication, poor naming, overly large functions, and unnecessary complexity.
Suggest improvements first. Do not rewrite the entire project.
Identify which specific modules/functions should be refactored and why.

Prompt11:
Test at least these cases:
Add a valid expense
Add multiple expenses
View expenses
Calculate total
Filter by category
Enter a non-numeric amount
Enter a negative amount
Enter an empty category
Start with no data file
Interrupt the program with Ctrl+C

Prompt12:
Add README file and update it

Prompt13:
PersonalExpense/expense_tracker/storage.py loads and saves JSON expenses, but save_expenses does not create the data directory before writing.

Prompt14:
