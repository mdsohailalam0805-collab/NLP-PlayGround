# Feature Extraction

## What is Feature Extraction?
Feature Extraction is the process of converting text into numerical values that a machine learning model can understand.
Computers cannot work directly with text, so we convert words into numbers.

## Why do we use Feature Extraction?
<!-- key points :- -->
* Convert text into numbers
* Prepare data for machine learning models
* Improve text classification and prediction tasks

## Common Feature Extraction Methods

### One-Hot Encoding
One-Hot Encoding represents each word as a binary vector (0 or 1).

**Example**

Words:

```text
I, love, NLP
```

Representation:

| Word | I | love | NLP |
| ---- | - | ---- | --- |
| I    | 1 | 0    | 0   |
| love | 0 | 1    | 0   |
| NLP  | 0 | 0    | 1   |


**Advantages**
* Simple and easy to understand
* Works well for small vocabularies

**Disadvantages**
* Creates very large vectors
* Does not capture word meaning or context

### Bag of Words (BoW)
Bag of Words counts how many times each word appears in a sentence.

**Example**
Sentences:

```text
I love NLP
I love Python
```

BoW representation:

| Sentence      | I | love | NLP | Python |
| ------------- | - | ---- | --- | ------ |
| I love NLP    | 1 | 1    | 1   | 0      |
| I love Python | 1 | 1    | 0   | 1      |

**Advantages**
* Simple and fast
* Good for basic text classification

**Disadvantages**
* Ignores word order
* Does not understand context

### TF-IDF
TF-IDF (Term Frequency–Inverse Document Frequency) gives higher weight to important words and lower weight to common words.

**Example**

Sentences:

```text
I love NLP
I love Python
NLP is amazing
```

TF-IDF representation (example values):

| Sentence       | I    | love | NLP  | Python | is   | amazing |
| -------------- | ---- | ---- | ---- | ------ | ---- | ------- |
| I love NLP     | 0.58 | 0.58 | 0.58 | 0.00   | 0.00 | 0.00    |
| I love Python  | 0.58 | 0.58 | 0.00 | 0.58   | 0.00 | 0.00    |
| NLP is amazing | 0.00 | 0.00 | 0.47 | 0.00   | 0.62 | 0.62    |

**Explanation**
* **I** and **love** appear in multiple sentences, so they get lower weights.
* **Python** appears in only one sentence, so it gets a higher weight.
* **amazing** appears in only one sentence, so it also gets a higher weight.

**Advantages**
* Highlights important words
* Reduces the effect of common words

**Disadvantages**
* Ignores word order
* More complex than Bag of Words

## Summary

| Method           | Main Idea                             |
| ---------------- | ------------------------------------- |
| One-Hot Encoding | Binary representation (0 or 1)        |
| Bag of Words     | Counts word frequency                 |
| TF-IDF           | Gives importance to informative words |

Feature Extraction is an important NLP step because machine learning models require numerical input instead of raw text.
