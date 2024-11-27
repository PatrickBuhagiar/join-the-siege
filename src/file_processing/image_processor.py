"""
Concrete classes for processing image files.
"""
from PIL import Image
from pytesseract import image_to_string
from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor import FileProcessor


class ImageProcessor(FileProcessor):
    def parse_text(self, file: FileStorage) -> str:
        """Extracts text from an image using OCR."""
        try:
            image = Image.open(file.stream)
            text = image_to_string(image)
            return text.strip()
        except Exception as e:
            raise ValueError(f"Error processing image: {e}")
