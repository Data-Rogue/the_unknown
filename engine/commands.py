import os
import subprocess
import sys



def clear_terminal():#It uh... clear the terminal. Yeah.
	if sys.platform.startswith("win"):#For future, for platform specific things
		subprocess.run(["cls"], shell=True, check=False)
	else:
		subprocess.run(["clear"], check=False)


COMMANDS = {
     "clear": clear_terminal()
}

def commands(cmd = "",):
    """
    Command module for terminal. (e.g. runs commands)

    cmd = command
    """
    pass


def sterilize_input(input = None):
	pass

def get_input(
		prompt: str = "Your input: ", 
		return_type = bool, 
		# text_on_error: str = "Please use numbers: ", 
		exit_valid = True
		):

    check = None
    check = input(f"{prompt}")
    print("")

    if exit_valid:
        if check.lower() == "exit":
            sys.exit("Exiting... ")


    if return_type == int:
        try:
            checked_type = int(check)
            return checked_type

        except ValueError:
            print("Error, please use numbers")
            


    if return_type == bool:
        try:
            checked_type = bool(check)
        except ValueError:
            print("Error, please use True/False")
             
        
