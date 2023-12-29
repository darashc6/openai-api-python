# REST API with Python

### Description
This project is a basic REST API managing a Todo list. It allows users to create, read, update and delete Todo items. Created with Python.

### Python libraries
* [FastAPI](https://fastapi.tiangolo.com/)
* [Pydantic](https://docs.pydantic.dev/2.5/)
* [TinyDB](https://tinydb.readthedocs.io/en/latest/index.html)

### Installation
To set up this project locally, follow these steps:

1. Clone the repository:
```powershell
git clone https://github.com/darashc6/python-repository
```

2. Navigate to the project directory:
```powershell 
cd 02_rest_api_with_python
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

### Usage
To start the server, run:

```powershell
uvicorn main:app --reload
```

API requests:

* Create a Todo -> 'POST <strong>/todos</strong>'
* Get a Todo -> 'GET <strong>/todos/{todo_id}</strong>'
* Update a Todo -> 'PUT <strong>/todos/{todo_id}</strong>'
* Delete a Todo -> 'DELETE <strong>/todos/{todo_id}</strong>'