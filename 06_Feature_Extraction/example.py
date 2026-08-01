

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

sentences = [
    "I love NLP",
    "I love Python",
    "NLP is interesting"
]

# Bag of Words
bow = CountVectorizer()
bow_matrix = bow.fit_transform(sentences)

print("Bag of Words Matrix:")
print(bow_matrix.toarray())
print("Vocabulary:", bow.get_feature_names_out())

# TF-IDF
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(sentences)

print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray())
print("Vocabulary:", tfidf.get_feature_names_out())


# output

#  Bag of Words Matrix:
# [[1 1 0 1 0]
#  [1 1 0 0 1]
#  [0 0 1 1 0]]

# Vocabulary: ['i' 'love' 'interesting' 'nlp' 'python']

# TF-IDF Matrix:
# [[0.58 0.58 0.00 0.58 0.00]
#  [0.58 0.58 0.00 0.00 0.58]
#  [0.00 0.00 0.72 0.69 0.00]]

# Vocabulary: ['i' 'love' 'interesting' 'nlp' 'python']


## feature extraction using CountVectorizer and TfidfVectorizer

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

documents = [
    "I love programming in Python.",
    "Python is a great programming language.",
    "I enjoy learning new programming languages." ]

vectorizer = CountVectorizer(ngram_range=(1, 2))  # Using unigrams and bigrams)

X = vectorizer.fit_transform(documents)

print("vocabulary:", vectorizer.get_feature_names_out())
print("Bag of Words Matrix:\n", X.toarray())


## tf-idf feature extraction using TfidfVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "I love programming in Python.",
    "Python is a great programming language.",
    "I enjoy learning new programming languages."
]

vectorizer = TfidfVectorizer() #  Using default parameters

X = vectorizer.fit_transform(documents) # just fit and transform the documents

print("vocabulary:", vectorizer.get_feature_names_out()) # build the vocabulary and print it
print("TF-IDF Matrix:\n", X.toarray())  # print the TF-IDF matrix