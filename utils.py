import openai
import requests

openai.api_key = "YOUR_OPEN_AI_KEY"
model_engine = "text-davinci-003"

# Get the text input from the js server
def get_answer(prompt): 
    prompt = prompt + " could you write a text about this using 10000 words, do not copy it?"

    completions = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=2000, n=1,stop=None,temperature=0.5)

    response = completions.choices[0].text

    return response
