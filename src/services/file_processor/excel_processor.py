from src.services.abstraction.abstract_file_processor import AbstractFileProcessor
from werkzeug.datastructures import FileStorage
import pandas as pd
from io import BytesIO
from werkzeug.datastructures import FileStorage
from src.exceptions.file_processing_error import FileProcessingError

class ExcelProcessor(AbstractFileProcessor):
    """ Processes Excel Files"""
    def process(self, file: FileStorage) -> str:
        try:
            excel_stream = BytesIO(file.read())
            dfs = pd.read_excel(excel_stream, sheet_name=None)
            file.stream.seek(0)

            text_chunks = []
            for sheet_name, df in dfs.items():
                text_chunks.append(f"Sheet: {sheet_name}")
                text_chunks.append(df.to_string(index=False, header=True))

            text = "\n\n".join(text_chunks)
            return text
        
        except Exception as e:
            raise FileProcessingError(str(e))

    
