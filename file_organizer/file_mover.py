import shutil
from pathlib import Path

from exceptions import (
    FileNotFoundErrorCustom,
    DestinationFolderError
)
from logger import log_success, log_failure


def move_file(file_path, destination_folder):
    """
    Move a file to the specified destination folder.
    Handles duplicate filenames and permission errors.
    """

    source = Path(file_path)
    destination = Path(destination_folder)

    # Check whether source file exists
    if not source.exists():
        message = f"File does not exist: {source}"
        log_failure(message)
        raise FileNotFoundErrorCustom(message)

    if not source.is_file():
        message = f"Not a file: {source}"
        log_failure(message)
        raise FileNotFoundErrorCustom(message)

    # Create destination folder if it does not exist
    try:
        destination.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        message = f"Permission denied while creating folder: {destination}"
        log_failure(message)
        raise DestinationFolderError(message)
    except OSError as error:
        message = f"Could not create destination folder {destination}: {error}"
        log_failure(message)
        raise DestinationFolderError(message)

    # Handle duplicate filenames
    target = destination / source.name

    if target.exists():
        counter = 1

        while True:
            new_name = f"{source.stem}_{counter}{source.suffix}"
            target = destination / new_name

            if not target.exists():
                break

            counter += 1

    # Move the file
    try:
        shutil.move(str(source), str(target))

        log_success(
            f"Moved '{source}' to '{target}'"
        )

        return target

    except PermissionError:
        message = f"Permission denied while moving '{source}'"
        log_failure(message)
        raise

    except OSError as error:
        message = f"Failed to move '{source}': {error}"
        log_failure(message)
        raise
