from openai import OpenAI
from dotenv import load_dotenv
import requests

load_dotenv()

client = OpenAI()

# 'Image Creation' API
# https://platform.openai.com/docs/api-reference/images/create
# Required parameters:
# prompt -> Text description of the desired image

# Other parameters:
# model -> The model to use for image generation. Default is 'dall-e-2'. To check which model is compatible, visit 'https://platform.openai.com/docs/models/model-endpoint-compatibility'.
# n -> Number of images to generate. Default is 1
# quality -> Image quality. Default is 'standard' (Only available for model -> 'dall-e-3')
# size -> Image size. Default is '1024x1024'. Must be one of '256x256', '512x512', or '1024x1024' for 'dall-e-2' and '1024x1024', '1792x1024' '1024x1792' for 'dall-e-3'
# style -> Style of the generated image. Must be one of 'natural' or 'vivid'. Default is 'natural' (Only available for model -> 'dall-e-3')
# response_format -> Format of the response. Must be 'url' or 'b64_json'. Default is 'url'.
response = client.images.generate(
    model="dall-e-2",
    prompt="a photograph of an astronaut riding a horse",
    size="1024x1024",
    n=1,
    response_format="url"
)

# Return the Image URL, and save it in a file called 'dalle2-image.png'
image_url = response.data[0].url
image_resource = requests.get(image_url)

if image_resource.status_code == 200:
    with open("dalle2-image.png", "wb") as image_file:
        image_file.write(image_resource.content)
        
    print("Image saved succesfully!")
else:
    print("Failed to download the image. Status code:", image_resource.status_code)


# Next, we will create a variation of the 'dalle2-image.png', using the 'Image Variation' API
# Note: This API is only available for the 'dall-e-2' model.

# 'Image Variation' API
# https://platform.openai.com/docs/api-reference/images/createVariation
# Required parameters:
# image -> The image to use as the basis for the variation. Must be a valid PNG file, less than 4MB and square (e.g: 1024x1024)
    
# Other parameters:
# model -> The model to use for image generation. The only model available for this API is the 'dall-e-2'
# n -> Number of images to generate. Must be between 1 and 10
# size -> Image size. Default is '1024x1024'. Must be one of '256x256', '512x512', or '1024x1024'.
# response_format -> Format of the response. Must be 'url' or 'b64_json'. Default is 'url'.
response = client.images.create_variation(
    image=open("dalle2-image.png", "rb"),
    n=1,
    size="1024x1024",
)
variation_url = response.data[0].url

# Return the Image URL, and save it in a file called 'dalle2-image_variation.png'
image_resource = requests.get(variation_url)

if image_resource.status_code == 200:
    with open("dalle2-image_variation.png", "wb") as image_file:
        image_file.write(image_resource.content)
        
    print("Variation saved succesfully!")
else:
    print("Failed to download the image. Status code:", image_resource.status_code)