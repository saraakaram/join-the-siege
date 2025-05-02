from src.constants.file_extensions import ALLOWED_EXTENSIONS

def allowed_file(filename: str) -> bool:
    """
    Extracts filename.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
