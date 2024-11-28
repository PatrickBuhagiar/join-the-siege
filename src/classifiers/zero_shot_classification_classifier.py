from typing import List, Dict

import torch
from transformers import pipeline

from src.classifiers.classifier import BaseClassifier


class ZeroShotClassificationClassifier(BaseClassifier):
    def __init__(self, model_name="facebook/bart-large-mnli"):
        # Use GPU if available, otherwise fall back to CPU
        device = 0 if torch.cuda.is_available() else -1
        self.pipeline = pipeline("zero-shot-classification", model=model_name, device=device, return_all_scores=True)

    def classify(self, text: str, labels: List[str]) -> Dict[str, float]:
        predictions = self.pipeline(text, candidate_labels=labels)
        scores = {label: score for label, score in zip(predictions["labels"], predictions["scores"])}
        print("Scores:", scores)
        return scores
