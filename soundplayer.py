#!/usr/bin/python

import sys;
import pygame;
import os;
import time;
import Button;
import fnmatch;

from Button import Button;
from pygame.locals import *

class Icon:
	def __init__(self, name):
		self.name = name
		try:
			self.bitmap = pygame.image.load(iconPath + '/' + name + '.png')
		except:
			pass



def signal_handler(signal, frame):
	print 'got SIGTERM'
	pygame.quit()
	sys.exit()


def viewCallback(n):
	print "Callback called, value:",n;


# Setup some variables for the touch screen
os.putenv('SDL_VIDEODRIVER', 'fbcon')
os.putenv('SDL_FBDEV'      , '/dev/fb1')
os.putenv('SDL_MOUSEDRV'   , 'TSLIB')
os.putenv('SDL_MOUSEDEV'   , '/dev/input/touchscreen')

# Initialize pygame and load a background image
pygame.init()
#pygame.mouse.set_visible(False)
modes = pygame.display.list_modes(16)
screen = pygame.display.set_mode(modes[0], FULLSCREEN, 16)
image = pygame.image.load('icons/LapsePi.png');

if image is None or image.get_height() < 240:
	print "Filling screen..."
	screen.fill(0)

if image:
	print "setting display image..."
	screen.blit(image, ((320 - image.get_width() ) / 2, (240 - image.get_height()) / 2))

pygame.display.update();
time.sleep(1);



print "Adding button...";

  # Screen 2 for numeric input
buttons =  [Button((  0,  0,320, 60), bg='box'),
   Button((180,120, 60, 60), bg='0',     cb=viewCallback, value=0),
   Button((  0,180, 60, 60), bg='1',     cb=viewCallback, value=1),
   Button((120,180, 60, 60), bg='3',     cb=viewCallback, value=3),
   Button(( 60,180, 60, 60), bg='2',     cb=viewCallback, value=2),
   Button((  0,120, 60, 60), bg='4',     cb=viewCallback, value=4),
   Button(( 60,120, 60, 60), bg='5',     cb=viewCallback, value=5),
   Button((120,120, 60, 60), bg='6',     cb=viewCallback, value=6),
   Button((  0, 60, 60, 60), bg='7',     cb=viewCallback, value=7),
   Button(( 60, 60, 60, 60), bg='8',     cb=viewCallback, value=8),
   Button((120, 60, 60, 60), bg='9',     cb=viewCallback, value=9),
   Button((240,120, 80, 60), bg='del',   cb=viewCallback, value=10),
   Button((180,180,140, 60), bg='ok',    cb=viewCallback, value=12),
   Button((180, 60,140, 60), bg='cancel',cb=viewCallback, value=11)];

icons = []

print "Loading Icons..."
# Load all icons at startup.
for file in os.listdir("icons"):
	if fnmatch.fnmatch(file, '*.png'):
		icons.append(Icon(file.split('.')[0]))

# Assign Icons to Buttons, now that they're loaded
print"Assigning Buttons"
for b in buttons:            #  For each button on screen...
	for i in icons:      #   For each icon...
		if b.bg == i.name: #    Compare names; match?
			b.iconBg = i     #     Assign Icon to Button
			b.bg     = None  #     Name no longer used; allow garbage collection
		if b.fg == i.name:
			b.iconFg = i
			b.fg     = None



for i,b in enumerate(buttons):
	b.draw(screen)
 

pygame.display.update();

while (True):
	for event in pygame.event.get():
#		print "Got event: ", event.type;
		if(event.type is MOUSEBUTTONDOWN):
			pos = pygame.mouse.get_pos()
			print "Position: ", pos;
			if b.selected(pos):
				print "Button was pressed";
			else:
				print "Button was not pressed!";


