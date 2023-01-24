from perplexity import * 

def evaluate(text):
    print("Evaluating the text given...")
<<<<<<< HEAD

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
=======
    get_perplexity(text)
>>>>>>> parent of 53eee72 (Updates)
    
    return return_msg()