# OpenAI API

### Description
This section includes Python files containing the basic but concise explanations, along with example use cases for the main OpenAI's models. Includes the following:
* [Chat Completion API](/03_openai_api/01_chat_completion_api.py) - Simple chat models, similar to ChatGPT
* [Basics of prompt engineering](/03_openai_api/02_prompt_engineering.py) - Strategies and tactics for getting better results from large language models (such as GPT-3.5, GPT-4, etc).
* [DALL-E](/03_openai_api/03_dall_e_api.py) - Generation or manipulation of images with DALL·E in the API.
* [Audio API](/03_openai_api/04_audio_api.py) - Turning text into lifelike spoken audio, and viceversa.
* [Text Embedding](/03_openai_api/05_text_embeddings.py) - Measuring the relatedness of text strings.

### Setup
To set up this project locally, follow these steps:

1. Clone the repository:
```powershell
git clone https://github.com/darashc6/python-repository
```

2. Navigate to the project directory:
```powershell 
cd 03_openai_api
```

3. Set up the virtual environment:
```powershell 
python -m venv venv
```

4. Activate the virtual environment: 
```powershell
venv\Scripts\activate
```

5. Once activated, the command prompt will show the name of the virtual environment, something like '<strong>(venv)</strong>'

6. Install the dependencies present in the '<strong>requirements.txt</strong>' file:
```powershell
pip install -r requirements.txt
```

You will also need an API Key for this particular project. This key will be saved in a <strong>.env</strong> file under the variable name <strong>'OPENAI_API_KEY'</strong>. (See the <strong>'.env.example'</strong> file for guidance).

To generate an OpenAI API key, please refer to this [guide](https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key), and proceed with the '<strong>Setup your API key for a single project</strong>' step.

### Usage
Simply select any of the Python files you would like to execute and run.

For example, if you want to execute the '<strong>01_chat_completion_api.py</strong>' file, simply run the following command:

```powershell
py 01_chat_completion_api.py
```