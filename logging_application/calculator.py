import logging

from exceptions import CalculationError


logger = logging.getLogger("application")


def calculate():
    """Perform a simple calculation."""

    logger.debug("Calculation operation started")

    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))

        operator = input(
            "Enter operation (+, -, *, /): "
        ).strip()

        if operator == "+":
            result = first + second

        elif operator == "-":
            result = first - second

        elif operator == "*":
            result = first * second

        elif operator == "/":
            if second == 0:
                logger.error("Division by zero attempted")
                raise CalculationError(
                    "Cannot divide by zero."
                )

            result = first / second

        else:
            logger.warning(
                "Invalid calculation operator entered"
            )
            raise CalculationError(
                "Invalid operator."
            )

        logger.info("Calculation completed")

        print(f"Result: {result}")

    except ValueError:
        logger.error("Non-numeric value entered")
        raise CalculationError(
            "Please enter valid numbers."
        )

    except CalculationError:
        raise

    except Exception as error:
        logger.exception(
            "Unexpected calculation error: %s",
            error
        )
        raise CalculationError(
            "Calculation failed."
        )
