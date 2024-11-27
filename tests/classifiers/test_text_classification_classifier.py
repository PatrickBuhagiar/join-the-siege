from unittest.mock import patch

import torch

from src.classifiers.text_classification_classifier import TextClassificationClassifier


@patch("src.classifiers.text_classification_classifier.pipeline")
def test_text_classification_classifier(mock_pipeline):
    """Test classification using TextClassificationClassifier."""
    # Configure the mock pipeline to return a nested structure similar to the real pipeline
    mock_pipeline.return_value = lambda text: [
        [
            {"label": "LABEL_0", "score": 0.9},
            {"label": "LABEL_1", "score": 0.05},
            {"label": "LABEL_2", "score": 0.05},
            {"label": "LABEL_3", "score": 0.0},
        ]
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

    # Verify pipeline was called with the correct arguments
    device = 0 if torch.cuda.is_available() else -1
    mock_pipeline.assert_called_once_with("text-classification", model="bert-base-uncased", device=device,
                                          top_k=None)
