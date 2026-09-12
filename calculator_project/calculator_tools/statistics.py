def _validate_values(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("Values must be a list or tuple.")

    if not values:
        raise ValueError("Values cannot be empty.")

    if any(
        not isinstance(value, (int, float)) or isinstance(value, bool)
        for value in values
    ):
        raise TypeError("All values must be numbers.")


def percentage(value, total):
    """Calculate what percentage value is of total."""
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Value must be a number.")

    if not isinstance(total, (int, float)) or isinstance(total, bool):
        raise TypeError("Total must be a number.")

    if total == 0:
        raise ZeroDivisionError("Total cannot be zero.")

    return (value / total) * 100


def average(values):
    """Calculate the arithmetic mean of a collection of numbers."""
    _validate_values(values)
    return sum(values) / len(values)
