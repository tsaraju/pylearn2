import logging
import os


def setup_logging():
    """Configure application and error loggers."""

    os.makedirs("logs", exist_ok=True)

    # Main application log
    application_logger = logging.getLogger("application")
    application_logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if not application_logger.handlers:

        application_handler = logging.FileHandler(
            "logs/application.log"
        )

        application_handler.setLevel(logging.DEBUG)

        application_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        application_handler.setFormatter(application_formatter)

        application_logger.addHandler(application_handler)

    # Error log
    error_logger = logging.getLogger("error")
    error_logger.setLevel(logging.ERROR)

    if not error_logger.handlers:

        error_handler = logging.FileHandler(
            "logs/error.log"
        )

        error_handler.setLevel(logging.ERROR)

        error_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        error_handler.setFormatter(error_formatter)

        error_logger.addHandler(error_handler)

    return application_logger, error_logger
