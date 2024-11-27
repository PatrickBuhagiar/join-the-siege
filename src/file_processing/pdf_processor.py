"""
Concrete classes for processing PDF files.
"""
from PyPDF2 import PdfReader
from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor import FileProcessor


class PDFProcessor(FileProcessor):
    def parse_text(self, file: FileStorage) -> str:
        try:
            pdf_reader = PdfReader(file.stream)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text.strip()
        except Exception as e:
            raise ValueError(f"Error processing PDF: {e}")
