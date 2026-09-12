from calculator_tools import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
    percentage,
    average,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_length,
    InvalidOperationError,
)


def main():
    print("=== Calculator Tools Demo ===")

    # Basic arithmetic
    print("\nArithmetic:")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))

    # Using the generic calculate function
    print("\nGeneric calculation:")
    print("20 + 4 =", calculate(20, 4, "add"))
    print("20 / 4 =", calculate(20, 4, "divide"))

    # Percentage
    print("\nPercentage:")
    print("25 is", percentage(25, 100), "% of 100")

    # Average
    print("\nAverage:")
    numbers = [10, 20, 30, 40, 50]
    print("Average:", average(numbers))

    # Temperature conversion
    print("\nTemperature conversion:")
    print("25 C =", celsius_to_fahrenheit(25), "F")
    print("77 F =", fahrenheit_to_celsius(77), "C")

    # Unit conversion
    print("\nLength conversion:")
    print("5 km =", convert_length(5, "km", "m"), "m")
    print("250 cm =", convert_length(250, "cm", "m"), "m")

    # Error handling
    print("\nError handling:")

    try:
        divide(10, 0)
    except ZeroDivisionError as error:
        print("Division error:", error)

    try:
        average([])
    except ValueError as error:
        print("Value error:", error)

    try:
        add(10, "5")
    except TypeError as error:
        print("Type error:", error)

    try:
        convert_length(10, "mile", "km")
    except InvalidOperationError as error:
        print("Operation error:", error)


if __name__ == "__main__":
    main()
