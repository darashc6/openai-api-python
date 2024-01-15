from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# 'Create Speech' API -> Generates audio from the input text
# https://platform.openai.com/docs/api-reference/audio/createSpeech
# Required parameters:
# model -> The ID of the model to use. The models available for this API are 'tts-1' or 'tts-1-hd'.
# input -> The text to generate audio from. Max length -> 4096 chars
# voice -> The voice to use when generating the audio. Supported voices: 'alloy', 'echo', 'fable', 'onyx', 'nova', and 'shimmer'

# Other parameters:
# response_format -> Format of the audio. Formats supported: 'mp3', 'opus, 'aac' and 'flac'. Default is 'mp3'.
# speed -> The speed of the generated audio. Must be between 0.25 and 4.0. Default is 1.0.

response = client.audio.speech.create(
    model="tts-1-hd",
    input="Nosso sistema solar é composto por oito planetas diversos, desde os mundos internos rochosos como a Terra e Marte até os gigantes gasosos como Júpiter e Saturno, cada um com suas características e luas únicas.",
    voice="nova",
    speed=1.0
)

# The response returns the audio file content. To listen to the audio, we must save the file.
with open("speech.mp3", "wb") as audio_file:
    audio_file.write(response.content)
    print("Audio saved in 'speech.mp3' file")


# 'Create Transcription' API -> Transcribes audio into text
# https://platform.openai.com/docs/api-reference/audio/createTranscription
# Required parameters:
# file -> The audio file to transcribe. Must be a valid audio file (flac, mp3, mp4, mpeg, mpga, m4a, wav, ogg or webm)
# model -> The ID of the model to use. Only 'whisper-1' is currently available
    
# Other parameters:
# language -> The language of the input audio (e.g: 'es', 'en')
# prompt -> Optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language
# response_format -> The format of the transcript output. Supported: 'json', 'text', 'srt', 'verbose_json', and 'vtt'. Default is 'json'
# temperature -> Sampling temperature. Simliar use to the 'Chat Completion API'. Must be between 0 and 1. Default is '0'

audio_file = open("speech.mp3", "rb")
response = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language='pt'
)

# The response returns the transcribed text
print("Text transcribed from 'speech.mp3':",response.text)


# 'Create Translations API' -> Translates audio into english
# https://platform.openai.com/docs/api-reference/audio/createTranslation
# Required parameters:
# file -> The audio file to translate. Must be a valid audio file (flac, mp3, mp4, mpeg, mpga, m4a, wav, ogg or webm)
# model -> The ID of the model to use. Only 'whisper-1' is currently available
    
# Other parameters:
# prompt -> Optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language
# response_format -> The format of the transcript output. Supported: 'json', 'text', 'srt', 'verbose_json', and 'vtt'. Default is 'json'
# temperature -> Sampling temperature. Simliar use to the 'Chat Completion API'. Must be between 0 and 1. Default is '0'

audio_file = open("speech.mp3", "rb")
response = client.audio.translations.create(
    model="whisper-1",
    file=audio_file,
)

# The response returns the translated text
print("Text translated to English from 'speech.mp3'",response.text)