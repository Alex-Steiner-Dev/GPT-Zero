from perplexity import *
from nltk.tokenize import sent_tokenize 

from itertools import zip_longest
from typing import List


def evaluate(text):
    print("Evaluating the text given...")

    paragraphs = grouper(sent_tokenize(text), 9)
    results = []

    print(len(paragraphs))

    for i in range(len(paragraphs)):
        txt = ""
        for j in paragraphs[i]:
            txt+= str(j)

        print(j)
        get_perplexity(txt)
        results.append(return_msg())

        print(results[i])
    
    return results[0]

def grouper(iterable: List, n: int, fillvalue=None) -> List:
    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))