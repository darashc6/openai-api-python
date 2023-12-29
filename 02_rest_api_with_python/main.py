# 'FastAPI' -> Python library used for building REST APIs
# To install -> 'pip install fastapi'
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from exceptions.invalid_todo_update_exception import InvalidTodoUpdateException # Importing the 'InvalidYodoUpdateException' exception
from routes.todo import router as todo_router # Importing all the API routes related with the 'Todo' model

# * To run the server -> 'uvicorn main:app --reload'
# 'main:app' -> Tells Uvicorn to look for an object named "app" in the "main.py" file
# '--reload' -> Tells Uvicorn to reload the server if a change is made. 

# Creating a new 'FastAPI' instance
app = FastAPI()

app.include_router(todo_router) # Include all the API routes related with the 'Todo' model

# Creating a new exception handler for 'InvalidTodoUpdateException'
@app.exception_handler(InvalidTodoUpdateException)
def invalid_todo_update_exception_hanlder(request, exc: InvalidTodoUpdateException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": str(exc)},
    )

# Endpoint -> "/" - GET
# Returns 'Hello World!'
@app.get("/")
def get_root():
    return "Hello World!"