import requests
from io import BytesIO
from PIL import Image
import os
import random


def get_stored_image():

    """
    return a random image from the onboard image directory
    """

    img_dir = './images'
    image_files = os.listdir(img_dir)
    load_img = random.choice(image_files)
    img_path = os.path.join(img_dir, load_img)
    
    with Image.open(img_path) as im:
        
        im = im.resize((800,480))

    return im



def get_inspirobot():

    """
    get image from inspirobot api
    
    """

    r = requests.get("https://inspirobot.me/api?generate=true")
    im_url = r.content.decode()

    img = Image.open(requests.get(im_url, stream=True).raw)
    img = img.resize((480,480))

    #white background
    base_image = Image.new('RGBA', (800,800), (255,255,255,255))
    base_image.paste(img, (160, 0))


    return base_image
