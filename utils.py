import openai

<<<<<<< HEAD
openai.api_key = "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"
model_engine = "text-davinci-003"
=======
openai.api_key = "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"
model_engine = "text-davinci-002"
>>>>>>> parent of 53eee72 (Updates)


# Get the text input from the js server
def get_answer(prompt): 
    prompt = prompt + " could you write a text about this using 10000 words, do not copy it?"

    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2000, n=1,stop=None,temperature=0.5)

    response = completions.choices[0].text
    
    return response
