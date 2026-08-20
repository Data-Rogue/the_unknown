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
    
    for key, value in data["nodes"][current_node].items():##Key = 'text,' 'choices,' ect.
        print(f"{key} with value of {value}")

        
        

def parse_node(node):

    for key, value in node.items():
        match key:
            case "effect":
                handle_effect(value)

            case "speed":
                handle_speed(value)

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
    print("Effect: ", value)

def handle_speed(value):
    print("Speed: ", value)

def handle_newline(value):
    print("Newline: ", value)

def handle_pause(value):
    print("Pause: ", value)

def handle_text(value):
    print("Text: ", value)

def handle_choices(value):
    print("Choices: ", value)



def parse_data(data, save):
    #get_metadata(data)
    resume_game(save)
    