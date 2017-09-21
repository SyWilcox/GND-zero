#GND ZERO

#DROP MULTIPLE PAYLOADS WITH GUI MENU FOR PI ZERO / ZERO W

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

RST= None #piOLED this pin isn't used
#following only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

#128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

#initialize library
disp.begin()

#clear display
disp.clear()

#create blank image for drawing (1 is 1-bit colour)
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

#get drawing object to draw on image
draw = ImageDraw.Draw(image)

#draw a black filled box to clear image
draw.rectangle((0,0,width,height),outline=0, fill=0)

#define constants  for easy resizing
padding = -2
top = padding
bottom = height-padding

x = 0

#load default font
#alternativley load ttf - make sure font file is in same directory as python script
font = ImageFont.truetype('/fonts/nougatine.ttf', 10)
#font = ImageFont.load_default()

while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((x, top), str('METERPRETER SHELL'), font=font, fill=225)
    draw.text((x, top+8), str('reverse_tcp_65535'), font=font, fill=255)

    #display image
    disp.image(image)
    disp.display()
    time.sleep(.1)
