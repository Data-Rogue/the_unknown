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
		prompt: str = "Select: ", 
		return_type: type[bool] | type[int] | type[str] | type[float] = int, 
		# text_on_error: str = "Please use numbers: ", 
		allow_exit: bool = True
		):
    """
    Get input from user, set the wanted return type, and ability to exit the program
    
    :param prompt: Text to ask user for input
    :type prompt: str
    :param return_type: Specify what value type you want the prompt to return 
    :type return_type: bool, int, str, float
    :param allow_exit: Allow the user to type 'exit' to exit the program
    :type allow_exit: bool
    """

    check = None
    check = input(f"{prompt}")
    print("")

    if allow_exit:
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
             
        
