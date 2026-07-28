import os
import subprocess
import sys

def commands(cmd = "",):
    """
    Command module for terminal. (e.g. runs commands)

    cmd = command
    """
    pass



def clear_terminal():#It uh... clear the terminal. Yeah.
	if sys.platform.startswith("win"):#For future, for platform specific things
		subprocess.run(["cls"], shell=True, check=False)
	else:
		subprocess.run(["clear"], check=False)
