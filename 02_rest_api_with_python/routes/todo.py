# routes/todo.py - Contains all the routes and logic for the 'Todo' model
from fastapi import HTTPException, status, APIRouter
from db import todos_table # importing the 'todos_table' for database actions
from models.Todo import Todo, TodoUpdate # importing the 'Todo' model
from exceptions.invalid_todo_update_exception import InvalidTodoUpdateException
from tinydb import Query

router = APIRouter()


# Endpoint -> "/todos" - GET
# Returns all the 'todos'
@router.get("/todos", response_model=list[Todo])
def get_todos():
    return todos_table.all()

# Endpoint -> "/todos/{todo_id}" - GET
# Returns a specific 'todo'
# * Uses a path parameter to specify which 'todo' to return -> 'todo_id'
@router.get("/todos/{todo_id}", response_model=Todo, status_code=status.HTTP_200_OK)
def get_todo(todo_id: str):
    # Check if 'Todo' item exists.
    # If it does, return the 'Todo' item
    # If it doesn't, raise an 'HTTPException'
    try:
        Todo = Query()
        result = todos_table.search(Todo.id == todo_id)

        return result[0]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo item not found')

# Endpoint -> "/todos" - CREATE
# Creates a new 'todo'
# * If we want to specify the return type, we can use the 'response_model' parameter
# * If we want to specify the status code, we can use the 'status_code' parameter
@router.post("/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo: Todo):
    try:
        # Insert the new 'Todo' item into the 'todos_table'
        # To insert the 'Todo' item, we need to convert it to a dictionary -> todo.model_dump()
        todos_table.insert(todo.model_dump())
        return todo
    except Exception as e:
        # General catch-all exception
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='An Error ocurred while creating a new todo item.')

# Endpoint -> "/todos/{todo_id}" - PUT
# This endpoint will update a specific 'Todo' item
@router.put("/todos/{todo_id}", response_model=Todo, status_code=status.HTTP_200_OK)
def update_todo(todo_id: str, todo_to_update: TodoUpdate):
    # First, we check that the 'Todo' item with the specified ID metioned in the 'todo_id' parameter exists
    Todo = Query()
    todo_exists = todos_table.search(Todo.id == todo_id)

    if not todo_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo item not found')

    updated_todo = todo_exists[0]

    # Next, we check if the 'todo_to_update' object contains any 'None' values ('title', 'description', 'completed')
    # If it does, we raise an 'InvalidUpdateException'
    if todo_to_update.title is None and todo_to_update.description is None and todo_to_update.completed is None:
        raise InvalidTodoUpdateException()
    
    # If the above check is clear without errors, we update the 'Todo' item
    # We update all the fields that are not 'None' (Present in the 'body' of the request)
    for field, value in todo_to_update.model_dump().items():
        if value is not None:
            updated_todo[field] = value
    
    todos_table.update(updated_todo, Todo.id == todo_id)
    return updated_todo

# Endpoint ("/todos/{todo_id}") - DELETE
# This endpoint will delete a specific 'Todo' item
@router.delete("/todos/{todo_id}", status_code=status.HTTP_200_OK)
def delete_todo(todo_id: str):
    # we check that the 'Todo' item with the specified ID exists and proceed to delete such item
    Todo = Query()
    todo_deleted = todos_table.remove(Todo.id == todo_id)

    if not todo_deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Todo item not found')
    
    return {"message": "Todo item deleted successfully"}