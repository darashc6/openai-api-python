# Exception when updating the 'Todo' item fails
# This exception is raised when at least one of the 'title', 'description' or 'completed' fields is not specified in the request body
class InvalidTodoUpdateException(Exception):
    def __init__(self, message="At least one of 'title', 'description' or 'completed' must be specified."):
        self.message = message
        super().__init__(self.message)