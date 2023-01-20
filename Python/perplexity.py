from utils import *
import nltk
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE
from utils import *

def get_perplexity():
    # Train the model
    text = '''
    Gravity is a fundamental force of nature that describes the interaction between objects with mass. It is the force that causes objects to be attracted to one another. The strength of the gravitational force between two objects is proportional to the mass of the objects and inversely proportional to the square of the distance between them. This is encapsulated in Newton's law of universal gravitation. The force of gravity is what holds us to the ground, and what keeps the planets in orbit around the sun.
    '''
    train_sentences = [get_answer(text)]

    tokenized_text = [list(map(str.lower, nltk.tokenize.word_tokenize(sent))) 
                    for sent in train_sentences]
    n = 1
    train_data, padded_vocab = padded_everygram_pipeline(n, tokenized_text)
    model = MLE(n)
    model.fit(train_data, padded_vocab)

    test_sentences = ['Gravity is a fundamental force of nature that describes']
    tokenized_text = [list(map(str.lower, nltk.tokenize.word_tokenize(sent))) 
                    for sent in test_sentences]

    test_data, _ = padded_everygram_pipeline(n, tokenized_text)

    for i, test in enumerate(test_data):
        try:
            print("Perplexity: {0}".format((model.perplexity(test))))

            if(model.perplexity(test) < 10):
                get_perplexity()
        except:
            get_perplexity()