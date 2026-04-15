from collections import defaultdict, Counter

data = [
    [("the", "DET"), ("market", "NOUN"), ("is", "VERB"), ("rising", "VERB")],
    [("stocks", "NOUN"), ("are", "VERB"), ("falling", "VERB")],
    [("the", "DET"), ("sun", "NOUN"), ("is", "VERB"), ("bright", "ADJ")],
    [("market", "NOUN"), ("is", "VERB"), ("volatile", "ADJ")]
]

train = data[:3]
test = data[3:]

trans = defaultdict(Counter)
emit = defaultdict(Counter)

for sent in train:
    prev = "<s>"
    for word, tag in sent:
        word = word.lower()
        trans[prev][tag] += 1
        emit[tag][word] += 1
        prev = tag

def hmm_tag(sentence):
    result = []
    for word in sentence:
        word = word.lower()
        best_tag = max(emit, key=lambda t: emit[t][word])
        result.append(best_tag)
    return result

correct = total = 0
for sent in test:
    words = [w for w, t in sent]
    true_tags = [t for w, t in sent]
    pred_tags = hmm_tag(words)

    for p, t in zip(pred_tags, true_tags):
        if p == t:
            correct += 1
        total += 1

hmm_acc = correct / total if total > 0 else 0
print("HMM Accuracy:", hmm_acc)

def features(word):
    return {
        "word": word.lower(),
        "suffix": word[-2:].lower()
    }

feature_tag_counts = defaultdict(Counter)

for sent in train:
    for word, tag in sent:
        f = features(word)
        key = (f["word"], f["suffix"])
        feature_tag_counts[key][tag] += 1

def predict(word):
    f = features(word)
    key = (f["word"], f["suffix"])
    
    if key in feature_tag_counts:
        return feature_tag_counts[key].most_common(1)[0][0]
 
    if word.endswith("ing"):
        return "VERB"
    elif word.endswith("ly"):
        return "ADV"
    else:
        return "NOUN"

correct = total = 0

for sent in test:
    for word, true_tag in sent:
        pred = predict(word)
        if pred == true_tag:
            correct += 1
        total += 1

log_acc = correct / total if total > 0 else 0
print("Log-Linear Accuracy:", log_acc)
