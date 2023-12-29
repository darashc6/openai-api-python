# 'tinydb' -> Python library used for local database. Documen-oriented DB
# To install -> 'pip install tinydb'
from tinydb import TinyDB

db = TinyDB("db.json") # Database file stored in 'db.json'
todos_table = db.table("todos") # Database table -> 'todos'
