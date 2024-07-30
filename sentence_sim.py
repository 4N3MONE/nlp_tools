import torch
from transformers import AutoModel, AutoTokenizer

class SentenceSim:
    SCALE_FACTOR = 100

    def __init__(self, model_path='BM-K/KoDiffCSE-RoBERTa'):
        # self.device = 'cuda' if torch.cuda.is_available else 'cpu'
        self.device = 'cpu'
        self.model = AutoModel.from_pretrained(model_path).to(self.device)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path) 

    def _get_embeddings(self, sentence: str):
        input_ids = self.tokenizer(sentence, padding=True, truncation=True, return_tensors='pt').to(self.device)
        outputs = self.model(**input_ids, return_dict=False)[0]  # outputs shape is (batch_size, seq_length, hidden_dim)
        embeddings = outputs.mean(dim=1)  # 평균 임베딩 계산 (batch_size, hidden_dim)
        return embeddings

    
    def _cosine_similarity(self, emb1, emb2) :
        if len(emb1.shape) == 1: emb1 = emb1.unsqueeze(0)
        if len(emb2.shape) == 1: emb2 = emb2.unsqueeze(0)

        emb1_norm = emb1 / emb1.norm(dim=1)[:, None]
        emb2_norm = emb2 / emb2.norm(dim=1)[:, None]
        return (emb1_norm @ emb2_norm.transpose(0, 1)).item() * self.SCALE_FACTOR
    
    def cal_score(self,label_sentence:str,compare_sentence:str) ->float : 

        label_embeddings = self._get_embeddings(label_sentence)
        compare_embeddings = self._get_embeddings(compare_sentence)

        return round(self._cosine_similarity(label_embeddings, compare_embeddings),3)


