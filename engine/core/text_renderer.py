import json
from engine.core import text_effects
from engine import commands
import time

#make json parser to extract data into commands.


#Take in a dictionary and recursively search for nodes and input.
#It must be light on resources, and fast for input. Parsing data
#chunk-by-chunk is not that efficient. It does for now, but keep
#that in mind.

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

    default_settings = get_default_settings(data)

    parse_node(node)

    

def get_metadata(data) -> dict:
    return data["metadata"]

def get_default_settings(data) -> dict:
    return data["default_settings"]
        

def parse_node(node):

    current_settings = default_settings

    for key, value in node.items():
        match key:
            case "effect":
                try:
                    current_settings["effect"] = handle_effect(value)
                except None:
                    pass

            case "speed":
                try:
                    current_settings["speed"] = handle_speed(value)
                except:
                    None

            case "newline":
                handle_newline(value)

            case "pause":
                handle_pause(value)

            case "text":
                handle_text(value)

            case "choices":
                handle_choices(value)

            case _:
                print(f"Unknown command: {key}") 


        
def handle_effect(value):
    if value:
        return value #pretty useless right now, but here for the future.
    else:
        return None
    #print("Effect: ", value)

def handle_speed(value):
    ##DO SOMETHING HERE!
    print("Speed: ", value)

def handle_newline(value):
    print("Newline: ", value)

def handle_pause(value):
    print("Pause: ", value)

def handle_text(value):
    print("Text: ", value)

def handle_choices(value):
    print("Choices: ", value)#Needs to change current node to the next once selected.



def parse_data(data, save):
    #get_metadata(data)
    #resume_game(save)
    get_story(data)
    