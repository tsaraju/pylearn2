class UnsupportedFileError(Exception):
    """Raised when a file extension is not supported."""
    pass


class FileNotFoundErrorCustom(Exception):
    """Raised when the requested file does not exist."""
    pass


class DestinationFolderError(Exception):
    """Raised when the destination folder is missing or cannot be created."""
    pass
