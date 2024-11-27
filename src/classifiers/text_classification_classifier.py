from typing import List, Dict

import torch
from transformers import pipeline

from src.classifiers.classifier import BaseClassifier


class TextClassificationClassifier(BaseClassifier):
    def __init__(self, model_name="bert-base-uncased"):
        device = 0 if torch.cuda.is_available() else -1
        self.pipeline = pipeline("text-classification", model=model_name, device=device, top_k=None)

    def classify(self, text: str, labels: List[str]) -> Dict[str, float]:
        # Get predictions from the pipeline
        predictions = self.pipeline(text)

        # Handle nested structure
        scores = {label: 0 for label in labels}  # Initialize scores

        # Iterate through the predictions and map them to the provided labels
        for pred in predictions[0]:  # Access the first (and likely only) list
            label_idx = int(pred['label'].split('_')[-1])  # Extract numeric part of label
            if label_idx < len(labels):  # Ensure label index is within range
                scores[labels[label_idx]] += pred['score']

        print("Scores:", scores)
        return scores
