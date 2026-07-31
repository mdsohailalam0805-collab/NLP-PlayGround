## Python Example

text = "I LOVE NLP!!!"
clean_text = text.lower()
print(clean_text)



# Output:
# i love nlp!!!




# Text Preprocessing Example

import re
import string

text = "Hello!!! Visit https://example.com 😊 I have 2 cats."


# 1. Convert text to lowercase
text = text.lower()


# 2. Remove punctuation
text = text.translate(str.maketrans("", "", string.punctuation))


# 3. Remove numbers
text = re.sub(r"\d+", "", text)


# 4. Remove URLs
text = re.sub(r"https?://\S+|www\.\S+", "", text)


# 5. Remove HTML tags
text = re.sub(r"<.*?>", "", text)


# 6. Remove emojis
text = re.sub(r"[^\x00-\x7F]+", "", text)


# 7. Remove extra spaces
text = " ".join(text.split())


print(text)


# Output:


# hello visit i have cats


# This example shows the basic text preprocessing steps used before tokenization and other NLP techniques.
