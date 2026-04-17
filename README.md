## The_Unknown

The_Unknown is a choice-driven Python terminal adventure where your decisions shape the journey. Interact with an enigmatic entity and see if you can navigate the depths of the console.


## Features:

  - Terminal-Based Gameplay: A classic "*text adventure*" style interface, featuring ASCII art.
  
  - Dynamic Interactions: Your input directly *influences* the narrative path.
  
  - Persistent Progress: [(See Save System below)](#save-system-and-restricted-mode).

---

## Save System and Restricted Mode

To ensure your privacy and security, this program follows a strict file-access policy.

  **Standard Mode**: If a valid save file is detected in the local directory, the game will automatically record your progress, allowing you to resume your journey later.

  **Restricted Mode**: If no save file is found, the game will launch in Restricted Mode.

    In this mode, the program will not create new files on your system.
    You can play the full game, but your progress will not be saved after you close the terminal.
---

## Installation & Usage

  1. Clone the repository:
```Bash
git clone https://github.com/Data-Rogue/the_unknown.git
```
  2. Navigate to the folder:
```Bash
cd the_unknown
```

  3. Run the game:
```Bash
python3 main.py
```
---

## Privacy Disclaimer

This project respects your data. The code does not modify, delete, or upload any files from your computer. It only reads/writes to its own specific save file if you have provided one. You are encouraged to inspect the source code yourself to verify its behavior.


***Created by Hazmat Harry***
