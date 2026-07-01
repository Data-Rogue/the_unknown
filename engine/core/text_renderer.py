import json
from engine.core import text_effects


#make json parser to extract data into commands.


#Take in a dictionary and recursively search for nodes and input.
#It must be light on resources, and fast for input. Parsing data
#chunk-by-chunk is not that efficient. It does for now, but keep
#that in mind.

current_node = ""

def parse_data(data):
    get_metadata(data)



def get_metadata(data):
    for block in data:
        match block:
            case "metadata":
                pass
            case "default_save":
                pass


def get_story(data, save):
    global current_node

    for block in data["nodes"]:

        if block == "start":
            current_node = "start"##-------------remake to check if a save is selected.
            print(current_node)
        else:
            print("pass")
            pass
