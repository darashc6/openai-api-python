# Hello World
print("Hello World")

# Exploring Data Types
numInteger = 10 # Integer
numFloat = 10.0 # Float
text = "Hello World" # String
numList = [10, 20, 30] # List -> Ordered, mutable collection
numTuple = (10, 20, 30) # Tuple -> Ordered, inmutable collection
numDict = {1: "One", 2: "Two"} # Dictionary -> Key-value pairs
isTrue = True # Boolean

# Control Structures in Python
# Conditional Statements - If-Elif-Else Statement
if numInteger > 0:
    print("Positive")
elif numInteger < 0:
    print("Negative")
else:
    print("Zero")

# Loops - For Statements
for num in numList:
    print(num)

# Loops - While Statements
while numInteger > 0:
    print(numInteger)
    numInteger -= 1

# Functions
def greet(name):
    return "Hi " + name + "!"

print(greet("Darash"))


# Lists
numList = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
mixed_list = [1, "hello", 3.0, True]

print(numList[0]) # Accessing elements by index
print(fruits[-1]) # Accessing last element
print(fruits[0:3]) # Accessing multiple elements (Slicing)
fruits.append("mango") # Adding new element at the end of the lsit
fruits.remove("banana") # Removing an element
fruits.sort() # Sorting the list
print(fruits)
print(len(fruits)) # Length of the list

# Create a list of sports movies
sports_movies = ["Rocky", "Hoosiers", "Remember the Titans", "Rudy", "Field of Dreams"]
sports_movies.append("Rugrats") # Add a new sport movie
print(sports_movies)
print("Length of the list:", len(sports_movies))


# Tuples
coordinated = (3, 5)
rgb_colors = (255, 0, 0)

print(coordinated[0]) # Accessing elements by index
print(rgb_colors[-1]) # Accessing last element
combined = coordinated + rgb_colors # Combining two tuples
print(combined)


# Dictionaries
student = {
    'name': 'John',
    'age': 25,
    'grades': {
        'math': 'A',
        'history': 'B'
    }
}

print(student['name']) # Accessing elements by key
print(student['grades']['history']) # Accessing nested elements
student['gender'] = 'male' # Adding new key-value pair
student['grades']['physics'] = 'C' # Adding new nested key-value pair
print(student)


# Combining data structures
books = [
    {
        'title': 'Book1',
        'author': 'Author1',
        'year': 2020
    },
    {
        'title': 'Book2',
        'author': 'Author2',
        'year': 2021
    },
    {
        'title': 'Book3',
        'author': 'Author1',
        'year': 2022
    },
]

# Accessing elements
print(books[0]['author'])

# Filtering
filtered_books = [book for book in books if book['author'] == 'Author1']
print(filtered_books)