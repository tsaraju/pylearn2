import json
from pathlib import Path

from expense_tracker.models import Expense


def save_expenses(expenses, filename):
    """Save a list of Expense objects to a JSON file."""
    data = [
        {
            "id": expense.id,
            "amount": expense.amount,
            "category": expense.category,
            "description": expense.description,
            "date": expense.date,
        }
        for expense in expenses
    ]

    try:
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except OSError as error:
        raise OSError(f"Could not save expenses to {filename}: {error}") from error


def load_expenses(filename):
    """Load Expense objects from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"Could not load valid expense data from {filename}: {error}") from error

    if not isinstance(data, list):
        raise ValueError("Expense data must be a JSON list.")

    try:
        return [
            Expense(
                expense_id=item["id"],
                amount=item["amount"],
                category=item["category"],
                description=item["description"],
                date=item["date"],
            )
            for item in data
        ]
    except (KeyError, TypeError) as error:
        raise ValueError("Expense data contains an invalid record.") from error
