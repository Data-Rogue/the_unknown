from pathlib import Path
import json
import sys
from engine.core import text_effects

basic_data = {}
dialogue = []
saves_found = []

dialogue_path = Path("content/narratives")
savefile_path = Path("saves")

current_savefile = 0
current_story = ""



def get_stories():

	count = -1
	text_effects.clear_terminal()
	text_effects.typewriter_text("Stories ", 0.05, 2)


	for file in dialogue_path.rglob("*.json"):
		count += 1
		saves_found.append(str(file))
		text_effects.typewriter_text(f"{count}: {file.name} at {dialogue_path}", 0.01, 1, .1)
		print("\n")
	
	if count <= -1:
		sys.exit("Error: No playable stories have been found.")
	
	pick_story()
		


def get_saves():
	"""
	Gets saves and prints them.
	"""

	count = 0
	text_effects.clear_terminal()
	text_effects.typewriter_text("Saves ", 0.05, 2)

	text_effects.typewriter_text("0: New file", 0.01, 2, .1)

	for file in savefile_path.rglob("*.json"):
		count += 1
		saves_found.append(str(file))
		text_effects.typewriter_text(f"{count}: {file.name} at {savefile_path}", 0.01, 1, .1)
		print("\n")
	
	if count == 0:
		text_effects.typewriter_text("None found.", 0.01, 1, .1)
	#print(str(saves_found))



def pick_savefile():
	global current_savefile
	check = input("Choose save (Use number corresponding to save e.g., '2'. Or 'exit'): ")
	print("")

	if check.lower() == "exit":
		sys.exit("Exiting... ")
	
	try:
		check_num = int(check)
		
		match check_num:
			case int():
				current_savefile = check

	except ValueError:
		text_effects.typewriter_text("Error. Please use numbers.", 0.01, 2, 0)
		return pick_savefile()
	
	print(f"Save chosen: {current_savefile}")
	


def pick_story():
	global current_story
	check = input("Choose Story (Use number corresponding to story e.g., '2'. Or 'exit'): ")
	print("")

	if check.lower() == "exit":
		sys.exit("Exiting... ")
	
	try:
		check_num = int(check)
		
		match check_num:
			case int():
				current_story = check

	except ValueError:
		text_effects.typewriter_text("Error. Please use numbers.", 0.01, 2, 0)
		return pick_story()
	

	print(f"Story chosen: {current_story}")





def check_saves():###Make it so it saves the stories as: "title_save" but lowercase like;  .lower() and add 1,2,3 ect at the end in the folders
	get_saves()
	pick_savefile()



def load_save():
	pass

def load_story():
	pass


##------------------MAKE SAVE SYSTEM ADD SAVES FOR EACH STORY.
# [
#   {
#     "effect": "regular",
#     "text": "H-hello?",
#     "speed": 0.06,
#     "newline": 1,
#     "pause": 3
#   },
#   {
#     "effect":"regular",
#     "text": "Who's there??",
#     "speed": 0.1,
#     "delay": 2
#   },
#   {
#     "text": "You trust files...",
#     "speed": 0.1,
#     "delay": 1.5
#   }
# ]




#Change dialogue to be more lighthearted.
#Like "You... chose that? Interesting. I wasn't expecting that."


# print(dialogue_path)
# print(dialogue_path.resolve())
# print(dialogue_path.exists())

# def check_dialogue():
# 	global dialogue

# 	if not dialogue_path.exists():
# 		sys.exit(f"Error: {dialogue_path} not found. Exiting program... ")

# 	try:
# 		with dialogue_path.open('r', encoding='utf-8') as file:
# 			dialogue = json.load(file)#####--------------------------------------------------pass dialogue into text renderer!
# 	except json.JSONDecodeError:
# 		sys.exit(f"Error: {dialogue_path} is empty or contains invalid JSON.")


# def check_save():
# 	global basic_data

# 	if not savefile_path.exists():
# 		savefile_path.parent.mkdir(parents=True, exist_ok=True)

# 		with savefile_path.open('w', encoding='utf-8') as file:
# 			json.dump({}, file, indent=4)

# 	try:
# 		with savefile_path.open('r', encoding='utf-8') as file:
# 			basic_data = json.load(file)

# 		if not isinstance(basic_data, dict):
# 			raise json.JSONDecodeError("Invalid save format ", "", 0)

# 	except (json.JSONDecodeError, FileNotFoundError):
# 		basic_data = {}
# 		with savefile_path.open('w', encoding='utf-8') as file:
# 			json.dump(basic_data, file, indent=4)


# #checks for basic functionality
# def on_start_checks():
# 	check_dialogue()
# 	check_save()


#on_start_checks()# --------------------------------------------------Call for debug





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
	with savefile_path.open('w', encoding='utf-8') as file:
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


