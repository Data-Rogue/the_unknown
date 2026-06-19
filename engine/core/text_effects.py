import string
import random
import time
import os



#This file contains all the text effects for the game.

def clear_terminal():
	os.system('clear')


def glitch_text(text, glitch_chance=0.08):
	glitch_chars = string.ascii_letters + string.digits + "#$%&@!?\\/|"

	glitched = ""
	for char in text:
		if char != " " and random.random() < glitch_chance:
			glitched += random.choice(glitch_chars)
		else:
			glitched += char

	return glitched

def typewriter_glitch(text, delay=0.05, glitch_chance=0.08, burst_chance=0.15, newline=True, newline_amount=1):
	for char in text:
		# Random glitch bursts (whole word distortion moment)
		if random.random() < burst_chance:
			corrupted = glitch_text(text, glitch_chance * 2)
			print("\r" + corrupted, end="", flush=True)
			time.sleep(0.05)
			print("\r" + " " * len(corrupted), end="", flush=True)
			print("\r", end="")

		# Normal typing (with occasional char glitch)
		if char != " " and random.random() < glitch_chance:
			print(random.choice("#$%&@!?"), end="", flush=True)
		else:
			print(char, end="", flush=True)

		time.sleep(delay)

	if newline:
			if newline_amount >= 1:
				for i in range(newline_amount):
					print() #newline



def typewriter_text(text, speed=0.5, newline_amount=1, pause_time=0):
	"""
	text: What you want to print to the terminal.

	speed: How much time before the next character is printed.

	newline_amount: How many indents to leave for the next sentence. If equal to 0, no indentation.

	pause_time: how long to sleep or pause the terminal before continuing.
	"""
	for char in text:
		print(char, end="", flush=True)
		time.sleep(speed)
	if newline_amount > 0:
		for i in range(newline_amount):
			print() #newline	
	if pause_time > 0:
		time.sleep(pause_time)



def progress_bar(total=30, delay=0.05):
	for i in range(total + 1):
		percent = int((i / total) * 100)
		bar = "#" * i + "-" * (total - i)
		print(f"\r[{bar}] {percent}%", end="", flush=True)
		time.sleep(delay)
	print()  # newline after done
	

def scanning_bar():
	fake_tasks = [
		"Scanning directories",
		"Indexing files",
		"Reading metadata",
		"Analyzing structure",
		"Checking permissions",
		"Looking deeper",
		"Cross-referencing data"
	]

	total = 30
	for i in range(total + 1):
		percent = int((i / total) * 100)
		bar = "#" * i + "-" * (total - i)
		task = random.choice(fake_tasks)

		print(f"\r[{bar}] {percent}% | {task}...", end="", flush=True)
		time.sleep(random.uniform(0.02, 0.15))

	print()


def file_scan_sequence():
	files = [
		"notes.txt",
		"todo.md",
		"hidden.log",
		"passwords.txt",
		"archive.zip"
	]

	for file in files:
		print(f"\nAccessing: {file}")
		progress_bar(20, 0.02)

		if "pass" in file:
			typewriter_glitch("This one looks important...", 0.04)
