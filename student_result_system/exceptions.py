class InvalidMarksError(Exception):
    """Raised when marks are invalid or outside the range 0-100."""
    pass


class MissingStudentInfoError(Exception):
    """Raised when required student information is missing."""
    pass
