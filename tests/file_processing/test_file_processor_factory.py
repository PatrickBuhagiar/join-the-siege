import os

import pytest
from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor_factory import FileProcessorFactory
from src.file_processing.image_processor import ImageProcessor
from src.file_processing.pdf_processor import PDFProcessor

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")


def test_unsupported_file_type():
    txt_path = os.path.join(FILES_DIR, "sample.txt")
    with open(txt_path, "rb") as f:
        file = FileStorage(f, filename="sample.txt")
        with pytest.raises(ValueError, match="Unsupported file type: txt"):
            FileProcessorFactory.get_processor(file)


@pytest.mark.parametrize(
    "filename, expected_processor",
    [
        ("sample.pdf", PDFProcessor),
        ("sample.jpg", ImageProcessor),
        ("sample.jpeg", ImageProcessor),
        ("sample.png", ImageProcessor),
    ],
)
def test_factory_returns_correct_processor(filename, expected_processor):
    # Use the parametrized file and check for correct processor
    file_path = os.path.join(FILES_DIR, filename)
    with open(file_path, "rb") as f:
        file = FileStorage(f, filename=filename)
        processor = FileProcessorFactory.get_processor(file)
        assert isinstance(processor, expected_processor), f"Expected {expected_processor}, got {type(processor)}"
