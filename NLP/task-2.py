
text = "Natural Language Processing is an exciting field of Artificial Intelligence."


import string
tokens = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

print("Basic Tokens:")
print(tokens)

stop_words = {
    "is", "an", "a", "the", "of", "and", "in", "to", "for", "on", "with"
}

filtered_tokens = [word for word in tokens if word not in stop_words]

print("\nTokens (Stopwords Removed):")
print(filtered_tokens)

def fake_transformer_tokenizer(word):
    if len(word) > 6:
        return [word[:4], "##" + word[4:]]
    return [word]

transformer_tokens = []
for word in tokens:
    transformer_tokens.extend(fake_transformer_tokenizer(word))

print("\nSimulated Transformers Tokens:")
print(transformer_tokens)


filtered_spacy = [word for word in tokens if word not in stop_words]

print("\nSimulated spaCy Tokens (Stopwords Removed):")
print(filtered_spacy)
