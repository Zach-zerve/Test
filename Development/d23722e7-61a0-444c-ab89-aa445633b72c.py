import torch 

input_ids = tokenized_texts['input_ids']
attention_masks = tokenized_texts['attention_mask']


labels = torch.tensor([1, 0])