"""
Here I'm using a factory pattern to create the appropriate processor based on the file type.
Using this pattern will create a clean, maintainable, and extensible solution.
"""

from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor import FileProcessor
from src.file_processing.image_processor import ImageProcessor
from src.file_processing.pdf_processor import PDFProcessor


class FileProcessorFactory:
    @staticmethod
    def get_processor(file: FileStorage) -> FileProcessor:
        """Returns the appropriate processor based on file type."""
        file_extension = file.filename.rsplit('.', 1)[-1].lower()
        if file_extension == "pdf":
            return PDFProcessor()
        elif file_extension in {"jpg", "jpeg", "png"}:
            return ImageProcessor()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")
