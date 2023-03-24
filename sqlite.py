import requests
from PIL import Image
from io import BytesIO

# URL of the image to download
url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fhiddenhomemade.com%2Fporn%2Ffree-porn%2Fbbc%2Fbbc-bbc-white-face-5c7e77921d50c-3.html&psig=AOvVaw00LYzoM4EufFHK9WVcj9Jl&ust=1679782239141000&source=images&cd=vfe&ved=0CA4QjhxqFwoTCJj05dXK9f0CFQAAAAAdAAAAABAQ"

# Send a GET request to the URL to fetch the image data
response = requests.get(url)

# Check if the response was successful (status code 200)
if response.status_code == 200:

    # Open the image data as a PIL Image object using BytesIO
    img = Image.open(BytesIO(response.content))

    # Save the image to a local file
    img.save("image.jpg")

    print("Image downloaded successfully.")

else:
    print("Error downloading image.")
