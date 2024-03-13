import evaluate

def calc_bleu(predictions, references):
  bleu = evaluate.load("bleu")
  results = bleu.compute(predictions=predictions, references=references)
  return results