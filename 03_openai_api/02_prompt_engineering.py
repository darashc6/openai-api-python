from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Function using the 'Chat Completion' API
def get_chat_completion(user_prompt, system_role='You are a helpful assistant.', model='gpt-3.5-turbo', temperature=1):
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature
    )

    return completion.choices[0].message.content


# Effective guidelines/tactics for 'Prompt Engineering'

# Tactic #1: Put instructions at the beginning of the prompt, each on their new line, and use delimiters to clearly indicate distinct parts of the prompt.
# These delimiters can be: Triple backticks, triple quotes, curly braces, brackets, etc.

text = '''
Prompt engineering is a new discipline for developing and optimizing prompts to efficiently user language models (LMs) for a wide variety of applications and research topics.
'''

prompt = f'''
Translate the text delimited by brackets from English to Hindi.
({text})
'''

response = get_chat_completion(prompt)
print('Response to Tactic #1:',response)


# Tactic #2: Be specific, descriptive and as detailed as possible about the context, outcome, or length

text = '''
Artificial Intelligence (AI) represents a monumental leap in technological advancement, symbolizing the culmination of centuries of scientific exploration and innovative thinking. At its core, AI is about creating machines capable of mimicking human intelligence, performing tasks ranging from simple computations to complex problem-solving activities. The fundamental goal of AI is to enable machines to learn from experience, adjust to new inputs, and perform human-like tasks efficiently. This innovative technology utilizes deep learning and natural language processing, allowing machines to process and analyze large amounts of data, identify patterns, and make decisions with minimal human intervention.

The applications of AI are vast and varied, touching nearly every sector of modern life. In healthcare, AI is revolutionizing diagnostics and treatment, enabling early detection of diseases through advanced algorithms and enhancing patient care with personalized treatment plans. In the world of business, AI is transforming operations through predictive analytics, automating mundane tasks, and facilitating more informed decision-making. Similarly, in everyday life, AI manifests in the form of virtual assistants, recommendation systems on streaming services, and smart home devices, making life more convenient and tailored to individual preferences.

However, the rapid growth of AI also brings forth significant ethical and societal challenges. The automation of jobs has sparked debates over the future of employment and the need for new skills in the workforce. Issues of privacy and data security emerge as AI systems require vast amounts of data to function effectively, raising concerns about how this data is collected, used, and protected. Moreover, the potential for bias in AI algorithms, stemming from the data they are fed, poses a risk of perpetuating and amplifying existing societal prejudices, necessitating rigorous oversight and ethical guidelines in AI development and deployment.

In conclusion, AI stands at the forefront of a technological revolution, offering immense potential to improve efficiency, enhance convenience, and solve complex problems. As AI continues to evolve and integrate into various aspects of life, it is imperative to balance its benefits with careful consideration of the ethical, societal, and economic implications it brings. The future of AI promises both excitement and challenges, and navigating this landscape requires a collaborative effort from technologists, ethicists, policymakers, and the public to harness the full potential of AI while safeguarding against its risks.
'''

# Example of a 'Good' prompt
prompt = f'''
Summarize the text below delimited by triple backticks in, at most, 50 words.
Once you have summarized the text, count the number of words the text, and write it in a new paragraph (E. g: This text has been summarized into 'x' words).
Text : ```{text}```
'''
response = get_chat_completion(prompt)
print('Response to Tactic #2.1:',response)

# Example of a 'Great' prompt
prompt = f'''
Summarize the text below, delimited by triple backticks.
Begin the summary with an introduction sentence, followed by a bulleted list highlighting the key points in the text.
Conclude the summary with a sentence that encapsulates main idea of the text.
Text: ```{text}```
'''
response = get_chat_completion(prompt)
print('Response to Tactic #2.2:',response)


# Tactic #3: Use the RTF Format
# RTF -> Role, Task, Format

# Example #1
system_role = '''
You are an experienced Linux System Administrator and will provide only safe and error-free commands.
'''

prompt = '''
Configure the Nginx Web Server for Virtual Hosting.
Consider the following:
1. The Operating System is Ubunto
2. The name of the website (domain name) is gpt-prompting.ai
3. Enable SSL
4. Redirect HTTP requests to HTTPS
5. Explain each step and command
'''

response = get_chat_completion(user_prompt=prompt, system_role=system_role)
print('Response to Tactic #3.1:',response)

# Example #2
system_role = '''
You are a literary critic, carefully evaluating, studying and discussing literature.
'''
prompt = '''
Analize world literature and provide a list of the top 10 books a teenager should read.
Present the output in JSON format with the following keys: book_id, title, author, year, genre and description.
'''

response = get_chat_completion(user_prompt=prompt, system_role=system_role)
print('Response to Tactic #3.2:',response)


# Tactic #4: Few-Shot Prompting 
# Zero-Shot Prompting -> The user provides the LLM with a prompt, and the LLM tries to generate the output as well as it can based on the understandinglanguage and the knownledge.
# Few-Shot Prompting -> The user provides the LLM with a few examples of the desired output, along with clear instructions and context.

# Example of 'Zero-Shot Prompting'
prompt = 'Teach me about love.'
response = get_chat_completion(prompt)
print('Response to Tactic #4.1:',response)

# Example of 'Few-Shot Prompting'
system_role = 'You are an assistant that answers in a consistent manner.'
prompt = '''
[apprentice]: Teach me about patience.

[master]: The river that carves the deepest valley flows from a modest spring;
the grandest symphony originates from a single note;
the most intricate tapestry begins with a solutary thread.

[apprentice]: Teach me about love.
'''
#response = get_chat_completion(user_prompt=prompt, system_role=system_role)
# print('Response to Tactic #4.2:',response)

# The example above is more useful for the 'ChatGPT' Web Interface
# If we want to adapt it using the 'Chat Completion API', the end result would be the following+
messages = [
    {"role": "system", "content": "You are an assistant that answers in a consistent manner."},
    {"role": "user", "content": "[apprentice]: Teach me about patience."},
    {"role": "assistant", "content": "[master]: The river that carves the deepest valley flows from a modest spring;\n the grandest symphony originates from a single note;\n the most intricate tapestry begins with a solutary thread."},
    {"role": "user", "content": "[apprentice]: Teach me about love."},
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=1
)
print('Response to Tactic #4.3:',response.choices[0].message.content)


# Tactic #5: Specify the steps required to complete a task, spliting complex tasks into smalle subtasks
system_role = '''
You are a helpful assistant.

Use the following step-by-step instructions to respond to user inputs.

Step 1 - The user will provide you with text in triple backticks. Summarize this text in one sentence with a prefix that says "Summary: ".

Step 2 - Translate the summary of the text (from Step 1) to Portuguese, with a prefux that says "Summary (in Portuguese): ".

Step 3 - Extract each planet in the original text into a Python list, with the variable name being "list_planets".

Step 4 - Extract each planet and it's characteristics in the original text, and output a json object that contains the following keys for each planet: planet_name, planet_characteristics.


Separate your answers with line breaks.
'''
text = '''
Our solar system, a cosmic assembly of wonder, orbits around the Sun, a middle-aged star. It comprises eight diverse planets, from the rocky inner worlds like Earth and Mars to the gas giants such as Jupiter and Saturn. The asteroid belt, teeming with remnants from the solar system's formation, separates these two groups. Beyond Neptune, the icy bodies of the Kuiper Belt, including dwarf planets like Pluto, linger. Each planet, with its unique characteristics and moons, contributes to the solar system's dynamic nature. This celestial neighborhood, set against the backdrop of the Milky Way galaxy, represents just a tiny fraction of the universe's vast expanse, reminding us of both the uniqueness and insignificance of our home in the cosmos.
'''
prompt = f'''
```{text}```
'''
response = get_chat_completion(prompt, system_role=system_role)
print('Response to Tactic #5:',response)


# For additional tactics and guidelines for better prompting
# https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results
