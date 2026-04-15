from collections import defaultdict, Counter

data = [
    [("the", "DET"), ("market", "NOUN"), ("is", "VERB"), ("rising", "VERB")],
    [("the", "DET"), ("sun", "NOUN"), ("is", "VERB"), ("bright", "ADJ")],
    [("stocks", "NOUN"), ("are", "VERB"), ("rising", "VERB")],
    [("market", "NOUN"), ("is", "VERB"), ("volatile", "ADJ")]
]

trans = defaultdict(Counter)
emit = defaultdict(Counter)

for sent in data:
    prev = "<s>"
    for word, tag in sent:
        trans[prev][tag] += 1
        emit[tag][word] += 1
        prev = tag
        
def tag_sentence(sentence):
    result = []
    for word in sentence:
        word_lower = word.lower()
        
       
        best_tag = max(emit, key=lambda t: emit[t][word_lower])
        
        result.append((word, best_tag))
    
    return result


sentence = ["The", "market", "is", "rising"]

print("Tagged Sentence:")
print(tag_sentence(sentence))
