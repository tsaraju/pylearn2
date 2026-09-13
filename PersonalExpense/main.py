from pathlib import Path

from expense_tracker.exceptions import InvalidExpenseError
from expense_tracker.logger import get_logger
from expense_tracker.manager import ExpenseManager
from expense_tracker.storage import load_expenses, save_expenses


DATA_FILE = Path("data") / "expenses.json"


def display_expenses(expenses):
    """Print expenses in a simple readable format."""
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"ID: {expense.id} | Amount: {expense.amount:.2f} | "
            f"Category: {expense.category} | Description: {expense.description} | "
            f"Date: {expense.date}"
        )


def get_next_id(expenses):
    """Return the next available numeric expense ID."""
    numeric_ids = [expense.id for expense in expenses if isinstance(expense.id, int)]
    return max(numeric_ids, default=0) + 1


def add_expense(manager):
    """Collect and add one expense from user input."""
    amount = input("Amount: ").strip()
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    date = input("Date (YYYY-MM-DD): ").strip()

    if not description:
        raise InvalidExpenseError("Description cannot be empty.")
    if not date:
        raise InvalidExpenseError("Date cannot be empty.")

    expense = manager.add_expense(
        expense_id=get_next_id(manager.expenses),
        amount=amount,
        category=category,
        description=description,
        date=date,
    )
    print(f"Expense {expense.id} added successfully.")


def run():
    """Run the command-line expense tracker."""
    logger = get_logger()
    manager = ExpenseManager()

    try:
        try:
            manager.expenses = load_expenses(DATA_FILE)
            logger.info("Loaded expenses from %s", DATA_FILE)
        except (OSError, ValueError) as error:
            logger.error("Could not load expense data: %s", error)
            print(f"Could not load expense data: {error}")
            return

        try:
            while True:
                print("\nPersonal Expense Tracker")
                print("1. Add an expense")
                print("2. View expenses")
                print("3. View total expenses")
                print("4. Filter expenses by category")
                print("5. Exit")

                choice = input("Choose an option: ").strip()

                try:
                    if choice == "1":
                        add_expense(manager)
                        save_expenses(manager.expenses, DATA_FILE)
                        logger.info("Added and saved an expense")
                    elif choice == "2":
                        display_expenses(manager.list_expenses())
                    elif choice == "3":
                        print(f"Total expenses: {manager.calculate_total():.2f}")
                    elif choice == "4":
                        category = input("Category: ").strip()
                        display_expenses(manager.filter_by_category(category))
                    elif choice == "5":
                        save_expenses(manager.expenses, DATA_FILE)
                        logger.info("Saved expenses and exited")
                        print("Goodbye!")
                        break
                    else:
                        print("Invalid option. Please choose a number from 1 to 5.")
                except (InvalidExpenseError, OSError, ValueError) as error:
                    logger.warning("Operation failed: %s", error)
                    print(f"Error: {error}")
                except Exception:
                    logger.exception("Unexpected error while processing menu choice")
                    print("An unexpected error occurred. Please try again.")
        except KeyboardInterrupt:
            logger.info("Application interrupted by user")
            print("\nApplication interrupted. Goodbye!")
    except Exception:
        logger.exception("Unexpected application error")
        print("An unexpected application error occurred.")
    finally:
        logger.info("Expense tracker stopped")
        for handler in logger.handlers:
            handler.flush()


if __name__ == "__main__":
    run()
