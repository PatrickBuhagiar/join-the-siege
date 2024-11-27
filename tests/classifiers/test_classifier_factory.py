import pytest

from src.classifiers.classifier_factory import ClassifierFactory
from src.classifiers.text_classification_classifier import TextClassificationClassifier
from src.classifiers.zero_shot_classification_classifier import ZeroShotClassificationClassifier


def test_classifier_factory_text_classification():
    """Test ClassifierFactory returns TextClassificationClassifier."""
    classifier = ClassifierFactory.get_classifier("text-classification")
    assert isinstance(classifier, TextClassificationClassifier), "Incorrect classifier type for text-classification."


def test_classifier_factory_zero_shot_classification():
    """Test ClassifierFactory returns ZeroShotClassificationClassifier."""
    classifier = ClassifierFactory.get_classifier("zero-shot-classification")
    assert isinstance(classifier,
                      ZeroShotClassificationClassifier), "Incorrect classifier type for zero-shot-classification."


def test_classifier_factory_invalid_type():
    """Test ClassifierFactory with an unsupported type."""
    with pytest.raises(ValueError, match="Unsupported classifier type"):
        ClassifierFactory.get_classifier("unsupported-type")
