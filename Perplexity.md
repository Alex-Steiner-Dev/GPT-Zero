sentence = "The cat sat on the mat."

# Tokenize the sentence
words = tokenize(sentence)

# Initialize variable to store the cross-entropy
cross_entropy = 0

# Iterate through each word in the sentence
for i in range(len(words)):
    # Use the language model to calculate the probability of the current word given the previous words
    probability = language_model(words[i], words[:i])
    # Add the log2 of the probability to the cross-entropy
    cross_entropy += log2(probability)

# Negate the cross-entropy
cross_entropy = -cross_entropy

# Calculate perplexity by taking 2 to the power of the cross-entropy
perplexity = pow(2, cross_entropy)
