#!/usr/local/bin/python
import random
import os
import sys
import subprocess

qoutes = [
"Come on you target for faraway laughter. Come on you stranger, you legend, you martyr, and shine",
"There is no dark side of the Moon.\nIt's all dark, really.",
"Remember when you were young?\nYou shone like the Sun...",
"All in all, you're just another brick in the wall.",
"Did You Exchange A Walk On Part In The War For A Lead Role In A Cage?",
"There's someone in my head, but that's not me",
"No one told you when to run, You missed the starting gun",
"Home, Home Again. I like to be here when I can"
"And you run and you run, To catch up with the sun",
"Hey You !"]


PINK_FLOYD_ART="""_          _              ___ 
  _ __ (_)_ __ | | __  / _| | ___  _   _  __| |
 | '_ \| | '_ \| |/ / | |_| |/ _ \| | | |/ _` |
 | |_) | | | | |   <  |  _| | (_) | |_| | (_| |
 | .__/|_|_| |_|_|\_\ |_| |_|\___/ \__, |\__,_|
 |_|                               |___/       """

def get_random_qoute(qoutes):
	if qoutes:
		qlen = len(qoutes)
		selection = random.randint(0,qlen-1)
		return qoutes[selection]

message = get_random_qoute(qoutes)
full_message = PINK_FLOYD_ART + "\n" + message
print(full_message)
exit(0)
# check if running with sudo access
if  os.geteuid() == 0:
	# overwrite message to motd
	with open("/etc/motd","w") as fh:
		fh.write(full_message)
	exit("Login with new window to see motd")
else:
	exit("Could not change the motd")	
