from pathlib import Path
from exceptions import UnsupportedFileError


FILE_CATEGORIES = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    ".txt": "Text",
    ".md": "Text",

    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",

    ".csv": "Data",
    ".xlsx": "Data",
    ".xls": "Data",

    ".mp3": "Audio",
    ".wav": "Audio",

    ".mp4": "Videos",
    ".mkv": "Videos",
}


def detect_file_category(file_path):
    """
    Determine the destination category based on file extension.
    """

    extension = Path(file_path).suffix.lower()

    if extension not in FILE_CATEGORIES:
        raise UnsupportedFileError(
            f"Unsupported file type: {extension or 'no extension'}"
        )

    return FILE_CATEGORIES[extension]
