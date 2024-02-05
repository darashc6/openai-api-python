from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv() # Load .env variables

client = OpenAI()

# Meal generator for breakfast, lunch and dinner, given a list of ingredients.
def meal_generator(ingredients):
    instructions = f'''
        Create a healthy daily meal plan for breakfast, lunch and dinner, with the following ingredients: {ingredients}
        Explain each recipe.
        The total daily intake should be below 2000 kcal.
        Specify the total number of kcal for each meal.
        Assign a asuggestive and concise title for each meal.
        Your asnwer should end with 'Titles: ' and the title of each recipe.
        For example:

        Titles:
        - Meal 1
        - Meal 2
        - Meal 3
    '''

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'You are a talented chef.'},
            {"role": "user", "content": instructions},
        ],
    )

    return response.choices[0].message.content

# Creating the image of the meal specified, and saving it in a specific file name.
def create_meal_image(meal, file_name):
    response = client.images.generate(
        model="dall-e-2",
        prompt=meal,
        size="1024x1024",
        n=1,
        response_format="url"
    )

    image_url = response.data[0].url
    image_resource = requests.get(image_url)

    if image_resource.status_code == 200:
        with open(f"{file_name}.png", "wb") as image_file:
            image_file.write(image_resource.content)
    else:
        print("Failed to download the image. Status code:", image_resource.status_code)

user_input = input("Enter the ingredients you want to base your meal plan on: ")

if user_input:
    # Prints the detailed information for each meal
    response = meal_generator(user_input)
    print(response)

    # Extracts the meals from the response
    meals = response.splitlines()[-3:]
    meals = [meal.strip('- ')  for meal in meals]
    
    # For each meal, generate an image and save it
    for index, meal in enumerate(meals):
        create_meal_image(meal, f"meal_{index+1}")
    
    print("Meals image saved!")

else:
    print("No ingredients inserted.")