from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load .env variables

client = OpenAI()

# Given a list of messages containing a conversation between the user and the assistant, returns the response
def get_response(list_messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=list_messages,
        temperature=0.5
    )
    return response.choices[0].message.content

messages = list()

# Define the system role
# This is an optional input. The user can simply skip it if they don't want to define it
# If not defined, a default role will be assigned -> 'You are a helpful assistant.'
system_role = input("(Optional) Define the system role of the your chat bot: ")
if system_role:
    messages.append({"role": "system", "content": system_role})
else:
    messages.append({"role": "system", "content": "You are a helpful assistant."})

# Start the conversation
# The user will be able to ask questions until they enter an empty string
# Once they enter an empty string, the conversation will end
while True:
    user_prompt = input("Me: ") # Enter a question/message. If they enter an empty string, the conversation will end
    if user_prompt == '':
        print("Chat Bot: Thank you for your time! See you soon!")
        break
    
    messages.append({"role": "user", "content": user_prompt}) # Append the user message to the list
    response = get_response(messages) # Return the response of said input
    messages.append({"role": "assistant", "content": response}) # Append the assistant response to the list
    print("Chat Bot:", response)
    print('-' * 50)
    

