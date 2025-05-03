import re
from werkzeug.datastructures import FileStorage
from src.config import ALLOWED_EXTENSIONS
from src.services.file_processor.processor_factory import get_processor

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

def clean_content(text: str) -> str:
    """
    Cleans extracted text from the file:
    - Removes form feeds and control characters
    - Normalizes whitespace and newlines
    - Keeps alphanumeric content intact
    """
    if not text:
        return ""
    text = text.replace("\f", " ").replace("\r", " ")
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    lines = text.split('\n')
    lines = [line.strip() for line in lines if len(line.strip()) > 2]
    
    cleaned = "\n".join(lines)

    return cleaned.strip()


def process_file(file: FileStorage, file_extension: str) -> str:
    """
    Extracts and cleans file content.
    """
    file_processor = get_processor(file_extension)
    extracted_text = file_processor.process(file)
    return clean_content(extracted_text)