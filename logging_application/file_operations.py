import logging

from exceptions import FileOperationError


logger = logging.getLogger("application")


def read_file():
    """Read contents from a file."""

    filename = input("Enter file name to read: ").strip()

    logger.debug(
        "Attempting to read file: %s",
        filename
    )

    if not filename:
        logger.warning("File name was empty")
        raise FileOperationError(
            "File name cannot be empty."
        )

    try:
        with open(filename, "r") as file:
            content = file.read()

        if not content.strip():
            logger.warning("File was empty")
            print("Warning: File is empty.")
            return

        print("\nFile contents:")
        print(content)

        logger.info(
            "File read successfully: %s",
            filename
        )

    except FileNotFoundError:
        logger.error(
            "File could not be opened: %s",
            filename
        )
        raise FileOperationError(
            "File does not exist."
        )

    except PermissionError:
        logger.error(
            "Permission denied while opening file: %s",
            filename
        )
        raise FileOperationError(
            "Permission denied."
        )

    except Exception as error:
        logger.exception(
            "Unexpected file reading error: %s",
            error
        )
        raise FileOperationError(
            "Unable to read file."
        )


def write_file():
    """Write user-provided content to a file."""

    filename = input("Enter file name to write: ").strip()

    if not filename:
        logger.warning("File name was empty")
        raise FileOperationError(
            "File name cannot be empty."
        )

    content = input("Enter content to write: ")

    logger.debug(
        "Attempting to write file: %s",
        filename
    )

    try:
        with open(filename, "w") as file:
            file.write(content)

        logger.info(
            "File written successfully: %s",
            filename
        )

        print("File written successfully.")

    except PermissionError:
        logger.error(
            "Permission denied while writing file: %s",
            filename
        )
        raise FileOperationError(
            "Permission denied."
        )

    except Exception as error:
        logger.exception(
            "Unexpected file writing error: %s",
            error
        )
        raise FileOperationError(
            "Unable to write file."
        )
