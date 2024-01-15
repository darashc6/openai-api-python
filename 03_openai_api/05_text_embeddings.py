from openai import OpenAI
from dotenv import load_dotenv
import numpy as np
import pandas as pd

load_dotenv()

client = OpenAI()

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Embedding -> Vector list of floating point numbers. The distance between 2 vectors measure the relatedness. Small distance suggest high relatedness. Big distance suggest low relatedness.
# Text embeddings measure the relatedness of text strings.

# 'Create Embeddings' API
# https://platform.openai.com/docs/api-reference/embeddings/create
# Required parameters:
# model -> The ID of the model to use. Only 'text-embedding-ada-002' is currently available.
# input -> The input text to embed. Can be a single text, or an array
# 
# Other parameters:
# encoding_format -> Format to return the embeddings. Can be a 'float' or 'base64'. Default is 'float' 
def get_embedding(input, model='text-embedding-ada-002', encoding_format='float'):
    text = input.replace('\n', ' ') # Recommended according to OpenAI documentation. To improve performance.

    response = client.embeddings.create(
        model=model,
        input=text,
        encoding_format=encoding_format
    )

    return response.data[0].embedding

# Returns a list of 'embeddings' objects (Vector list)
print(get_embedding("red"))


# Finding similarities using Embeddings
# Using the 'words.csv' file, we can categorize the words into 'food or drinks', 'animals', 'coloura'
# For this example, we will use the 'numpy' and 'pandas' library

# Reading CSV into a dataframe
# DataFrame -> 2-dimensional size data structure. Similar to a table with rows and columns, or a 2 dimensional array
df = pd.read_csv('words.csv')

# Next, in the DataFrame, we will create a new column called 'embedding'. This column will contain the embeddings for each word in the 'words.csv' file.
# We will use the 'apply()' method to apply the 'get_embeddings' function to each row of the 'text' column.
df['embedding'] = df['text'].apply(lambda x: get_embedding(x))

# Storing the embeddings locally
df.to_csv('words-embeddings.csv', index=False)
print("CSV file saved in 'words-embeddings.csv'")

# Perform semantic searches using Embeddings
df = pd.read_csv('words-embeddings.csv')

# When reading the file from CSV, the 'text' and 'embedding' values are read as a string
# To perform operations using Embeddings, we must convert the 'embedding' values to an array
# We use the 'numpy' library to convert the values to an array
df['embedding'] = df['embedding'].apply(eval).apply(np.array)

# Proceeding with the semantic search
search_term = 'purple'
search_term_vector = get_embedding(search_term)

# To compare the similarity between 2 words, we will implement the 'Cosine Similarity' Algorithm
# Wikipedia: https://en.wikipedia.org/wiki/Cosine_similarity
# Function to calculate the cosine similarity -> See 'cosine_similarity' function in Line 10
# We're adding a new column 'similarities', to apply the cosine similarity for each row
df['similarities'] = df['embedding'].apply(lambda x: cosine_similarity(x, search_term_vector))

# To see which words are most similar, we will sort the 'similarities' column in descending order
df = df.sort_values('similarities', ascending=False)
print(df)