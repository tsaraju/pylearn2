import logging
from pathlib import Path


LOG_FILE = Path("logs") / "expense_tracker.log"


def get_logger():
    """Return the application logger configured to write to the log file."""
    logger = logging.getLogger("expense_tracker")

    if not logger.handlers:
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

        handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
