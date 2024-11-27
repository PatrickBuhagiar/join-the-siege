from werkzeug.datastructures import FileStorage

from src.file_processing.file_processor_factory import FileProcessorFactory


def test_image_processor():
    with open("files/sample.png", "rb") as f:
        file = FileStorage(f, filename="sample.jpg")
        processor = FileProcessorFactory.get_processor(file)
        text = processor.parse_text(file)

    """ 
     Look at that subtle off-ocr text. The tasteful inaccuracies of it
     """
    assert text == ('212 555 6342 Pierce & Pierce\n'
                    '\n'
                    'Merazrs AND AcquisiTIONS\n'
                    '\n'
                    'Patrick BATEMAN\n'
                    'Vice Presipent\n'
                    '\n'
                    '358 Excuance Ptace, New York, N.Y. 100099 Fax 212.555 6390 THEX TO 45 3.4')
