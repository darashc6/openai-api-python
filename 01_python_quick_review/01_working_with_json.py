import json # Serialize and deserialize JSON
from pathlib import Path # Manipulate paths

# 1 - JSON Encoding/Decoding with 'json' Module
# Python object to JSON String
data = {
    'name': 'John',
    'age': 25,
}
json_string = json.dumps(data) # Convert Python object to JSON String -> json.dumps(JSON Object)
print(json_string, ' - Type', type(json_string))

# JSON String to Python object
json_string = '{"name": "John", "age": 25}'
json_object = json.loads(json_string)  # Convert JSON String to Python object -> json.loads(JSON String)
print(json_object, ' - Type', type(json_object))

# Write the 'json_object' variable to a file called 'person.json'. With pretty printing
# Save the file to a specific location ('01_python_quick_review/data')
folder_path = Path('01_python_quick_review/data')
file_path = folder_path / 'person.json'

# Create folder if it doesn't exist
# 'parents' -> Create parent directories if they don't exist
# 'exist_ok' -> Don't raise an error if the folder already exists
folder_path.mkdir(parents=True, exist_ok=True)

# To write using the pretty print format, use 'indent' parameter
with open(file_path, 'w') as json_file:
    json.dump(json_object, json_file, indent=2)
    print('Data written to file -> person.json')

# Read the 'person.json' file and print to screen
with open(file_path, 'r') as json_file:
    print("Reading from person.json")
    json_object = json.load(json_file)
    json_string = json.dumps(json_object, indent=2)
    print(json_string)