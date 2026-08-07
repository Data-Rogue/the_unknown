from engine.core import save_system
from engine.core import text_effects
from engine import commands
from engine import settings
##read narratives and choose, when load saves by passing which story to start.


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
    print("Version 0.1.6")
    print("Created by Hazmat Harry")
    print("\n\n")
    
    select_option()



def select_option():
    print("1: Start          2: Settings\n\n")
    user_input : int = int(input("Select: "))#TODO: Add safety net to catch errors.
    if user_input == 1:
        choose_story()
    elif user_input == 2:
        pass #Settings
    else:
        print("Something went wrong.")




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