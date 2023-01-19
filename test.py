import openai

# Replace YOUR_API_KEY with your own OpenAI API key
openai.api_key = "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"

# Define a function to calculate perplexity
def perplexity(sentence):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"perplexity of the following sentence: {sentence}",
    )
    perplexity = (response.choices[0].text.strip())
    return perplexity

# Human-written text
human_text = "Dogs are loyal and loving companions that are known for their ability to form strong bonds with their human owners."

# AI-written text
ai_text = "The dog is a mammal of the order Carnivora. It is a domesticated form of the gray wolf and is the most widely abundant wild mammal."

# Text to be evaluated
text_to_evaluate = "Dogs are nice"

# Calculate perplexity of the human-written text
human_perplexity = perplexity(human_text)

# Calculate perplexity of the AI-written text
ai_perplexity = perplexity(ai_text)

# Calculate perplexity of the text to be evaluated
text_to_evaluate_perplexity = perplexity(text_to_evaluate)

# Compare the perplexity of the text to be evaluated with the human-written and AI-written text
if text_to_evaluate_perplexity < min(human_perplexity, ai_perplexity):
    print("The text is likely to be written by a human")
else:
    print("The text is likely to be written by an AI")