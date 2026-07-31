from nltk.util import ngrams

text = "I love learning NLP"
words = text.split()

# Unigram
unigrams = list(ngrams(words, 1))

# Bigram
bigrams = list(ngrams(words, 2))

# Trigram
trigrams = list(ngrams(words, 3))

print("Unigrams:", unigrams)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)


# OutPut

# Unigrams: [('I',), ('love',), ('learning',), ('NLP',)]

# Bigrams: [('I', 'love'), ('love', 'learning'), ('learning', 'NLP')]

# Trigrams: [('I', 'love', 'learning'), ('love', 'learning', 'NLP')]