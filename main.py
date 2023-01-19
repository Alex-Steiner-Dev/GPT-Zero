import os

# Get Input
print("Inputer your text: ", end="")
sentence = input()

# Tokenize the sentence
def tokenize(sentence):
    return sentence.split()

cross_entropy = 0

# Get tokenize sentence
sentence = tokenize(sentence)

print(sentence)