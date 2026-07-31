import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

text = "I love NLP"
tokens = word_tokenize(text)
tags = pos_tag(tokens)

print(tags)

# Output:

# [('I', 'PRP'), ('love', 'VBP'), ('NLP', 'NNP')]