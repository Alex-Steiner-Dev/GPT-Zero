import os
from utils import *

# Get Input
print("Inputer your text: ", end="")
sentence = input()

cross_entropy = 0

# Get tokenize sentence
sentence = tokenize_sentence(sentence)

print(sentence)