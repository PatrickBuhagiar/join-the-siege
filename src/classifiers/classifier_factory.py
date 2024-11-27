from src.classifiers.classifier import BaseClassifier
from src.classifiers.text_classification_classifier import TextClassificationClassifier
from src.classifiers.zero_shot_classification_classifier import ZeroShotClassificationClassifier


class ClassifierFactory:
    @staticmethod
    def get_classifier(type_: str) -> BaseClassifier:
        if type_ == "text-classification":
            return TextClassificationClassifier()
        elif type_ == "zero-shot-classification":
            return ZeroShotClassificationClassifier()
        else:
            raise ValueError(f"Unsupported classifier type: {type_}")
