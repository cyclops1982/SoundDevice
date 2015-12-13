#!/usr/bin/python

import sys;
import pygame;
import os;
import time;
import Button;


from Button import Button;
from pygame.locals import *



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
pygame.mouse.set_visible(False)
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
time.sleep(4);

print "Adding button...";

b = Button((5,180,120, 60), bg='start', cb=viewCallback, value=1);

b.draw(screen);
pygame.display.update();

while (True):
	for event in pygame.event.get():
		print "Got event: ", event.type;
		if(event.type is MOUSEBUTTONDOWN):
			pos = pygame.mouse.get_pos()
			print "Position: ", pos;
			if b.selected(pos):
				print "Button was pressed";
			else:
				print "Button was not pressed!";


