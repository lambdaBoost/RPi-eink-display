from PIL import Image
import os
import time
import datetime
import random
import inky
from inky.inky_ac073tc1a import Inky as InkyAC073TC1A
import RPi.GPIO as GPIO
from inky_display import display_modes, helpers

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

#display setup
display = InkyAC073TC1A(resolution=(800, 480))
border_colors = ['Black', 'White', 'Green', 'Blue', 'Red', 'Yellow', 'Orange']
saturation = 0.7

#define times for nighttime mode
start = datetime.time(9,0,0)
end = datetime.time(17,0,0)

#now = datetime.datetime.now().time()
#if helpers.time_in_range(start, end, now):
#    im = display_modes.get_inspirobot()
#else:
im = display_modes.get_network_image()

        
#set to inky internal buffer
display.set_image(im, saturation)
    
#set border color (random for now)
display.set_border(random.choice(border_colors))
    
#show the image
display.show()
        
time.sleep(5)

#done pin (switch off pi)
GPIO.output(18,GPIO.HIGH)


