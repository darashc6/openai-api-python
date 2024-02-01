from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv() # Load .env variables

# Project 2 -> Create a ChatGPT clone (OpenAI API and Streamlit)

client = OpenAI()

# Given a list of messages containing a conversation between the user and the assistant, returns the response.
def get_response(list_messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=list_messages,
        temperature=0.5
    )
    return response.choices[0].message.content

# Returns a list of messages containing a conversation between the user and the assistant.
# Formatted to display it in a Sidebar
def show_conversation():
    for message in messages:
        if message["role"] == "user":
            st.write(f"User: {message['content']}")
        
        if message["role"] == "assistant":
            st.write(f"Assistant: {message['content']}")


# Session state initialization
messages = list()

if 'messages' not in st.session_state:
    st.session_state.messages = list()

if 'messages' in st.session_state:
    messages = st.session_state.messages

# Building the Chat form
col_spacing_start, col1, col_spacing_end = st.columns([0.4, 0.5, 0.4])

with col1:
    st.header("Chat GPT Clone")

with st.form("chat_form"):
    system_role_input = st.text_input("System role:", value="You are a helpful assistant", key="system_role")

    user_input = st.text_area("Enter your message:", key="user_input")

    button_col1, spacing, button_col2 = st.columns([2, 7, 2])

    with button_col1:
        submit = st.form_submit_button("Submit", type="secondary")
    
    with button_col2:
        clear_history = st.form_submit_button("Clear history", type="primary", help="Clears the chat history")

    # Submit button
    if submit:
        if not system_role_input: # If 'System role' input is empty
            st.error("Error - System role cannot be empty", icon="🚨")
        elif not user_input: # If message input is empty
            st.error("Error - Message cannot be empty", icon="🚨")
        else:
            # Valid inputs

            # Check if the list of messages already has the 'system' role defined
            # If not, add the role to the list
            system_role_in_list = any(message["role"] == 'system' for message in messages)

            if not system_role_in_list:
                messages.append({"role": "system", "content": system_role_input})

            messages.append({"role": "user", "content": user_input})
            response = get_response(messages)
            messages.append({"role": "assistant", "content": response})

            st.session_state.messages = messages
    
    # Clear history button
    if clear_history:
        messages = list()
        st.session_state.messages = messages

# Sidebar, containg the chat conversation
with st.sidebar:
    st.header("Chat history")
    show_conversation()