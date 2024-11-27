from unittest.mock import patch

import pytest


@pytest.fixture
def mock_pipeline():
    """Mock the Hugging Face pipeline."""
    with patch("your_module_name.pipeline") as mock:
        yield mock


@pytest.fixture
def mock_split_text():
    """Mock the text splitting function."""
    with patch("your_module_name.__split_text") as mock:
        mock.return_value = ["chunk 1", "chunk 2"]
        yield mock


@pytest.fixture
def labels():
    """Shared labels for classification."""
    return ["drivers_license", "bank_statement", "invoice", "unknown"]
