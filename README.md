# NLP Playground

This repository contains my NLP (Natural Language Processing) learning journey.
I am learning NLP step by step through simple notes and hands-on projects.

## Topics

* NLP introduction
* Text Preprocessing
* Tokenization
* Stopwords Removal
* Stemming and Lemmatization
* Bag of Words (BoW)
* TF-IDF
* Emotion Detection Project

Each topic contains:

* Easy English notes
* Python code examples
* Small practice examples
* A simple explanation of why each step is used

The goal of this repository is to build a complete beginner-friendly NLP notebook that I can revise anytime.



# Introduction to NLP

Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that helps computers understand, process, and generate human language.

In simple words, NLP allows a computer to work with text and speech just like humans do.

## Examples of NLP

* Google Translate
* ChatGPT
* Grammarly
* Email spam detection
* Sentiment analysis
* Voice assistants such as Siri and Alexa

## Why is NLP important?

Most information on the internet is in the form of text. NLP helps machines analyze text, find useful information, classify documents, answer questions, and understand human emotions.

## Basic NLP Workflow

1. Load the dataset
2. Clean the text
3. Tokenization
4. Remove stopwords
5. Stemming or Lemmatization
6. Convert text into numbers (Bag of Words or TF-IDF)
7. Train a machine learning model
8. Make predictions

This repository contains my NLP learning journey with simple notes, Python examples, and small projects.



# Text Preprocessing

## What is Text Preprocessing?

Text preprocessing is the first step in most NLP projects. It is the process of cleaning and preparing text before giving it to a machine learning model.

Real-world text often contains capital letters, punctuation, numbers, emojis, URLs, and other unwanted characters. A model cannot learn well from messy text, so we clean it first.

## Why do we use Text Preprocessing?

* Remove unnecessary information
* Make text easy to understand
* Improve model accuracy
* Reduce noise in the dataset

## Example

Original text:

```
I LOVE NLP!!! Visit https://example.com 😊
```

After preprocessing:

```
i love nlp visit
```

## Common Text Preprocessing Steps

1. Convert text to lowercase
2. Remove punctuation
3. Remove numbers
4. Remove URLs
5. Remove HTML tags
6. Remove emojis
7. Remove stopwords
8. Perform stemming or lemmatization

## Python Example

```python
text = "I LOVE NLP!!!"
clean_text = text.lower()
print(clean_text)
```

Output:

```
i love nlp!!!
```

## Summary

Text preprocessing prepares raw text for NLP tasks. It removes unnecessary characters and makes the text clean and consistent, which helps machine learning models perform better.




# Tokenization

## What is Tokenization?

Tokenization is the process of breaking text into small parts called **tokens**. A token can be a word, a sentence, or a character.

Example:

```text
I love NLP
```

Output:

```text
['I', 'love', 'NLP']
```

## Why do we use Tokenization?

* Computers cannot understand full sentences directly.
* It helps process text word by word.
* It is the first major step in most NLP tasks.

## Types of Tokenization

### Word Tokenization

```text
I love NLP
```

Output:

```text
['I', 'love', 'NLP']
```

### Sentence Tokenization

```text
I love NLP. It is interesting.
```

Output:

```text
['I love NLP', 'It is interesting']
```

## Python Example

```python
text = "I love NLP"
tokens = text.split()
print(tokens)
```

Output:

```text
['I', 'love', 'NLP']
```

## NLTK Example

```python
from nltk.tokenize import word_tokenize

tokens = word_tokenize("I love NLP!")
print(tokens)
```

Output:

```text
['I', 'love', 'NLP', '!']
```

## Summary

* Tokenization breaks text into tokens.
* It is the first practical step in NLP.
* Other techniques such as stopwords removal, stemming, and TF-IDF use tokens as input.



