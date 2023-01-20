from utils import *

def get_perplexity(text):
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
        n = float(model.perplexity(test))

        print("Perplexity: {0}".format(n))
        print(type(n))

        try:
            if n != float('inf'):
                break
            else:
                get_perplexity(text)
        except:
            get_perplexity(text)