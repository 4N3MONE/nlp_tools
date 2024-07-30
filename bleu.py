import evaluate

def calc_bleu(sentence1, sentence2):
    bleu = evaluate.load('bleu')
    results = bleu.compute(predictions=[sentence1], references=[sentence2])
    return results['bleu']