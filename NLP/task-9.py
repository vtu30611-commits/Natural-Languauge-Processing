
sentences = [["I", "love", "NLP"], ["NLP", "is", "fun"]]
tags = [["PRP", "VBP", "NN"], ["NN", "VBZ", "JJ"]]

from collections import defaultdict, Counter

word_tag_map = defaultdict(Counter)

for sent, tag_seq in zip(sentences, tags):
    for word, tag in zip(sent, tag_seq):
        word_tag_map[word.lower()][tag] += 1

def predict(sentence):
    result = []
    
    for word in sentence:
        word_lower = word.lower()
        
        if word_lower in word_tag_map:
            
            tag = word_tag_map[word_lower].most_common(1)[0][0]
        else:
           
            if word_lower.endswith("ing"):
                tag = "VBG"
            elif word_lower.endswith("ed"):
                tag = "VBD"
            else:
                tag = "NN"
        
        result.append(tag)
    
    return result

test = ["I", "love", "NLP"]

print("Prediction:")
print(predict(test))
