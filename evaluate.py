from perplexity import * 
from itertools import zip_longest
from typing import List
from nltk.tokenize import sent_tokenize

def evaluate(text):
    print("Evaluating the text given...")

    paragraphs = grouper(sent_tokenize(text), 5)
    results = []

    print(len(paragraphs))

    for i in range(len(paragraphs)):
        txt = ""
        for j in range(len(paragraphs[i])):
            txt += str(j)

        get_perplexity(txt)
        results.append(return_msg())

        print(results[i])

    return return_msg()

def grouper(iterable: List, n: int, fillvalue=None) -> List:
    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))