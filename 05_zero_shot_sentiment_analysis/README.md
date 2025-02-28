# Project: Zero-Shot Sentiment Analysis using ChatGPT and Streamlit

### Description
Developed a web app using Streamlit and the OpenAI API for zero-shot sentiment analysis, accommodating both text and emotions as input. Users interact with an intuitive interface, allowing dynamic analysis and exploration of sentiment patterns in user-provided content.

### Setup
To set up this project locally, follow these steps:

1. Clone the repository:
```powershell
git clone https://github.com/darashc6/python-repository
```

2. Navigate to the project directory:
```powershell 
cd 05_zero_shot_sentiment_analysis
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
To start the Streamlit app, run:

```powershell
streamlit run main.py
```
