import nltk
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from nltk import FreqDist

def get_burtiness(text):
    tokens = nltk.word_tokenize(text)

    fdist = FreqDist(tokens)

    mean = sum(fdist.values())/len(fdist)
    std_dev = (sum((val - mean)**2 for val in fdist.values())/len(fdist))**0.5

    cv = std_dev / mean

    return cv
