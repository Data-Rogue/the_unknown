import os ##pretty straight forward
import time
import re## import regex!!!!! USE THIS!
import random
import string
import sys
import json
from engine.core import save_system
from pathlib import Path
from engine import start
from engine import game
from engine.core import text_effects
from engine.core import save_system
from engine.core import text_renderer

#save_system.check_saves()
#save_system.on_start_checks()# This will exit if the program is missing the dialogue.
#save_system.times_played("increment")
#print(f"Times played: {save_system.times_played("read")}")

# narrative1 = Path("content/narratives/origin.json")
# gamedata = ""
# with narrative1.open('r', encoding='utf-8') as file:
		
# 		gamedata = json.load(file)


# text_renderer.parse_data(gamedata)
#text_renderer.get_story(gamedata)

#time.sleep(30)
game.start_game()
#start.choose_story()

time.sleep(70)


#Deleted old codebase
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
