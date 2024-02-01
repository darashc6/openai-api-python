from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv() # Load .env variables

# Project 1 -> Creating a Zero-Shot Sentiment Analysis using ChatGPT & Streamlit

client = OpenAI()

# Function that classifies input prompt by user into different emotions, which is also specified by the user
def gpt_classify_sentiment(prompt, emotions):
    model = "gpt-3.5-turbo"
    system_role = f'''
        You are an emotionally intelligent assistant. 
        Classify the sentiment of the user's text with ONLY ONE OF THE FOLLOWING EMOTIONS: {emotions}.
        After classifying the text, respond with the emotion ONLY.
    '''

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt}
        ],
        max_tokens=20,
        temperature=0
    )

    if completion.choices[0].message.content == '':
        return 'N/A'
    
    return completion.choices[0].message.content

# Displays the list of the prompt inputs by the user
def show_history(history):
    for item in history:
        st.write(item)


# Session state initialization
history = [];
if 'history' not in st.session_state:
    st.session_state.history = history

if 'history' in st.session_state:
    history = st.session_state.history

st.markdown("<h1 style='text-align: center;'>Zero-Shot Sentiment Analysis</h1>", unsafe_allow_html=True)

# Working with Streamlit Forms
# https://docs.streamlit.io/library/advanced-features/forms
with st.form(key='my_form', clear_on_submit=True):
    default_emotions = "Positive, Negative, Neutral"
    emotions = st.text_input('Emotions', default_emotions)

    text = st.text_area(label='Text to classify', key='text')

    submit_button = st.form_submit_button(label='Check')

    st.divider()

    if submit_button:
        emotion = gpt_classify_sentiment(text, emotions)
        result = f'{text} => {emotion}'
        history.insert(0, result)

        st.session_state.history = history
    
    show_history(history)
