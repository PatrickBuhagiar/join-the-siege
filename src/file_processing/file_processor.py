from abc import ABC, abstractmethod

from werkzeug.datastructures import FileStorage

""" 
Abstract class for processing files.
"""


class FileProcessor(ABC):
    @abstractmethod
    def parse_text(self, file: FileStorage) -> str:
        pass
