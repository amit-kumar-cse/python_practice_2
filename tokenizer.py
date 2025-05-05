import tiktoken

#tiktoken library works for open Ai model only

model = "gpt-4o"
encoding = tiktoken.encoding_for_model(model)

def tokenize_with_tiktoken(input_text, encoding=encoding):
    # Tokenize the input
    tokens = encoding.encode(input_text)
    
    return tokens


# reverse the tokenization
def detokenize_with_tiktoken(tokens, model=model):
    return encoding.decode(tokens)

# Example usage
text = "Hello Amit, how are you?"
print("Text:", text)
tokens = tokenize_with_tiktoken(text)
print("Token IDs:", tokens)
print("Number of tokens:", len(tokens)) 

# detokenize the tokens
detokenized_text = detokenize_with_tiktoken(tokens)
print("Detokenized text:", detokenized_text)


# print the number of token in the model
print("Number of tokens in the model:", encoding.n_vocab)