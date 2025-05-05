from io import BytesIO
from src.services.abstraction.abstract_file_processor import AbstractFileProcessor
from src.exceptions.file_processing_error import FileProcessingError
from pdfminer.high_level import extract_text
from werkzeug.datastructures import FileStorage

class PDFProcessor(AbstractFileProcessor):
    """ Processes PDF Files (Except for scanned images saved as PDF)"""

    def process(self, file: FileStorage) -> str:
        try:
            stream = BytesIO(file.read())
            text = extract_text(stream)
            file.stream.seek(0)
            return text
        except Exception as e:
            raise FileProcessingError(str(e))