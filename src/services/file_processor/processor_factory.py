from src.services.file_processor.pdf_processor import PDFProcessor
from src.services.file_processor.word_processor import WordProcessor
from src.services.file_processor.excel_processor import ExcelProcessor
from src.services.file_processor.image_processor import ImageProcessor

PROCESSORS = {
    "pdf": PDFProcessor(),
    "docx": WordProcessor(),
    "xlsx": ExcelProcessor(),
    "xls": ExcelProcessor(),
    "png": ImageProcessor(),
    "jpg": ImageProcessor(),
}

def get_processor(file_extension: str):
    if file_extension not in PROCESSORS:
        raise TypeError(f"Unsupported file extension: {file_extension}")
    return PROCESSORS[file_extension]
