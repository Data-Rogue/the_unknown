import json
from engine.core import text_effects
from engine import commands

#make json parser to extract data into commands.


#Take in a dictionary and recursively search for nodes and input.
#It must be light on resources, and fast for input. Parsing data
#chunk-by-chunk is not that efficient. It does for now, but keep
#that in mind.

current_node = ""

resume = False #Temp var until resume game or something is working


def get_metadata(data):
    for block in data:
        match block:
            case "metadata":
                pass
            case "default_save":
                pass


def resume_game(save):
    global current_node

    if save["resume_node"]:
        current_node = save["resume_node"]
        print(current_node)
    else:
        current_node = "start"
        print(current_node)


def get_story(data, save):
    global current_node

    if not resume:
        current_node = "start"

    text_effect = None
    
    for key, value in data["nodes"][current_node].items():
        print(f"{key} with value of {value}")
        match key:
            case "effect":
                match value:
                    case "regular":
                        text_effect = text_effects.typewriter_text()
            case "speed":
                pass
            case "newline":
                pass
            case "pause":
                pass
            case "text":
                pass
            case "choices":
                pass

        
        

        
        


def parse_data(data, save):
    #get_metadata(data)
    resume_game(save)
    