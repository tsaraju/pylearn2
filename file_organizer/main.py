import sys
from pathlib import Path

from file_detector import detect_file_category
from file_mover import move_file
from exceptions import (
    UnsupportedFileError,
    FileNotFoundErrorCustom,
    DestinationFolderError
)
from logger import log_success, log_failure


def organize_folder(folder_path):
    folder = Path(folder_path)

    # Check whether the source folder exists
    if not folder.exists():
        message = f"Source folder does not exist: {folder}"
        log_failure(message)
        print(message)
        return

    if not folder.is_dir():
        message = f"Path is not a folder: {folder}"
        log_failure(message)
        print(message)
        return

    # Process files in the folder
    for file_path in folder.iterdir():

        if not file_path.is_file():
            continue

        try:
            category = detect_file_category(file_path)

            destination = folder / category

            move_file(file_path, destination)

            print(
                f"Moved: {file_path.name} -> {category}/"
            )

        except UnsupportedFileError as error:
            log_failure(str(error))
            print(f"Skipped: {file_path.name} - {error}")

        except FileNotFoundErrorCustom as error:
            log_failure(str(error))
            print(f"Error: {error}")

        except DestinationFolderError as error:
            log_failure(str(error))
            print(f"Error: {error}")

        except PermissionError as error:
            log_failure(
                f"Permission error for {file_path}: {error}"
            )
            print(
                f"Permission denied: {file_path.name}"
            )

        except OSError as error:
            log_failure(
                f"OS error while processing {file_path}: {error}"
            )
            print(
                f"Could not process {file_path.name}: {error}"
            )


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <folder_path>")
        return

    folder_path = sys.argv[1]

    organize_folder(folder_path)


if __name__ == "__main__":
    main()
