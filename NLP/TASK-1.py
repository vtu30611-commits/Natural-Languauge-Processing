
text = "Natural Language Processing is a part of Artificial Intelligence."


import string

tokens = text.translate(str.maketrans('', '', string.punctuation)).split()
print("Tokens:", tokens)

stop_words = {"is", "a", "of", "the", "and", "in", "to"}

filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:", filtered_tokens)

def simple_pos(word):
    if word.lower() in {"is", "am", "are", "was", "were"}:
        return "VERB"
    elif word[0].isupper():
        return "NOUN (Proper)"
    elif word.endswith("ing"):
        return "VERB (Gerund)"
    else:
        return "NOUN"

pos_tags = [(word, simple_pos(word)) for word in tokens]
print("POS Tags:", pos_tags)

print("\nTokens and POS Tags:")
for word, tag in pos_tags:
    print(word, "->", tag)
