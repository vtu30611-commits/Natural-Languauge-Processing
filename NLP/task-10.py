
sentences = [["Welcome", "to", "our", "site"], ["This", "product", "is", "great"]]
chunks = [["H", "H", "H", "H"], ["P", "P", "P", "P"]]  

from collections import defaultdict, Counter


word_chunk_map = defaultdict(Counter)

for sent, chunk_seq in zip(sentences, chunks):
    for word, label in zip(sent, chunk_seq):
        word_chunk_map[word.lower()][label] += 1

def predict(sentence):
    result = []
    
    for word in sentence:
        word_lower = word.lower()
        
        if word_lower in word_chunk_map:
           
            label = word_chunk_map[word_lower].most_common(1)[0][0]
        else:
            
            if word_lower in {"welcome", "our"}:
                label = "H"
            else:
                label = "P"
        
        result.append(label)
    
    return result


test = ["Welcome", "product"]

print("Predicted Chunks:")
print(predict(test))
