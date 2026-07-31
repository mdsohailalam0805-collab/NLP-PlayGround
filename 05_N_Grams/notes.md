# N-Grams

## What are N-Grams?

N-Grams are groups of **N consecutive words** in a sentence.

The value of **N** decides how many words are grouped together.

## Why do we use N-Grams?

* Capture word order
* Understand context better
* Improve text classification and language models

## Types of N-Grams

### Unigram (1 word)

Sentence:

```text
I love NLP
```

Output:

```text
['I', 'love', 'NLP']
```

### Bigram (2 words)

Sentence:

```text
I love NLP
```

Output:

```text
['I love', 'love NLP']
```

### Trigram (3 words)

Sentence:

```text
I love learning NLP
```

Output:

```text
['I love learning', 'love learning NLP']
```

## Advantages

* Captures nearby word relationships
* Better than single words for many NLP tasks
* Useful in text prediction and classification

## Summary

* **Unigram** → 1 word
* **Bigram** → 2 words
* **Trigram** → 3 words
* N-Grams help preserve word order and context.
