from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load .env variable

client = OpenAI()

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


emotions = "Positive, Negative"
emotions = "Happy, Sad, Angry, Fearful, Tired, Disgust, Surprise, Neutral"

user_prompt = input("Enter your prompt (Leave empty to exit): ")

while user_prompt != '':
    emotion = gpt_classify_sentiment(user_prompt, emotions)
    print(emotion)
    user_prompt = input("Enter your prompt (Leave empty to exit): ")

review = '''
Super explanation with all the important things you have to know in Python.
The course has a lot of examples and exercises.
Part 2 contains a lot of Python projects and shows you how to use Python in real-world scenarios.
'''
emotion = gpt_classify_sentiment(review, emotions)
print(f'{review[:50]} ... ======> {emotion.upper()}')

review = '''
This wasn't a good match for me and doesn't fit my learning style.
'''
emotion = gpt_classify_sentiment(review, emotions)
print(f'{review[:50]} ... ======> {emotion.upper()}') 