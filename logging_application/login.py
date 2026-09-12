import logging

from exceptions import LoginError


logger = logging.getLogger("application")


def login():
    """Handle user login."""

    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not username:
        logger.error("Username was empty")
        raise LoginError("Username cannot be empty.")

    if not password:
        logger.error("Password was empty")
        raise LoginError("Password cannot be empty.")

    # Simple login for assignment purposes
    if username == "admin" and password == "admin123":
        logger.info("User logged in")
        return True

    logger.warning("Invalid login attempt")
    raise LoginError("Invalid username or password.")
