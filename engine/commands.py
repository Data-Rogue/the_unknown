import os
import subprocess


def commands(cmd = "",):
    """
    Command module for terminal. (e.g. runs commands)

    cmd = command
    """
    pass



def clear_terminal():#It uh... clear the terminal. Yeah.
	if os.name == "nt":
		subprocess.run(["cls"], shell=True, check=False)
	else:
		print("\033[2J\033[H", end="", flush=True)
