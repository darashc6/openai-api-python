# Library to interact with OpenAI's API
# https://github.com/openai/openai-python
# pip install openai
from openai import OpenAI
# Library to load environment variables from a .env file. 
# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv() # Load environment variables from a .env file

# Create an instance of the OpenAI class
# To take the API key from an environment variable, we can specify it as an argument 'api_key '-> os.getenv("OPENAI_API_KEY")
client = OpenAI()

# 'Chat Completion' API
# https://platform.openai.com/docs/api-reference/chat/create
# Required parameters:
# model -> Specify the model to use. To check which model is compatoble, visit 'https://platform.openai.com/docs/models/model-endpoint-compatibility'
# messages -> List of message objects representing the conversation Each message object must contain a 'role' and 'content' property. The 'role' property must be one of 'system', 'user', or 'assistant'. 'content' is the actual text of the message.

# Other parameters:
# temperature -> Sets the degree of randomness of the model's output. Accepts values between 0 and 2. Higher values result in more random output. Lower values result will make the responses more focused deterministic. Default is 1. Also check the 'seed' parameter for another way of setting the randomness of the model
# response_format -> Object specifying the response format. Must be 'text' or 'json_object' (Ex: { "type": "json_object" }). IMPORTANT: If we want to return the response in JSON format, we MUST instruct the model to return the response in JSON format. This can be done specifying in the 'messages' parameter.
# stream -> Control how the model delivers the message. If set to 'True', the model will print the response in chunkes, like it currently does in the ChatGPT app.
# n -> Number of messages to generate. Default is 1 to reduce costs.

# Example 1 -> Asking a question, and returning the response as 'text'
completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who has the most Premier League titles from 2010 onwards?"},
    ],
    temperature=0.6,
    n=2
)

# Returns a 'ChatCompletion' object
# Includes fields such as 'id', the model used, date created of the conversation, and 'choices' which contains a list of 'Message' objects
# Messages -> 'completion.choices[x].message.content'
print("'ChatCompletion' object: ", completion)
print("\nModel Responses:")
for choice in completion.choices:
    print(choice.message.content)

# Example 2 -> Asking a question, and returning the response in JSON format. This is done by telling the model to return the response as a JSON object
# * IMPORTANT: This only works if the model specified is either a 'gpt-4-1106-preview' or a 'gpt-3.5-turbo-1106'
completion_json = client.chat.completions.create(
    model='gpt-3.5-turbo-1106',
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Whatever response you return will be returned in a JSON format"},
        {"role": "user", "content": "Can you tell me all the provinces located in the Andalusian region of Spain? Include the provinces name, coordinates, population and capital city"},
    ],

)

# Printing the JSON response
print("\nModel Response:", completion_json.choices[0].message.content)


# Example 3 -> Asking a question, and returning the response in chunks. This can be done by setting the 'stream' parameter to 'True'
completion_stream = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Name the starting XI for Arsenal for Arsene Wenger's last ever game. Separate each player with a comma. Only name the players. E.g: Petr Cech, Granit Xhaka, ..."},
    ],
    temperature=0,
    seed=123,
    stream=True
)

collected_chunks = []
collected_content = [];

# Printing the chunks of the response
for chunk in completion_stream:
    collected_chunks.append(chunk)
    collected_content.append(chunk.choices[0].delta.content)

print("\nCollected 'Chunks':", collected_chunks)
print("\nCollected content:", collected_content)

# Clean 'collected_content'. Remove None values and join whole list as string
cleaned_content = ''.join(str(e) for e in collected_content if e is not None)
print("\nCleaned content:", cleaned_content)