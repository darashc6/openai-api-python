# 'Pydantic' -> Python library used for data validation
# To install -> 'pip install pydantic'
from pydantic import BaseModel
# 'uuid' -> Python library used for generating unique identifiers
import uuid

# * In this file, we will create a new model 'Todo'

# Model used when creating a new 'Todo'
class Todo(BaseModel):
    id: str = str(uuid.uuid4())
    title: str
    description: str
    completed: bool = False

# Model used when updating a 'Todo'
class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None