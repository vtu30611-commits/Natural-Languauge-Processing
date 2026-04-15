
text = """Natural language processing enables computers to understand human language.
It is a key area of artificial intelligence."""

import string
tokens = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

vocab = sorted(set(tokens))

word_map = {}

for i in range(len(tokens) - 1):
    word = tokens[i]
    next_word = tokens[i + 1]
    
    if word not in word_map:
        word_map[word] = []
    
    word_map[word].append(next_word)


import random

def generate_text(seed_text, next_words):
    words = seed_text.lower().split()
    
    for _ in range(next_words):
        last_word = words[-1]
        
        if last_word in word_map:
            next_word = random.choice(word_map[last_word])
        else:
            next_word = random.choice(vocab)
        
        words.append(next_word)
    
    return " ".join(words)

print("Generated Text:")
print(generate_text("natural language", 5))
