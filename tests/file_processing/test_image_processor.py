import difflib
import os

from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor_factory import FileProcessorFactory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")


def test_image_processor():
    image_path = os.path.join(FILES_DIR, "sample.png")

    with open(image_path, "rb") as f:
        file = FileStorage(f, filename="sample.png")  # Ensure filename matches the file type
        processor = FileProcessorFactory.get_processor(file)
        text = processor.parse_text(file)

    """
    Look at that subtle off-ocr text. The tasteful inaccuracies of it.
    """
    expected_text = (
        '212 555 6342 Pierce & Pierce\n'
        '\n'
        'Merazrs AND AcquisiTIONS\n'
        '\n'
        'Patrick BATEMAN\n'
        'Vice Presipent\n'
        '\n'
        '358 Excuance Ptace, New York, N.Y. 100099 Fax 212.555 6390 THEX TO 45 3.4'
    )

    similarity = difflib.SequenceMatcher(None, text, expected_text).ratio()
    assert similarity > 0.85, f"OCR output similarity too low: {similarity}\nExpected:\n{expected_text}\nGot:\n{text}"
