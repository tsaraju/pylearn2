from .exceptions import InvalidOperationError


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError("Temperature must be a number.")

    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    if not isinstance(fahrenheit, (int, float)) or isinstance(fahrenheit, bool):
        raise TypeError("Temperature must be a number.")

    return (fahrenheit - 32) * 5 / 9


def convert_length(value, from_unit, to_unit):
    """Convert between simple length units."""

    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise TypeError("Value must be a number.")

    conversions = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
    }

    if from_unit not in conversions:
        raise InvalidOperationError(
            f"Unsupported source unit: {from_unit}"
        )

    if to_unit not in conversions:
        raise InvalidOperationError(
            f"Unsupported target unit: {to_unit}"
        )

    meters = value * conversions[from_unit]
    return meters / conversions[to_unit]
