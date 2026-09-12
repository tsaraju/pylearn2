import logging

from logger_config import setup_logging
from login import login
from calculator import calculate
from file_operations import read_file, write_file
from exceptions import (
    LoginError,
    CalculationError,
    FileOperationError
)


# Configure logging
application_logger, error_logger = setup_logging()


def main():
    logged_in = False

    application_logger.info("Application started")

    while True:

        print("\n==========================")
        print("     MENU")
        print("==========================")
        print("1. Login")
        print("2. Calculate")
        print("3. Read a File")
        print("4. Write a File")
        print("5. Logout")
        print("6. Exit")
        print("==========================")

        choice = input("Enter your choice: ").strip()

        application_logger.debug(
            "User selected menu option: %s",
            choice
        )

        # LOGIN
        if choice == "1":

            try:
                logged_in = login()

            except LoginError as error:
                error_logger.error(
                    "Login error: %s",
                    error
                )
                print(f"Login failed: {error}")

            except Exception as error:
                error_logger.exception(
                    "Unexpected login failure: %s",
                    error
                )
                print("Unexpected login error.")

        # CALCULATE
        elif choice == "2":

            if not logged_in:
                application_logger.warning(
                    "Calculation attempted without login"
                )
                print("Please login first.")
                continue

            try:
                calculate()

            except CalculationError as error:
                error_logger.error(
                    "Calculation error: %s",
                    error
                )
                print(f"Calculation failed: {error}")

            except Exception as error:
                error_logger.exception(
                    "Unexpected calculation failure: %s",
                    error
                )
                print("Unexpected calculation error.")

        # READ FILE
        elif choice == "3":

            if not logged_in:
                application_logger.warning(
                    "File read attempted without login"
                )
                print("Please login first.")
                continue

            try:
                read_file()

            except FileOperationError as error:
                error_logger.error(
                    "File reading error: %s",
                    error
                )
                print(f"File reading failed: {error}")

            except Exception as error:
                error_logger.exception(
                    "Unexpected file reading failure: %s",
                    error
                )
                print("Unexpected file reading error.")

        # WRITE FILE
        elif choice == "4":

            if not logged_in:
                application_logger.warning(
                    "File write attempted without login"
                )
                print("Please login first.")
                continue

            try:
                write_file()

            except FileOperationError as error:
                error_logger.error(
                    "File writing error: %s",
                    error
                )
                print(f"File writing failed: {error}")

            except Exception as error:
                error_logger.exception(
                    "Unexpected file writing failure: %s",
                    error
                )
                print("Unexpected file writing error.")

        # LOGOUT
        elif choice == "5":

            if logged_in:
                logged_in = False
                application_logger.info("User logged out")
                print("Successfully logged out.")

            else:
                application_logger.warning(
                    "Logout attempted while not logged in"
                )
                print("You are not logged in.")

        # EXIT
        elif choice == "6":

            application_logger.info("Application stopped")
            print("Goodbye!")
            break

        else:
            application_logger.warning(
                "Invalid menu option: %s",
                choice
            )
            print("Invalid choice. Please try again.")


if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        application_logger.warning(
            "Application interrupted by user"
        )
        print("\nApplication interrupted.")

    except Exception as error:
        error_logger.critical(
            "Unexpected application failure: %s",
            error,
            exc_info=True
        )
        print(
            "CRITICAL: Unexpected application failure."
        )
