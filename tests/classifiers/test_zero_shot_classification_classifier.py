from unittest.mock import patch

from src.classifiers.zero_shot_classification_classifier import ZeroShotClassificationClassifier


@patch("src.classifiers.zero_shot_classification_classifier.pipeline")
def test_zero_shot_classification_classifier(mock_pipeline, labels):
    """Test classification using ZeroShotClassificationClassifier."""
    # Configure mock pipeline
    mock_pipeline.return_value = lambda text, candidate_labels: {
        "labels": candidate_labels,
        "scores": [0.7, 0.2, 0.1, 0.0],
    }

    # Initialize the classifier
    classifier = ZeroShotClassificationClassifier()

    # Call the classify method
    text = "This is a driver's license document."
    result = classifier.classify(text, labels)

    # Expected result
    expected_result = {
        "drivers_license": 0.7,
        "bank_statement": 0.2,
        "invoice": 0.1,
        "unknown": 0.0,
    }

    # Assertions
    assert result == expected_result, "Classifier returned incorrect scores."
    mock_pipeline.assert_called_once_with("zero-shot-classification", model="facebook/bart-large-mnli")
