import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://inspirobot.me/api?generate=true")
im_url = r.content.decode()

img = Image.open(requests.get(im_url, stream=True).raw)
img = img.save("img1.jpg")
