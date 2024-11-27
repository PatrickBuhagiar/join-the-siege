from typing import List, Dict

from transformers import pipeline

from src.classifiers.classifier import BaseClassifier


class ZeroShotClassificationClassifier(BaseClassifier):
    def __init__(self, model_name="facebook/bart-large-mnli"):
        self.pipeline = pipeline("zero-shot-classification", model=model_name, device=0, top_k=None)

    def classify(self, text: str, labels: List[str]) -> Dict[str, float]:
        predictions = self.pipeline(text, candidate_labels=labels)
        scores = {label: score for label, score in zip(predictions["labels"], predictions["scores"])}
        print("Scores:", scores)
        return scores
