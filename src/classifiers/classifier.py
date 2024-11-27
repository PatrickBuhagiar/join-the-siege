from abc import ABC, abstractmethod
from typing import List, Dict

from transformers import AutoTokenizer


class BaseClassifier(ABC):
    @abstractmethod
    def classify(self, text: str, labels: List[str]) -> Dict[str, float]:
        pass


# required for handling long text
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
MAX_TOKEN_LENGTH = 512


def classify_text(text: str, classifier: BaseClassifier, labels: List[str]) -> str:
    chunks = __split_text(text)
    aggregated_scores = {label: 0 for label in labels}

    try:
        for chunk in chunks:
            scores = classifier.classify(chunk, labels)
            for label, score in scores.items():
                aggregated_scores[label] += score

        # Find the label with the highest aggregated score
        best_label = max(aggregated_scores, key=aggregated_scores.get)
        return best_label
    except Exception as e:
        return f"Error during classification: {e}"


def __split_text(text: str, max_token_length: int = MAX_TOKEN_LENGTH):
    tokens = tokenizer.tokenize(text)
    chunks = [" ".join(tokens[i:i + max_token_length]) for i in range(0, len(tokens), max_token_length)]
    return chunks
