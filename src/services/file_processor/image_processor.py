from io import BytesIO
from src.services.abstraction.abstract_file_processor import AbstractFileProcessor
from src.exceptions.file_processing_error import FileProcessingError
from werkzeug.datastructures import FileStorage
import easyocr
from PIL import Image
import numpy as np

reader = easyocr.Reader(['en'], gpu=False) # Loads once when the module is imported

class ImageProcessor(AbstractFileProcessor):
    """ Processes image files """
    def process(self, file: FileStorage) -> str:
        try:
            image = Image.open(BytesIO(file.read())).convert("RGB")
            img_np = np.array(image)
            result = reader.readtext(img_np, detail=0)
            file.stream.seek(0)
            text = "\n".join(result)
            if not text.strip():
                raise FileProcessingError("No text found in PNG.")
            return text
        except Exception as e:
            raise FileProcessingError(str(e))
