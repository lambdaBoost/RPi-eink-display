from PIL import Image
import os
import time
import datetime
import random
import inky
from inky.auto import auto
import RPi.GPIO as GPIO
from inky_display import display_modes, helpers

GPIO.setmode(GPIO.BCM)

#board 7 is gpio 4
GPIO.setup(18, GPIO.OUT)

#display setup
display = auto()
border_colors = ['Black', 'White', 'Green', 'Blue', 'Red', 'Yellow', 'Orange']
saturation = 0.7

#define times for nighttime mode
start = datetime.time(19,0,0)
end = datetime.time(23,59,59)

now = datetime.datetime.now().time()
if helpers.time_in_range(start, end, now):
    im = display_modes.get_inspirobot()
else:
    im = display_modes.get_stored_image()

        
#set to inky internal buffer
display.set_image(im, saturation)
    
#set border color (random for now)
display.set_border(random.choice(border_colors))
    
#show the image
display.show()
        
time.sleep(5)

#done pin (switch off pi)
GPIO.output(18,GPIO.HIGH)


