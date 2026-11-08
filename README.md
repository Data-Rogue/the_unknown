![The_unknown logo](assets/the_unknown_banner.svg)

## The_Unknown


The_Unknown is an open-source Python terminal narrative engine and interactive fiction framework.

Create branching stories, dialogue driven adventures, mystery games, visual novel style experiences, or entirely custom text-based projects using simple JSON narrative files.

The project includes a starter narrative called **Origin**, but the engine is designed to support entirely custom narratives without modifying the core Python code.

## Active Development
> [!Note]
> This engine is currently in early Alpha development. Removed features and breaking changes are to be expected. Want to help us improve the engine? See [Development](#development)

Current progress:

- [x] Active story loop is working
- [ ] Stories, savefiles and plugins should be in a separate folder https://github.com/Data-Rogue/the_unknown/issues/1
- [ ] More cool stuff soon...


## Features
  
  - Create **branching narratives** using **simple JSON** files with ***minimal programming knowledge***

  - **Dynamic Interactions**: Player choices influence story progression, dialogue, and narrative outcomes

  - **Persistent Progress**: Quickly jump back into stories with ***saves***!



## Save System and File Creation

To ensure your privacy and security, this program follows a strict file-access policy.

  **Standard**: The engine stores save files in each story's save directory. If a valid save is found for the current narrative, progress can be loaded.

  **File Creation**: If no save file or directory exists, the engine will automatically create the required files and folders.

## Prerequisites
Before installing, ensure you have the following installed on your system
- **Python 3.12.3 and up** (Recommended)
- **Git** (To clone the repository)

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
python3 the_unknown.py
```

## Story writing
Want to see how you can make your own story? See [story_writing.md](development/story_writing.md) for examples and explanations.
 > Prefer an GUI editor? Open a Pull Request and tell us what you would like! If we have enough requests, development may start on The_Unknown_Editor!

## Development
We're thrilled you want to help us improve the engine! 
Please feel free to open a pull request!
> [!IMPORTANT]
> With the rise of AI agents and coding assistants, some may worry about the quality of the code generated. This project is **Human first**, with AI code last. Please **refrain from using substantial amounts of AI generated code.** Small amounts like revising the README or fixing a **small bug** will be accepted. We know everyone has the right to choose how they code, but **please follow this outline when contributing to this project.**  Thank you!
<!-- Please first read the [Code of Conduct]() and [...] -->

## Privacy Disclaimer

This project only reads from and writes to its designated save directory. It does not modify unrelated files on your system or transmit data externally.
You are encouraged to review the source code to verify its behavior firsthand.

## License
This project is licensed under the [MIT License](LICENSE)

***Created by Hazmat Harry***

```Text
      ___    ___     ___    ___  _____    ,
     /  /   /  /    |   |  |   |/ ____\  /B
    /  /___/  /     |   |__|   | | n n |//
   /__ ___ __/      B    __    | |_____|/
   \  \   \  \      |   |  |   | o  U o|      /|/|
    \__\   \__\     |   |  |   |   ____|-_-_-/ | |
    /__/   /__/    /_____\/_____\______________|_|
```





