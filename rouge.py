from korouge_score import rouge_scorer

def ko_rouge(sentence1: str, sentence2: str) -> dict:
    #sentence1 : reference sentence
    #sentence2 : summary sentence
    scorer = rouge_scorer.RougeScorer(["rouge1", "rouge2", "rougeL", "rougeLsum"])
    result = scorer.score(sentence1, sentence2)
    
    # score(fmeasure)만 추출
    return {k: v.fmeasure for k, v in result.items()}
