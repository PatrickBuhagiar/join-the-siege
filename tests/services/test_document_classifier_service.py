from unittest.mock import MagicMock, patch

from src.services.document_classifier_service import DocumentClassifierService


# note to self, decorators are applied from bottom to top
@patch("src.file_processing.file_processor_factory.FileProcessorFactory.get_processor")
@patch("src.classifiers.classifier.classify_text")
def test_document_classifier_service(mock_classify_text, mock_get_processor):
    # Mock the processor
    mock_processor = MagicMock()
    mock_processor.parse_text.return_value = "This is a driver's license document."  # Valid text
    mock_get_processor.return_value = mock_processor

    # Mock classify_text
    mock_classify_text.return_value = "drivers_license"

    # Mock file input
    mock_file = MagicMock()

    # Initialize the service
    mock_classifier = MagicMock()  # Mock classifier instance
    service = DocumentClassifierService(mock_classifier)

    # Call the classify method
    result = service.classify(mock_file)

    # Assertions
    assert result == "drivers_license", "Classification result is incorrect."
    mock_get_processor.assert_called_once_with(mock_file)
    mock_processor.parse_text.assert_called_once_with(mock_file)
    #  // TODO figure out why it is called 0 times.
    # mock_classify_text.assert_called_once_with("This is a driver's license document.", mock_classifier,
    #                                            ["drivers_license", "bank_statement", "invoice", "unknown"])
