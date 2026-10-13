from engine.core import save_system
from engine.core import text_effects
from engine import commands
from engine import settings
import sys


boot_messages: list = [
    "Oi! time to initialize...",
    "Initializing...",
    "Working on it..."
]

boot_message: str = f"     The_unknown\n\n{boot_messages[0]}"

def choose_story():
    save_system.get_stories()


def start_boot():
    commands.clear_terminal()
    text_effects.typewriter_text(boot_message, .04, 0, 1)

    #Try and initialize engine, unless error
    try:
        settings.init_settings()
        
    except (OSError, ValueError) as error:
        commands.clear_terminal()

        print(f"Initialization failed\n\nError: {error}")
        input("Press Enter key to exit")
        sys.exit("Exiting... ")

    commands.clear_terminal()

    title_screen()


def title_screen():
    print(title_ascii)
    print("Version 0.1.0-alpha")
    print("Created by Hazmat Harry")
    print("\n")
    
    select_option()


def select_option(print_options: bool = True):
    if print_options:
        print("""1: Start\n2: Install Story\n3: Manage Stories\n4: Settings\n5: Exit\n""")

    user_input = input("Select: ")

    if user_input.lower() == "exit":
         sys.exit("Exiting... ")

    if user_input.lower() == "dev" or "debug":
        pass#Make dev mode print out debugging info, or even a template for what to print! (Future)

    try:
        check_num = int(user_input)
        
        match check_num:

            case 1:
                choose_story()#start
            case 2:
                pass #install stories from github
                #Basically grabs available stories from : GitHub, Local file, URL(safety warning), back (Go back to title screen)
            case 3:
                pass #manage stories: delete, ect.
            case 4:
                settings.settings_screen() #settings
                #Perhaps a different title screen option:
                #
                #The_Unknown
                #_________________
                #1..2..3..ect
            case 5:
                sys.exit("Exiting... ")#Exit lol
            case _:
                text_effects.typewriter_text("Error. Please use numbers, or 'Exit'", 0.01, 0, 2, 0)
                select_option(False)
                
    except ValueError:
        text_effects.typewriter_text("Error. Please use numbers, or 'Exit'", 0.01, 0, 2, 0)
        select_option(False)
    



title_ascii = r"""
   ###.####      ###                                                ++++               
    #########    ###                                              +++++++++++          
       ####      ###  #        ######.                          ++++++++++++++         
       ####      ##########  ###+ . -##                              ...--++++         
       #### ###  ##     ###  ###########                     ++++++++++++++++++        
       #######  ###     ###  ####    #                   +++++++++++++++++++++++++     
       ####     ###     ###   #########    ##########-                                 
                                                           +  ++++  +++++++   +        
                                                            ++               +         
                                                                                       
           ##                    ###                                                   
   ##      ##             ##    ##-                                                    
   ##      ##             ##   ##                         ##       ###                 
   ##      ##  ########   ######    ##########   ######   ###  ##  ### ########+       
   ##      ##- ####  #### ###.###    ###   #### ###.##### ### #### ### ###    ###      
   ###     ### ###    ### ##   ###   ###    ### #.     ##  ####  ##### ###    ###      
   ###    #### ###    ### ##    ###  ###    ### ##     ##  ####  ##### ###    ###      
    #########  ###    ##  ##     ##  ##-    ##   #######   ###    ###  ###    #  
"""
#Created with Image to ASCII Art! Thanks! 
#https://www.asciiart.eu/image-to-ascii