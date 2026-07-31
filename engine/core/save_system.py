from pathlib import Path
import json
import sys
from engine.core import text_effects
import time
from engine import commands


basic_data = {}
dialogue = []
saves_found = []
stories_found = []


dialogue_path = Path("content/narratives")
savefile = Path("saves")#this is the path to the actual savefile
save_path = Path("saves")#path to all savefiles

current_savefile = 0
current_story = {} #Used to be a string, can't iterate through a string. (that I know of...)
story_count = 0
selected_story = 0

stories: list = []



#TODO: return dictionary and parse story to get metadata.
def get_stories():
	"""
	Grabs stories and append paths into stories.
	"""
	global story_count, stories
	stories.clear()

	story_count = 0
	commands.clear_terminal()
	text_effects.typewriter_text("Stories ", 0.05, 0, 2)

#---------------------------Load story and extract metadata per story. Append all story data to dict or something.
#---------------------------Print some metadata for each story(like; name, version, ect.)
#---------------------------When a story is selected, move story to current story(like '.pop()'), and clear variable to free up memory.


	for file in dialogue_path.rglob("story.json"):##HACK :Saves should go in the narrative's folder!
		story_count += 1
		
		text_effects.typewriter_text(
					f"{story_count}", 0.01, 0, 0, 0.1)

		with file.open('r', encoding='utf-8') as f:
			data = json.load(f)

			if not isinstance(data, dict):
				print(f"Error: {file} must begin with '{{}}', not a list '[]'.")
				continue

			if "metadata" not in data:
				print(f"Error: {file} is missing 'metadata' section.")
				continue

			stories.append({
				"path": file,
				"metadata": data["metadata"]
			})
			
		for key, value in data["metadata"].items():#Print metadata
			text_effects.typewriter_text(f"  {key.title()}: {value}", 0.01, 0, 1, 0)

		print("\n")
		
		# text_effects.typewriter_text(
		# 	f"{story_count}: {file.parent.name} at {file.parent}", 
		# 	0.01, 0, 1, 0.1
		# 	)
		
	
	if story_count <= 0:
		sys.exit("Error: No playable stories have been found.")

	pick_story()





def get_saves(narrative_name):#HACK: Saves should go in the narrative's folder!
	"""
	Gets saves for selected savefile.
	"""
	global saves_found
	pattern =  f"{narrative_name}*.json"
	saves_found.clear()
	saves_count = 0 ## DELETE: old variable
	
	commands.clear_terminal()
	text_effects.typewriter_text(f"Saves for {narrative_name}", 0.05, 0, 3)
	text_effects.typewriter_text("0: New file", 0.01, 0, 2, .1)

	for file in save_path.rglob(pattern):
		saves_count += 1
		saves_found.append(file)
		text_effects.typewriter_text(f"{saves_count}: {file.stem} at {save_path}", 0.01, 0, 1, .1)
		print("\n")


	match saves_count:
		case 0:
			# TODO: Make new save if none are found.
			text_effects.typewriter_text("None found.", 0.01, 0, 1, .1)
			make_savefile(narrative_name)
		case count if count > 0:
			pick_savefile()

	#print(str(saves_found))



def pick_savefile():
	"""
	Pick savefile from user input.
	"""
	global current_savefile, savefile

	check = input("Choose save (Use numbers, or 'exit'): ")

	try:
		check = int(check)

	except (ValueError, TypeError):
		if check.lower() == "exit":
			sys.exit("Exiting... ")
		else:
			text_effects.typewriter_text("Error. Please use numbers.", 0.01, 0, 2, 0)
			return pick_savefile()

	print("")

	
	if check in range(1, len(saves_found) + 1):#add 1 to be inclusive
		print(check)
		current_savefile = check
		print(type(check))

		time.sleep(4)
		savefile = saves_found[check - 1]
		load_save(current_savefile)

	elif check == 0:
		make_savefile("narrative_name")## HACK: FIX THIS. Currently does not pass useable name to make_savefile()

	else:
		print("Not a selectable story.")
		pick_savefile()
				

	
	print(f"Save chosen: {current_savefile}")
	


def pick_story():
	"""
	Pick story from user input.
	"""
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
		text_effects.typewriter_text("Error. Please use numbers.", 0.01, 0, 2, 0)
		return pick_story()
	

	#print(f"Story chosen: {story_count}")





def check_saves():###Make it so it saves the stories as: "title_save" but lowercase like;  .lower() and add 1,2,3 ect at the end in the folders
	#get_saves()
	pick_savefile()
	global current_save


def load_save(savefile):
	pass



def load_story(story):##Fix so that it loads savefile if picked.
	"Grab and load save based in the input."
	global current_story
	index = story - 1

	print(index)

	
	
	story_path = stories[index]["path"]
	narrative_name = stories[index]["metadata"]["title"] #This looks ugly. Sorry to future maintainers (If any lol, small project)



	#GET THE SAVES BASED ON THE NAME OF THE STORIES!!!
	get_saves(narrative_name)
	
	with story_path.open('r', encoding='utf-8') as file:
		current_story = json.load(file)

	

	#print(current_story)
	#return current_story



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
	print(str(savefile))
	with savefile.open('w', encoding='utf-8') as file:# HACK: FIX OPENING FOLDER INSTEAD OF FILE
		json.dump(basic_data, file, indent=4)


def read_save(key, default=None):
	return basic_data.get(key, default)

def make_savefile(name):
	text_effects.typewriter_text("Creating new savefile...", 0.01, 0, 1, .1)
	#save_path
	# HACK nothing here works yet.
	text_effects.typewriter_text("Done!", 0.01, 0, 3, .1)
	text_effects.typewriter_text("Starting...", 0.01, 0, 1, .1)




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


