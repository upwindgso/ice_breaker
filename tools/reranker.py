import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-reranker-v2-m3')
model = AutoModelForSequenceClassification.from_pretrained('BAAI/bge-reranker-v2-m3')
model.eval()

def rerank_results(query, passages):
    pairs = [[query, passage] for passage in passages]
    
    with torch.no_grad():
        inputs = tokenizer(pairs, padding=True, truncation=True, 
                         return_tensors='pt', max_length=512)
        scores = model(**inputs, return_dict=True).logits.view(-1,).float()
    
    return scores