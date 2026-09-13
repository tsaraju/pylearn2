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
