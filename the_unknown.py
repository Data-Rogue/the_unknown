import os ##pretty straight forward
import time
import re## import regex!!!!! USE THISSS
import random
import string
import sys
import json
from pathlib import Path
from core import text_effects


#Debug Variables-----------Start

restricted_mode = False

#Debug Variables-----------End



#Data? Whats that? 

dataaa = {}
dialogue = []
savefile_path = Path("bitz.json")
dialogue_path = Path("content") / "narrative.json"


if dialogue_path.exists():
	with dialogue_path.open('r', encoding='utf-8') as d:
		dialogue = json.load(d)
		#print(str(dialogue))
		#print("Success")
else:
	sys.exit(f"Error: {dialogue_path} not found. Exiting program.")##breakpoint if dialogue not found-----/o\




def file_init():
	global dataaa, restricted_mode
	if savefile_path.is_file():
		with open('bitz.json', 'r') as file:
			dataaa = json.load(file)
	else:
		restricted_mode = True

file_init()

##Saves data to json
def write_save(key, value):
	dataaa[key] = value
	with open('bitz.json', 'w') as file:
		json.dump(dataaa, file, indent=4)

#Data? Whats that?





##Helper functions begin here -------------------------------------->>>start

##Helper functions end here ---------------------------------------->>>end





##ASCII Art begin here ----------------------------->>>start


startup_node = r"""
 _________________   _____ _-_I_-_      ____
 \                \  \    \   I  ___    \ \ \
  \___(I)  (I)  ___\  \    \ (I)/   \    | | |
	  \         \      \    \  /    /   / / /
	   \         \      \    \/    /   / / /____
		\_________\      \________/   /_/_/____/   Just watching... from afar...
"""

files_texted = r"""
 ____________  ______      ____          .,.,.,     ______
 \     _____| |__  __|    :'''':        E  ____|   y   ___L
  \    \___     \  \      1    1        1  \___   1   d
   \     __\    /  /      L    L        3  ____H   \  \____
	\    \    __\  \__    I    I>--__   |  \___    _\_...  Y
	 \____\  |________|   |__________>  |______|  |________3

"""

##ASCII Art end here ------------------------------->>>end





##Story time ------------------------------------------------------>>>start

disclaimer = "THIS PROJECT DOES NOT TOUCH YOUR FILES IN ANY WAY, INSPECT THE CODE FOR YOURSELF AT https://github.com/Data-Rogue/the_unknown"


files_like = "You know, I like files..."

proposition_pt1 = "\nFiles are data and data is power."
proposition_pt2 = "How about this?"
proposition_pt3 = "You solve a few puzzles, and I'll give you a secret file."
proposition_pt4 = "\nYou will get 3 lives, and 5 hints."
proposition_pt5 = "\nFail, and you start over..."
proposition_pt6 = "\n\nAre we in? (Y, N)"

##Story time ------------------------------------------------------>>>end






#write and save data
current = int(dataaa.get("played", 0))
current += 1
write_save("played", current)

#Get and store username
username = os.getenv("LOGNAME")




if username:
	text_effects.clear_terminal
	text_effects.typewriter_text(startup_node, .015, pause_time=2)
	text_effects.scanning_bar()
	

	restricted_mode = True#-------------------------------------------------------------------delete

	if not restricted_mode:
		if int(dataaa.get("played", 0)) > 0:
			text_effects.typewriter_text(f"\nWelcome back {username}...", 0.05)
		else:
			text_effects.typewriter_text(f"\nHello {username}...", 0.05, 2)
	else:
		text_effects.typewriter_text("Entering restricted mode... ", 0.045, 1, 3.5)

		text_effects.typewriter_text("Because you deleted your data. ", 0.045, 1, 1)

		text_effects.typewriter_text("Smooth.", 0.045, 1, 1.5)

		text_effects.typewriter_text(f"\nHello {username}...", 0.05, 2, 4)
else:
	text_effects.typewriter_text("No username found... ", 0.046, 0, 1.4)
	text_effects.typewriter_text("well done.", .5, 2, 4)




def play_intro():
	
	text_effects.typewriter_text("\n\nI\'ve Noticed something...", .06)
	time.sleep(3)


	text_effects.typewriter_text("Files...", .1)
	time.sleep(2)


	text_effects.typewriter_text(files_like, .05)#You know, I like files...
	time.sleep(3)

	#typewriter_text(proposition_pt1, .04)#And files house all the data we need to live in this 'modern' world.
	text_effects.typewriter_text("You trust files...", .1, 0)
	time.sleep(1.5)
	#typewriter_glitch("but you’ve never questioned them.", 0.04, True, 2)#------------------------------------------------change this back as well
	text_effects.typewriter_text(" but you’ve never questioned them.", .05, 1)
	time.sleep(5)

	text_effects.typewriter_text(proposition_pt2, 0.07)#How about this?
	time.sleep(.8)

	text_effects.typewriter_text(proposition_pt3, 0.05)#You solve a few puzzles, and I'll give you a secret file.
	time.sleep(2)

	text_effects.typewriter_text(proposition_pt4, 0.05)#You will get 3 lives, and 5 hints.
	time.sleep(1.5)

	text_effects.typewriter_text(proposition_pt5, 0.05)#Fail, and you start over...
	time.sleep(5)

	text_effects.typewriter_text(proposition_pt6, 0.1)#Are we in? (Yes, no)



#user says yes or no
def story_1():
	print("\nYour answer: ")
	user_agree = str(input())
	print(f"User says: {user_agree}")


play_intro()
story_1()







#key -> decipher the message -> 



#This is your next thing to work on: scrambling the secret message and unscrambling the message with a key
#the user will recieve a key to unlock the first 

def obfuscate(text, secret_key):
	chars = list(text)
	random.seed(secret_key)
	random.shuffle(chars)
	return "".join(chars)

def deobfuscate(shuffled_text, secret_key):
	# Map the original indices using the same seed
	indices = list(range(len(shuffled_text)))
	random.seed(secret_key)
	random.shuffle(indices)
	
	# Place characters back into their original positions
	original = [None] * len(shuffled_text)
	for i, original_index in enumerate(indices):
		original[original_index] = shuffled_text[i]
	return "".join(original)

# Usage
msg = "The key is 3204 by night, but what is that without flight?"
key = 42

scrambled = obfuscate(msg, key)
print(f"Scrambled: {scrambled}")

unscrambled = deobfuscate(scrambled, key)
print(f"Unscrambled: {unscrambled}")



