import json
from engine.core import text_effects
from engine import commands
import time

#make json parser to extract data into commands.


#Take in a dictionary and recursively search for nodes and input.
#It must be light on resources, and fast for input. Parsing data
#chunk-by-chunk is not that efficient. It does for now, but keep
#that in mind.

engine_defaults: dict = {
    "effect": "regular",
    "speed": 0.04,
    "newline": 1,
    "pause": 1
}


current_node = ""

resume = False #Temp var until resume game or something is working

default_settings: dict = {}



def resume_game(save):
    global current_node, resume

    if save["resume_node"]:
        current_node = save["resume_node"]
        resume = True
        print(current_node)#HACK: FUTURE: Use the continue dialogue.
    else:
        current_node = "start"
        resume = False
        print(current_node)


def get_story(data):#, save#NOTE Old argument
    global current_node, default_settings

    if not resume:
        current_node = "start"

    node = data["nodes"][current_node]

    if get_default_settings(data):
        default_settings = get_default_settings(data)
    else:
        default_settings = engine_defaults.copy()

    parse_node(node)

    

def get_metadata(data) -> dict:
    return data["metadata"]

def get_default_settings(data) -> dict:
    return data["default_settings"]
        

def parse_node(node):


    parsed = {
        "settings": default_settings.copy(),
        "text": None,
        "choices": None,
        "next": None
    }
    node_settings = default_settings.copy()

    for key, value in node.items():
        match key:
            
            case "effect" | "speed" | "newline" | "pause":
                parsed["settings"][key] = value

            case "text":
                parsed["text"] = value

            case "choices":
                parsed["choices"] = value

            case "next":#if no choices node. make a check
                parsed["next"] = value

            case _:
                print(f"Unknown command: {key}")

    return parsed


def execute_node(node):

    parsed = parse_node(node)

    if parsed["text"] is not None:
        handle_text(parsed["text"], parsed["settings"])

    if parsed["choices"] is not None:
        handle_choices(parsed["choices"])

    if parsed["next"] is not None:
        pass#TODO: Add logic to switch nodes


        
def handle_text(value, node_settings):
    #print("Text: ", value, " ", node_settings)
    match node_settings["settings"]["effect"]:
        case "regular":
            text_effects.typewriter_text(
                value,
                speed = node_settings["speed"],
                speed_random = 0,
                newline_amount = node_settings["newline"],
                pause_time = node_settings["pause"]

            )

        
    

def handle_choices(value):
    print("Choices: ", value)#Needs to change current node to the next once selected.



def parse_data(data, save):
    #get_metadata(data)
    #resume_game(save)
    get_story(data)
    