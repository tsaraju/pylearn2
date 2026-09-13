from expense_tracker.exceptions import InvalidExpenseError
from expense_tracker.models import Expense


class ExpenseManager:
    """Provides operations for managing expenses."""

    def __init__(self):
        self.expenses = []

    def add_expense(self, expense_id, amount, category, description, date):
        """Validate and add an expense."""
        try:
            amount = float(amount)
        except (TypeError, ValueError) as error:
            raise InvalidExpenseError("Amount must be a number.") from error

        if amount <= 0:
            raise InvalidExpenseError("Amount must be greater than zero.")
        if not category or not str(category).strip():
            raise InvalidExpenseError("Category cannot be empty.")

        expense = Expense(
            expense_id=expense_id,
            amount=amount,
            category=str(category).strip(),
            description=str(description).strip(),
            date=date,
        )
        self.expenses.append(expense)
        return expense

    def list_expenses(self):
        """Return all expenses."""
        return list(self.expenses)

    def calculate_total(self):
        """Return the total amount of all expenses."""
        return sum(expense.amount for expense in self.expenses)

    def filter_by_category(self, category):
        """Return expenses matching a category, ignoring letter case."""
        if not category or not str(category).strip():
            raise InvalidExpenseError("Category cannot be empty.")

        category = str(category).strip().lower()
        return [
            expense
            for expense in self.expenses
            if expense.category.lower() == category
        ]
