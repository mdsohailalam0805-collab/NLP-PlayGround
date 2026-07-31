# examples.py


from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk

# Download required data
nltk.download("wordnet")

words = ["playing", "played", "plays", "better", "running", "studies"]

# Stemming
stemmer = PorterStemmer()

print("Stemming:")
for word in words:
    print(f"{word} -> {stemmer.stem(word)}")

# Lemmatization
lemmatizer = WordNetLemmatizer()

print("\nLemmatization:")
for word in words:
    print(f"{word} -> {lemmatizer.lemmatize(word, pos='v')}")


# Output:


# Stemming:
# playing -> play
# played -> play
# plays -> play
# better -> better
# running -> run
# studies -> studi

# Lemmatization:
# playing -> play
# played -> play
# plays -> play
# better -> better
# running -> run
# studies -> study


# Notice that **stemming** may produce a non-real word like `studi`, while **lemmatization** returns the correct dictionary word `study`.
