from unittest.mock import patch

from src.classifiers.text_classification_classifier import TextClassificationClassifier


@patch("src.classifiers.text_classification_classifier.pipeline")
def test_text_classification_classifier(mock_pipeline):
    """Test classification using TextClassificationClassifier."""
    # Configure the mock pipeline
    mock_pipeline.return_value = lambda x: [
        {"label": "drivers_license", "score": 0.9},
        {"label": "bank_statement", "score": 0.05},
        {"label": "invoice", "score": 0.05},
        {"label": "unknown", "score": 0.0},
    ]

    # Instantiate the classifier
    classifier = TextClassificationClassifier()

    # Test input text
    text = "This is a driver's license."
    labels = ["drivers_license", "bank_statement", "invoice", "unknown"]

    # Call the classify method
    result = classifier.classify(text, labels)

    # Expected result
    expected_result = {
        "drivers_license": 0.9,
        "bank_statement": 0.05,
        "invoice": 0.05,
        "unknown": 0.0,
    }

    # Assertions
    assert result == expected_result, "The classifier did not return the expected scores."
    mock_pipeline.assert_called_once_with("text-classification", model="bert-base-uncased", return_all_scores=True)
