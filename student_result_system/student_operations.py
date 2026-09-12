import logging

from exceptions import InvalidMarksError, MissingStudentInfoError
from result_calculation import calculate_result


def read_student_details():
    """Read and validate student information."""

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()

    if not name:
        raise MissingStudentInfoError("Student name cannot be empty.")

    if not roll_number:
        raise MissingStudentInfoError("Roll number cannot be empty.")

    return name, roll_number


def read_marks():
    """Read marks for 5 subjects."""

    marks = []

    for subject_number in range(1, 6):
        value = input(
            f"Enter marks for subject {subject_number}: "
        ).strip()

        try:
            mark = float(value)
        except ValueError:
            raise InvalidMarksError(
                f"Non-numeric mark entered for subject {subject_number}."
            )

        if mark < 0 or mark > 100:
            raise InvalidMarksError(
                f"Mark for subject {subject_number} must be between 0 and 100."
            )

        marks.append(mark)

    return marks


def process_student():
    """Read one student's data and calculate the result."""

    name, roll_number = read_student_details()
    marks = read_marks()

    total, percentage, grade, status = calculate_result(marks)

    return {
        "name": name,
        "roll_number": roll_number,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": status
    }


def display_result(result):
    """Display a student's result."""

    print("\n----- Student Result -----")
    print(f"Name       : {result['name']}")
    print(f"Roll Number: {result['roll_number']}")
    print(f"Total      : {result['total']:.2f}")
    print(f"Percentage : {result['percentage']:.2f}%")
    print(f"Grade      : {result['grade']}")
    print(f"Status     : {result['status']}")
    print("--------------------------")


def process_students(number_of_students):
    """Process all students without stopping after an error."""

    for student_number in range(1, number_of_students + 1):
        print(f"\nProcessing Student {student_number}")

        try:
            result = process_student()
            display_result(result)

        except (
            InvalidMarksError,
            MissingStudentInfoError,
            ArithmeticError
        ) as error:
            logging.error(
                "Error processing student %d: %s",
                student_number,
                error
            )
            print(
                f"Error processing Student {student_number}: {error}"
            )
            print("Error logged. Continuing with the next student...\n")

        except Exception as error:
            # Handles unexpected errors without terminating the program.
            logging.exception(
                "Unexpected error while processing student %d",
                student_number
            )
            print(
                f"Unexpected error for Student {student_number}: {error}"
            )
            print("Error logged. Continuing with the next student...\n")
