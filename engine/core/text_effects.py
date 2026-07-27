import string
import random
import time
import os
import random


#This file contains all the text effects for the engine.

def clear_terminal():
	os.system('clear') ##Replace with subprocess


def glitch_text(text: str, glitch_chance: float = 0.08):
	glitch_chars = string.ascii_letters + string.digits + "#$%&@!?\\/|"

	glitched = ""
	for char in text:
		if char != " " and random.random() < glitch_chance:
			glitched += random.choice(glitch_chars)
		else:
			glitched += char

	return glitched


def typewriter_glitch(text: str, delay: float = 0.05, glitch_chance: float = 0.08, burst_chance: float = 0.15, newline: bool = True, newline_amount: int = 1):
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



def typewriter_text(
		text: str, 
		speed: float = 0.5,
		speed_random: float = 0,
		newline_amount: int = 1, 
		pause_time: float = 0
		):
	"""
	text: What you want to print to the terminal.

	speed: How much time before the next character is printed.

	speed_random: Randomize amount of pause time before next character is printed. (Affects 'speed')

	newline_amount: How many indents to leave for the next sentence. If equal to 0, no indentation.

	pause_time: how long to sleep or pause the terminal before continuing.
	"""

	if speed_random > 0:# Check if speed_random is used.
		for char in text:
			print(char, end="", flush=True)

			#Does not account for negative numbers.
			#I tried subtracting the speed_random from speed
			#and got a negative time error for time.sleep()
				
			rand_num = random.uniform(speed, speed + speed_random) # HACK: Not ready. Must account for negative numbers. Read comment above.
		
			time.sleep(rand_num)
	else:
		for char in text:
			print(char, end="", flush=True)
			time.sleep(speed)

	if newline_amount > 0:
		for i in range(newline_amount):
			print() #newline

	if pause_time > 0:
		time.sleep(pause_time)


def delete_typewriter_text(length: int = 1, speed: float = 0.05, pause_time: float = 0):
	"""
	Delete text with a typewriter effect.

	length: amount of characters you want to delete.

	speed: delay before the next character is deleted.

	pause_time: how long to sleep or pause the terminal before continuing.
	"""
	for _ in range(length + 1): # TODO:  +1 accounts for cursor whitespace. Not tested yet.
		print("\b \b", end="", flush=True)
		time.sleep(speed)
	if pause_time > 0:
		time.sleep(pause_time)




def progress_bar(total: int = 30, delay: float = 0.05):
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
