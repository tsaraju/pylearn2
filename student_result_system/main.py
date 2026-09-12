import logging

from logging_config import setup_logging
from student_operations import process_students


def main():
    setup_logging()

    try:
        value = input("Enter the number of students: ").strip()

        try:
            number_of_students = int(value)

            if number_of_students <= 0:
                raise ValueError(
                    "Number of students must be greater than zero."
                )

        except ValueError as error:
            logging.error("Invalid number of students: %s", error)
            print(f"Invalid input: {error}")
            return

        process_students(number_of_students)

    except Exception as error:
        logging.exception("Unexpected application error: %s", error)
        print("An unexpected error occurred. Check student_results.log.")


if __name__ == "__main__":
    main()
