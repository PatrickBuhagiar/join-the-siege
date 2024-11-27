import os

import pytest
from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor_factory import FileProcessorFactory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")


def test_pdf_processor():
    pdf_path = os.path.join(FILES_DIR, "sample.pdf")

    with open(pdf_path, "rb") as f:
        file = FileStorage(f, filename="sample.pdf")
        processor = FileProcessorFactory.get_processor(file)
        text = processor.parse_text(file)

        """
        Interesting that `Description` read as Descrip2on...
        """
        expected_text = (
            "Bank of Wakanda  Account Holder:  T'Challa  Account Number: "
            "XXXX-XXXX-XXXX-6782  Statement Period: 2023-02  Date Descrip2on Debit ($) "
            "Credit ($) 14/02/2023 Wire Transfer 147,000  09/02/2023 ATM Withdrawal  "
            "245.51    End of Statement"
        )
        assert text == expected_text, f"Expected:\n{expected_text}\nBut got:\n{text}"


def test_corrupted_pdf_file():
    corrupted_pdf_path = os.path.join(FILES_DIR, "corrupted.pdf")

    with open(corrupted_pdf_path, "rb") as f:
        file = FileStorage(f, filename="corrupted.pdf")
        processor = FileProcessorFactory.get_processor(file)
        with pytest.raises(ValueError, match="Error processing PDF"):
            processor.parse_text(file)


def test_empty_file():
    empty_pdf_path = os.path.join(FILES_DIR, "empty.pdf")

    with open(empty_pdf_path, "rb") as f:
        file = FileStorage(f, filename="empty.pdf")
        processor = FileProcessorFactory.get_processor(file)
        result = processor.parse_text(file)
        assert result == "", "Empty file should return an empty string"
