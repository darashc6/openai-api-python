import requests # HTTP library for making web requests
import json # JSON serialization/deserialization
from pathlib import Path # Manipulate paths

# 2 - Makiing HTTP requests using the 'requests' Module
# GET request, and then writing the result in a 'posts.json' file
response = requests.get('https://jsonplaceholder.typicode.com/posts')
print('Status Code: ', response.status_code)
response_json = response.json()

# Saving the 'response_json' in a '01_python_quick_review/data/full_posts.json' file
folder_path = Path('01_python_quick_review/data')
file_path = folder_path / 'full_posts.json'

# Create folder if it doesn't exist
folder_path.mkdir(parents=True, exist_ok=True)

# Write the 'response_json' variable to a file called 'full_posts.json'
with open(file_path, 'w') as json_file:
    json.dump(response_json, json_file, indent=2)
    print('Data written to file -> full_posts.json')



# GET request with parameters, and then writing the result in a 'posts_with_params.json' file
# Return all posts whose 'userId' is equal to 1
parameters = {'userId': 1}
response = requests.get('https://jsonplaceholder.typicode.com/posts', params=parameters)
print('Status Code: ', response.status_code)
response_json = response.json()

# Saving the 'response_json' in a '01_python_quick_review/data/posts_with_params.json' file
file_path = folder_path / 'posts_with_params.json'

# Write the 'response_json' variable to a file called 'posts_with_params.json'
with open(file_path, 'w') as json_file:
    json.dump(response_json, json_file, indent=2)
    print('Data written to file -> posts_with_params.json')


# POST request, and then writing the result in a 'new_post.json' file
# Create a new post
new_post = {
    'title': 'foo',
    'body': 'bar',
    'userId': 12
}
json_string = json.dumps(new_post)

response = requests.post('https://jsonplaceholder.typicode.com/posts', data=json_string)
print('Status Code: ', response.status_code)
response_json = response.json()

# Saving the 'response_json' in a '01_python_quick_review/data/new_post.json' file
file_path = folder_path / 'new_post.json'

# Write the 'response_json' variable to a file called 'new_post.json'
with open(file_path, 'w') as json_file:
    json.dump(response_json, json_file, indent=2)
    print('Data written to file -> new_post.json')



# PUT request, and then writing the result in a 'updated_post.json' file
# Update an existing post
updated_post = {
    'id': 1,
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
json_string = json.dumps(updated_post)

response = requests.put('https://jsonplaceholder.typicode.com/posts/1', data=json_string)
print('Status Code: ', response.status_code)
response_json = response.json()

# Saving the 'response_json' in a '01_python_quick_review/data/updated_post.json' file
file_path = folder_path / 'updated_post.json'

# Write the 'response_json' variable to a file called 'updated_post.json'
with open(file_path, 'w') as json_file:
    json.dump(response_json, json_file, indent=2)
    print('Data written to file -> updated_post.json')


# DELETE request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print('Status Code: ', response.status_code)
print('Response: ', response.json())