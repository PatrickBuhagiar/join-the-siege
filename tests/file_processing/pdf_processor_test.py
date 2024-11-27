import pytest
from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor_factory import FileProcessorFactory


def test_pdf_processor():
    with open("files/sample.pdf", "rb") as f:
        file = FileStorage(f, filename="sample.pdf")
        processor = FileProcessorFactory.get_processor(file)
        text = processor.parse_text(file)

        """
        Interesting that `Description` read as Descrip2on...
        """
        assert text == ("Bank of Wakanda  Account Holder:  T'Challa  Account Number: "
                        'XXXX-XXXX-XXXX-6782  Statement Period: 2023-02  Date Descrip2on Debit ($) '
                        'Credit ($) 14/02/2023 Wire Transfer 147,000  09/02/2023 ATM Withdrawal  '
                        '245.51    End of Statement')


def test_corrupted_pdf_file():
    with open("files/corrupted.pdf", "rb") as f:
        file = FileStorage(f, filename="corrupted.pdf")
        processor = FileProcessorFactory.get_processor(file)
        with pytest.raises(ValueError, match="Error processing PDF"):
            processor.parse_text(file)


def test_empty_file():
    with open("files/empty.pdf", "rb") as f:
        file = FileStorage(f, filename="empty.pdf")
        processor = FileProcessorFactory.get_processor(file)
        result = processor.parse_text(file)
        assert result == "", "Empty file should return an empty string"
