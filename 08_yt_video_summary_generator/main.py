from openai import OpenAI
from dotenv import load_dotenv
from pytube import YouTube
import tiktoken

load_dotenv() # Load .env variables

# Project 4 -> YouTube Video Summary Generator given a YouTube link
# This script will be divided into 3 separate tasks
# Task 1 -> Given a YouTube link, download the audio stream. This can be done using the 'pytube' library
# Task 2 -> With the audio stream from Step 1, convert it to text using the OpenAI's Audio API
# Task 3 -> With the text from Step 2, generate a summary using the Chat Completion API

client = OpenAI()

# Generates a text transcription from an audio file, using the OpenAI's Audio API
def generate_text_transcription(audio_file, is_english=True):
    print("Generating text transcription...")

    if is_english:
        response = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    else:
        response = client.audio.translations.create(
            model="whisper-1",
            file=audio_file
        )

    print("Completed!")

    return response.text


# Returns the number of tokens in a text string
def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


# Generates a summary using the Chat Completion API, given a text transcription
def yt_video_summary_generator(text_transcription):
    print("Generating summary...")
    model = "gpt-3.5-turbo"
    instructions = f'''
        Generate a summary of the following text transcription taken from a YouTube video:
        {text_transcription}

        Your answer should include the following information:
        - A title of the summary, covering the main topic of the YouTube video.
        - Introduction: Covering the main topic of the video 
        - The different topics of the summary. This should be divided in bullet points. Depending on how lengthy the video/text transcription is, you can include from 5 to 10 bullet points. Also give a very brief explanation for each point.
        - The conclusion of the summary.
    '''

    num_tokens = num_tokens_from_string(instructions, model)

    # If num_tokens is within the model's limit, it generates a summary
    if num_tokens <= 4096:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": 'You are an expert YouTube video summarizer.'},
                {"role": "user", "content": instructions},
            ],
            n=1
        )
        print("Completed!")

        return response.choices[0].message.content
    
    print("Failed")
    return "No summary generated because the text transcription is too long. Please select a shorter video for summary generation."

# Example link (English): https://www.youtube.com/watch?v=I0uCIbhjYvg
# Example link (Spanish): https://www.youtube.com/watch?v=0qWErfwTtAk

# Enter the link of the youtube video which we would like to summarize
youtube_link = input("Enter the link of the YouTube video you want to download and summarize: ")

is_english = input("Is the video in English? (y/n): ")
if is_english.lower() == 'y':
    is_english = True
else:
    is_english = False

if not youtube_link:
    print("YouTube link not provided")
elif 'youtube.com' not in youtube_link:
    print("Invalid YouTube link")
else:
    # Step 1
    print("Audio stream downloading...")
    yt = YouTube(youtube_link) # Inserting the YouTube link to a 'YouTube' object
    yt.streams.filter(only_audio=True).first().download(filename="audio.mp3") # Downloading the audio stream from the YouTube video
    print("Completed!")

    # Step 2
    audio_file = open("audio.mp3", "rb")
    text_transcription = generate_text_transcription(audio_file, is_english)

    # Step 3
    text_summary = yt_video_summary_generator(text_transcription)
    print("Summary of the video:")
    print(text_summary)