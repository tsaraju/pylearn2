import logging


def setup_logging():
    """Configure application logging."""
    logging.basicConfig(
        filename="student_results.log",
        level=logging.ERROR,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
