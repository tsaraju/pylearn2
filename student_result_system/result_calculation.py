from exceptions import InvalidMarksError


def validate_marks(marks):
    """Validate that all marks are numeric and between 0 and 100."""

    if len(marks) != 5:
        raise InvalidMarksError("Marks must be provided for exactly 5 subjects.")

    for mark in marks:
        if not isinstance(mark, (int, float)):
            raise InvalidMarksError("Marks must be numeric.")

        if mark < 0 or mark > 100:
            raise InvalidMarksError(
                f"Invalid mark {mark}. Marks must be between 0 and 100."
            )


def calculate_total(marks):
    validate_marks(marks)
    return sum(marks)


def calculate_percentage(marks):
    validate_marks(marks)

    try:
        total = calculate_total(marks)
        return total / 5
    except (ZeroDivisionError, TypeError) as error:
        raise ArithmeticError(
            f"Unable to calculate percentage: {error}"
        )


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def calculate_status(marks):
    validate_marks(marks)

    # A student must score at least 35 in every subject.
    return "PASS" if all(mark >= 35 for mark in marks) else "FAIL"


def calculate_result(marks):
    """Calculate total, percentage, grade, and pass/fail status."""

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    status = calculate_status(marks)

    return total, percentage, grade, status
