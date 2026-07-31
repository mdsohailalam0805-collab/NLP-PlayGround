# Stemming and Lemmatization

## What is Stemming?

Stemming is the process of reducing a word to its root form by removing prefixes or suffixes.

Examples:

* playing → play
* played → play
* plays → play

Stemming is **fast**, but the result may not always be a real English word.



## What is Lemmatization?

Lemmatization is the process of converting a word into its correct dictionary form (called a **lemma**).

Examples:

* better → good
* running → run
* studies → study

Lemmatization is **more accurate** than stemming, but it is slightly slower.



## Difference Between Stemming and Lemmatization

| Stemming                   | Lemmatization                  |
| -------------------------- | ------------------------------ |
| Faster                     | More accurate                  |
| May produce non-real words | Produces real dictionary words |
| Uses simple rules          | Uses vocabulary and grammar    |



## When to Use?

* Use **Stemming** when speed is important.
* Use **Lemmatization** when accuracy is important.

## Summary

* Stemming removes word endings.
* Lemmatization finds the correct base word.
* Both methods help reduce different forms of a word and improve NLP models.
