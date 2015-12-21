#!/usr/bin/python

import sys;
import random;
import pygame;
import os;
import time;
import fnmatch;
import argparse;
import ConfigParser;

from pygame.locals import *

def signal_handler(signal, frame):
	print 'got SIGTERM'
	pygame.quit()
	sys.exit()

def IsDirectory(val):
	if not os.path.exists(val) or not os.path.isdir(val):
		msg = val,"does not exist or is not a directory."
		raise argparse.ArgumentTypeError(msg)
	return val

def GetRandomFile(directory):
	files = []
	for root,dirname,filenames in os.walk(directory):
		for regex in ('*.wav', '*.mp3'):
			for filename in fnmatch.filter(filenames, regex):
				files.append(os.path.join(root, filename))

	rand = random.randint(0, len(files)-1)
	return files[rand]

def playSound(directory):
	file2play = GetRandomFile(directory)
	print "playing", file2play
	pygame.mixer.init(44100, -16, 1, 1024)
	sound = pygame.mixer.music.load(file2play)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		time.sleep(1)
	pygame.mixer.quit()


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("rootfolder", help="The root directory for the application.",type=IsDirectory)
	parser.add_argument("--config", help="config file name. in above mentioned directory.", type=str, default="soundplayer.cfg")
	args = parser.parse_args()
	
	configfile = os.path.join(args.rootfolder, args.config);

	config = ConfigParser.RawConfigParser()
	if os.path.isfile(configfile) and os.access(configfile, os.R_OK):
		config.readfp(open(configfile))
		print "Readed configuration file"
	else:
		sys.exit("Failed to read config file")
	
	interval_min = config.getint('Config', 'min_time')
	interval_max = config.getint('Config', 'max_time')
	interval_rand = random.randint(interval_min, interval_max)	

	print "Min Time:", interval_min
	print "Max Time:", interval_max
	print "Random:", interval_rand

	while (True):
		playSound(args.rootfolder);
		print "sleeping", interval_rand
#		time.sleep(interval_rand)
		time.sleep(5)
		
		interval_rand = random.randint(interval_min, interval_max);	


if __name__ == "__main__":
	main()
