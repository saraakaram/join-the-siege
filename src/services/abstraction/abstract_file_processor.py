from abc import ABC, abstractmethod
from werkzeug.datastructures import FileStorage

class AbstractFileProcessor(ABC):
    @abstractmethod
    def process(self, file: FileStorage) -> str: pass