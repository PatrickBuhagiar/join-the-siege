from src.classifiers.zero_shot_classification_classifier import ZeroShotClassificationClassifier
from src.services.document_classifier_service import DocumentClassifierService

_service_instance = None


def get_document_classifier_service():
    """
    Return a singleton instance of DocumentClassifierService.

    Returns:
        DocumentClassifierService: Singleton instance.
    """
    global _service_instance
    if _service_instance is None:
        """
        I've experimented with two different classifiers for this exercise:
        1. text-classification (BERT)
        2. zero-shot-classification (BART)

        Both could work, but there are a few trade offs for each:
        Feature           \ text-classification              | zero-shot-classification
        --------------------------------------------------------------------------------------------------
        Label Flexibility | Static (predefined labels)       | Dynamic (labels at runtime)
        Fine tuning       | high, can fine tune for accuracy | fine-tuning not needed, works out of the box
        Inference speed   | faster                           | slower

        While testing, I found that zero-shot-classification is slower than text-classification but got 8/9 of the file classifications correct.
        text-classification will require some fine-tuning to get the same accuracy, which will take time and some tinkering.
        
        ultimately, I chose zero-shot-classification for its ease of use and accuracy. 
        """
        classifier = ZeroShotClassificationClassifier()
        """ 
        I'm defining the classifier here, but to productionize this, it should be specified via a configuration file 
        or environment variable.
        """
        _service_instance = DocumentClassifierService(classifier)
    return _service_instance
