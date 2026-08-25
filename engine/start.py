from engine.core import save_system
from engine.core import text_effects
from engine import commands
from engine import settings
import sys



def choose_story():
    save_system.get_stories()


def start_boot():
    commands.clear_terminal()
    text_effects.typewriter_text("Initializing... ", .04, 0, 1)

    settings.init_settings()
    commands.clear_terminal()

    title_screen()


def title_screen():
    print(title_ascii)
    print("Version 0.2.0")
    print("Created by Hazmat Harry")
    print("\n\n")
    
    select_option()


def select_option(print_options: bool = True):
    if print_options:
        print("1: Start          2: Settings\n\n")
    user_input = input("Select: ")

    if user_input.lower() == "exit":
         sys.exit("Exiting... ")

    try:
        check_num = int(user_input)
        
        match check_num:

            case 1:
                choose_story()
            case 2:
                pass #settings
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