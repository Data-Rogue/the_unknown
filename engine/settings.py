from pathlib import Path
import json
import sys
from engine import commands
from engine import start

settings_path = Path("engine/config.json")

loaded_settings = {}


stock_settings = {
    "plugins": {},
    "use_sound": False,
    "audio engine": "unsupported",
    "title_screen": "default",
    "default_dialogue_path": "content/narratives",
    "user_dialogue_path": ""
}


def init_settings():
    check_settings()



def scan_for_plugins():
    pass


def check_settings():
    """
    Checks if settings file exists, if true
    then read, else create and load.
    """
    global loaded_settings

    if settings_path.is_file():
        with settings_path.open('r', encoding='utf-8') as s:
            loaded_settings = json.load(s)

    else:
        write_to_settings("None", "None", True)
        # with settings_path.open('w', encoding='utf-8') as f:
        #     json.dump(stock_settings, f, indent=4)
        #     loaded_settings = stock_settings
        #     print(loaded_settings)

def get_setting(key: str = ""):
    return loaded_settings[key]


def write_to_settings(
        variable_name: str = "comment", 
        save_value: bool | int | str | float | dict = "Cool comment bro.",
        write_stock: bool = False
        ):#TODO: Accommodate for nested settings
    
    global loaded_settings

    if write_stock:
        loaded_settings = stock_settings.copy()
    else:
        loaded_settings[variable_name] = save_value

    with settings_path.open('w', encoding='utf-8') as f:
        json.dump(loaded_settings, f, indent=4)


def get_narrative_path():
    if len(get_setting("user_dialogue_path")) > 2:
        return get_setting("user_dialogue_path")
    else:
        return get_setting("default_dialogue_path")

def edit_narrative_path():
    commands.clear_terminal()
    print("+----------------------------+\n|  Configure Narrative Path  |\n+----------------------------+\n\n")
    print(f"Current Narrative path: '{get_narrative_path()}'")
    input("New Path: ")
    

def settings_screen():
    commands.clear_terminal()
    print("""+------------+\n|   V0.2.0   |\n+------------+\n\n""")
    # print("+------------+")
    # print("|   V0.2.0   |")
    # print("+------------+\n\n")
    print(f"""
1: Change title-screen
2: Use sound: {get_setting("use_sound")} - (toggaleable)
3: Configure narrative path: {get_narrative_path()}
4: Back
5: Exit\n""")

    input = commands.get_input("Select: ", int, True)

    match input:
        case 1:# Title screen type
            pass
        case 2:# Sound
            flip = not get_setting("use_sound")
            write_to_settings("use_sound", flip, False)

            settings_screen()
            # Currently unsupported
        case 3:# Configure narrative path
            edit_narrative_path()
        case 4:# Back
            start.title_screen()
        case 5:# Exit
            sys.exit("Exiting... ")

