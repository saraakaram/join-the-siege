from io import BytesIO
from werkzeug.datastructures import FileStorage

from src.services.abstraction.abstract_file_processor import AbstractFileProcessor
from src.exceptions.file_processing_error import FileProcessingError
from docx import Document

class WordProcessor(AbstractFileProcessor):
    """ Processes Word Files"""
    def process(self, file: FileStorage) -> str:
        try:
            docx_stream = BytesIO(file.read())
            document = Document(docx_stream)
            text = "\n".join([para.text for para in document.paragraphs])
            return text
        except Exception as e:
            raise FileProcessingError(str(e))

