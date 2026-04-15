
text = "The boys are playing games and running faster than before."

import string
tokens = text.lower().translate(str.maketrans('', '', string.punctuation)).split()


def simple_stem(word):
    if word.endswith("ing"):
        return word[:-3]
    elif word.endswith("ed"):
        return word[:-2]
    elif word.endswith("s") and len(word) > 3:
        return word[:-1]
    return word

stemmed_words = [simple_stem(word) for word in tokens]

print("Stemming Output:")
for word, stem in zip(tokens, stemmed_words):
    print(f"{word} -> {stem}")

def simple_pos(word):
    if word in {"is", "are", "was", "were"}:
        return "VERB"
    elif word.endswith("ing"):
        return "VERB (Gerund)"
    elif word.endswith("er"):
        return "ADJECTIVE (Comparative)"
    elif word.endswith("s"):
        return "NOUN (Plural)"
    else:
        return "NOUN"

def simple_lemma(word):
    return simple_stem(word)

print("\nMorphological Analysis:")
for word in tokens:
    print(f"Word: {word}")
    print(f" Lemma: {simple_lemma(word)}")
    print(f" POS: {simple_pos(word)}")
    print(f" Morphology: rule-based")
    print()
