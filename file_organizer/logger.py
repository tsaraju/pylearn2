import logging

LOG_FILE = "file_organizer.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("FileOrganizer")


def log_success(message):
    logger.info("SUCCESS: %s", message)


def log_failure(message):
    logger.error("FAILED: %s", message)
