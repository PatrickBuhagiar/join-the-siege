from werkzeug.datastructures import FileStorage

from src.classifiers.classifier import BaseClassifier, classify_text
from src.file_processing.file_processor_factory import FileProcessorFactory

labels = ["drivers_license", "bank_statement", "invoice", "unknown"]


class DocumentClassifierService:
    def __init__(self, classifier: BaseClassifier):
        self.classifier = classifier

    def classify(self, file: FileStorage) -> str:
        try:
            # get the right file processor
            processor = FileProcessorFactory.get_processor(file)

            # Extract text from the file
            file_text = processor.parse_text(file)
            joined_text = file.filename + " " + file_text

            # Use classify_text for label selection
            return classify_text(joined_text, self.classifier, labels)
        except Exception as e:
            raise ValueError(f"Error classifying document: {e}")
