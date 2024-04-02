import torch
from transformers import DistilBertTokenizer

texts = ["This is a positive sentence.", "This is a negative sentence."]

tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
tokenized_texts = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
