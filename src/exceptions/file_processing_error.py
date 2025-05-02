class FileProcessingError(Exception):
    """ Raised when processing a file fails. """
    def __init__(self, message: str):
        super().__init__(f"Failed to process file: {message}")
