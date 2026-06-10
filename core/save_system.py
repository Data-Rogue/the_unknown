from pathlib import Path
import json
import sys


basic_data = {} #formerly dataaa
dialogue = []
savefile_path = Path("saves") / "save1.json" 
dialogue_path = Path("content") / "narrative.json"
restricted_mode = False








#Change dialogue to be more lighthearted.
#Like "You... chose that? Interesting. I wasn't expecting that."

















# print(dialogue_path)
# print(dialogue_path.resolve())
# print(dialogue_path.exists())

def check_dialogue():
	global dialogue

	if not dialogue_path.exists():
		sys.exit(f"Error: {dialogue_path} not found. Exiting program... ")

	try:
		with dialogue_path.open('r', encoding='utf-8') as file:
			dialogue = json.load(file)
	except json.JSONDecodeError:
		sys.exit(f"Error: {dialogue_path} is empty or contains invalid JSON.")
	


def check_save():
	global basic_data

	if not savefile_path.exists():
		savefile_path.parent.mkdir(parents=True, exist_ok=True)

		with savefile_path.open('w', encoding='utf-8') as file:
			json.dump({}, file, indent=4)

	try:
		with savefile_path.open('r', encoding='utf-8') as file:
			basic_data = json.load(file)

		if not isinstance(basic_data, dict):
			raise json.JSONDecodeError("Invalid save format ", "", 0)

	except (json.JSONDecodeError, FileNotFoundError):
		basic_data = {}
		with savefile_path.open('w', encoding='utf-8') as file:
			json.dump(basic_data, file, indent=4)


#checks for basic functionality
def on_start_checks():
	check_dialogue()
	check_save()


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






def times_played(command = "r"):
	"""
	Function to increment times played. 
	
	Parameters:
		command = r =  read, w = write, anything else throws an error.
	"""
	match command:
		case "r":
			pass
		case "w":
			pass
		case _:
			print("Failure to read or write. Input command not known.")










##Saves data to json





