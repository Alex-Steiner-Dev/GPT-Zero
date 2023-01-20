import nltk
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE

from perplexity import * 

text = '''
Gravity is a fundamental force of nature that describes the interaction between objects with mass. It is the force that causes objects to be attracted to one another. The strength of the gravitational force between two objects is proportional to the mass of the objects and inversely proportional to the square of the distance between them. This is encapsulated in Newton's law of universal gravitation. The force of gravity is what holds us to the ground, and what keeps the planets in orbit around the sun.
'''

get_perplexity(text)