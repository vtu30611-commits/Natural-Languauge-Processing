
text = """Natural language processing is a field of artificial intelligence.
It enables computers to understand human language."""

import string
tokens = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append((tokens[i], tokens[i + 1]))

print("Generated Bigrams:")
print(bigrams)

from collections import defaultdict
import random

model = defaultdict(list)
for w1, w2 in bigrams:
    model[w1].append(w2)

def generate_text(seed, num_words):
    current_word = seed.lower()
    output = [current_word]

    for _ in range(num_words):
        next_words = model.get(current_word)
        if not next_words:
            break
        
        next_word = random.choice(next_words)
        output.append(next_word)
        current_word = next_word

    return " ".join(output)

print("\nGenerated Text:")
print(generate_text("natural", 8))

print("\nTokens:")
print(tokens)
