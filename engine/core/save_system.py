from pathlib import Path
import json
import sys
from engine.core import text_effects
import time

basic_data = {}
dialogue = []
saves_found = []
stories_found = []
stories_found_var = []

dialogue_path = Path("content/narratives")
savefile_path = Path("saves")#FIX SO IT CALLS saveFILE not directory!!

current_savefile = 0
current_story = ""
saves_count = 0
story_count = 0
selected_story = 0



def get_stories():
	"""
	Grabs stories and append paths into stories_found.
	"""
	global story_count, stories_found
	stories_found.clear()

	story_count = 0
	text_effects.clear_terminal()
	text_effects.typewriter_text("Stories ", 0.05, 2)


	for file in dialogue_path.rglob("*.json"):
		story_count += 1
		stories_found.append(file)
		text_effects.typewriter_text(f"{story_count}: {file.stem} at {dialogue_path}", 0.01, 1, .1)
		print("\n")
	
	if story_count <= 0:
		sys.exit("Error: No playable stories have been found.")

	pick_story()
		


def get_saves(narrative_name):
	"""
	Gets saves for selected savefile.
	"""
	global saves_count, saves_found
	pattern =  f"{narrative_name}*.json"
	saves_found.clear()
	saves_count = 0
	
	text_effects.clear_terminal()
	text_effects.typewriter_text(f"Saves for {narrative_name}", 0.05, 3)
	text_effects.typewriter_text("0: New file", 0.01, 2, .1)

	for file in savefile_path.rglob(pattern):
		saves_count += 1
		saves_found.append(file)
		text_effects.typewriter_text(f"{saves_count}: {file.stem} at {savefile_path}", 0.01, 1, .1)
		print("\n")


	match saves_count:
		case 0:
			# TODO: Make this make a new save if none are found.
			text_effects.typewriter_text("None found.", 0.01, 1, .1)
			text_effects.typewriter_text("Creating new savefile...", 0.01, 1, .1)
			text_effects.typewriter_text("Lol, I haven't made the logic yet. pls make it.", 0.01, 1, .1)
			#make_savefile(narrative_name)
			#text_effects.typewriter_text("Done!", 0.01, 3, .1)
			#text_effects.typewriter_text("Starting...", 0.01, 1, .1)
		case count if count > 0:
			pick_savefile()

	#print(str(saves_found))



def pick_savefile():
	global current_savefile
	check = input("Choose save (Use numbers, or 'exit'): ")
	print("")
	

	if check.lower() == "exit":
		sys.exit("Exiting... ")
	
	try:
		check_num = int(check)
		
		match check_num:
			case int():
				if check_num in range(1, saves_count + 1):#add 1 to be inclusive
					print(check_num)
					current_savefile = check
					load_save(current_savefile)
				else:
					print("Not a selectable story.")
					pick_savefile()
				

	except ValueError:
		text_effects.typewriter_text("Error. Please use numbers.", 0.01, 2, 0)
		return pick_savefile()
	
	print(f"Save chosen: {current_savefile}")
	


def pick_story():
	global story_count, selected_story
	check = input("Choose Story (Use numbers, or 'exit'): ")
	print("")

	if check.lower() == "exit":
		sys.exit("Exiting... ")
	
	try:
		check_num = int(check)
		
		match check_num:
			case int():
				if check_num in range(1, story_count + 1):#add 1 to be inclusive
					print(check_num)

					load_story(check_num)
				else:
					print("Not a selectable story.")
					pick_story()

	except ValueError:
		text_effects.typewriter_text("Error. Please use numbers.", 0.01, 2, 0)
		return pick_story()
	

	#print(f"Story chosen: {story_count}")





def check_saves():###Make it so it saves the stories as: "title_save" but lowercase like;  .lower() and add 1,2,3 ect at the end in the folders
	#get_saves()
	pick_savefile()



	global current_save
def load_save():
	pass



def load_story(story):##Fix so that it loads savefile if picked.
	"Grab and load save based in the input."
	global current_story
	index = story - 1

	story_path = stories_found[index] #Returns path
	narrative_name = story_path.stem

	#text_effects.typewriter_text("WAITING for debug...", 0.04, 2, 15)

	#GET THE SAVES BASED ON THE NAME OF THE STORIES!!!
	get_saves(narrative_name)
	
	with story_path.open('r', encoding='utf-8') as file:
		current_story = json.load(file)

	#print(current_story)
	return current_story



##------------------MAKE SAVE SYSTEM ADD SAVES FOR EACH STORY.



def write_save(key, value):
	"""
	Update game memory and calls save_game() 
	to write to disk.

	  key = key for list

	  value = data to be saved to key value
	"""
	global basic_data

	basic_data[key] = value
	save_game()



def save_game():
	"""
	Function to write data to the disk.
	"""
	print(str(savefile_path))
	with savefile_path.open('w', encoding='utf-8') as file:####FIX OPENING FOLDER INSTEAD OF FILE
		json.dump(basic_data, file, indent=4)


def read_save(key, default=None):
	return basic_data.get(key, default)



def times_played(command = "increment"):
	"""
	Function to increment times played. 
	
	Parameters for command:
		increment =  add to times played, 
		
		read = return times played, 
		
		clear = clear times played. 

		Anything else throws an error.
	"""
	match command:
		case "increment":
			write_save("played", read_save("played", 0) + 1)
		case "read":
			return read_save("played", 0)
		case "clear":
			write_save("played", 0)
		case _:
			print("Failure to read or write. Input command not known.")


