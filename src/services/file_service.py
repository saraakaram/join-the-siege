from werkzeug.datastructures import FileStorage
from src.constants.file_extensions import ALLOWED_EXTENSIONS
from src.services.file_processor.processor_factory import get_processor

def allowed_file(filename: str) -> bool:
    """
    Extracts filename.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_extension(filename: str) -> str:
    """
    Extracts file extension.
    """
    return filename.rsplit('.', 1)[1].lower()

def is_valid(extension: str) -> bool:
    """
    Checks if extension is allowed.
    """
    return extension in ALLOWED_EXTENSIONS

def process_file(file: FileStorage) -> str:
    """
    Validates and processes file.
    Returns file content.
    """
    file_extension = get_file_extension(file.filename)

    if not is_valid(file_extension):
        raise TypeError("Invalid file type.")
    
    file_processor = get_processor(file_extension)
    return file_processor.process(file)