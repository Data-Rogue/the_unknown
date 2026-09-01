## Map Key
- [File placement](#file-placement)
- [Story writing](#story-writing)


## File placement
Each story **must be placed in a folder named after the story's title**, such as the following example: 
```Text
    origin(folder)
        |
        |_story.json

```

You can have _multiple stories_ in the_unknown, but **each must be in its own separate folder**. This ensures organization, and enables support for future features. 
The folder containing all the stories is called "narratives". The path to this folder as of now is `content/narratives`.

## Story writing

After you have completed the steps above (see [File placement](#file-placement)), create and open `story.json`.
Then add 2 curly brackets like this:
```JSON
{

}
```

Before writing the story content, add the following cells:
- Metadata
- Default settings

Here's what these cells look like:
```JSON
{
  "metadata": {
    "title": "Origin",
    "author": "Hazmat Harry",
    "id": "origin",
    "version": "0.1.0"
  },
  
  "default_settings": {
    "effect": "regular",
    "speed": 0.04,
    "newline": 1,
    "pause": 3
  }
}
```
A few notes on these cells; 
 - Indentation is important here. Be mindful of the row your working on
 - The 'id' should be a lowercase, unique identifier for the story. It is recommended that the ID match the title when possible, with spaces and special characters removed or replaced
 - The 'default_settings' will be used for printing if each node doesn't specify its own. More on this [later](#default-settings)


## Default settings
These settings will be used throughout the story if each node doesn't specify its own parameter. (If there are no default settings specified it will fall back on the hard-coded engine defaults.)
For example, given the defaults above, the `"speed"` argument has a value of `0.04`. This can be overwritten by simply specifying `"speed": 0.1` in a given node;

```JSON
"intro_p1": {
  "speed": 0.06,
  "text": "W-who's there??",
  "commands": [
    {
      "command": "get_name"
    }
],
  "next": "intro_p2"
}
```

## Nodes
Nodes are the heart of the story. They orchestrate just about everything, so having proper structure will make everything flow smoothly.

### Start node
---
Besides the special nodes like `"metadata"` and `"default_settings"`, we have the `"start"` node. This acts like the doorway into the story that allows the user to enter into the world you've created!

Take a look at the following example of a start node:
```JSON
"start": {
      "interlude": {
        "clear_screen": true,
        "pause": 5
      },
      "text": "H-hello?",
      "choices": [
        {
          "text": "Who's there?",
          "set": {
            "interested": true
          },
          "next": "intro_p1"
        },
        {
          "text": "Say nothing.",
          "set": {
            "interested": false
          },
          "next": "intro_sus_1"
        }
      ]
    }
```

You don't have to understand everything that's going on here, but look at the way it's structured;
```Text
start <- (Name of node)
  |_interlude <- (Special arguments to execute before the other cells)
  | |_clear_screen: true
  | |_pause: 5
  |
  |_text <- (Text to print or ask user)
  |
  |_choices
    |_Choice 1: 
    | |
    | |_text "Who's there?" <- (This is text that will be printed as 
    | |                         an option to choose from)
    | |
    | |_set <- (Tells the engine to assign a value to a variable)
    |   |
    |   |_interested: true <- (Assigns the value 'true' to 'interested')
    |   |
    |   |_next: "intro_p1" <- (The name of the next node to go to if
    |                          chosen)
    |
    |_Choice 2: 
    | |
    | |_text "Say nothing." <- (This is text that will be printed as 
    | |                         an option to choose from)
    | |
    | |_set <- (Tells the engine to assign a value to a variable)
    |   |
    |   |_interested: false <- (Assigns the value 'false' to
    |   |                       'interested')
    |   |
    |   |_next: "intro_sus_1" <- (The name of the next node to go to if
    |                             chosen) 
```

Currently, the order of the cells does not matter[^1], but by maintaining clear structure we benefit not only the readability but also improve debugging. 

**Interlude**
> You may be wondering about that weird-looking `"interlude"` cell. 
> This cell tells the engine to execute these instructions first before processing the rest of the node. As a result, these arguments will run first when the node loads.

**Cells & Nodes**
> In case you're wondering what the difference is between a "cell" and a "node": **A cell is a named section containing settings or arguments for a specific part of a node**. **A node is a collection of cells that describes a point in the story**.


[^1]: The engine processes certain cells according to their defined behavior rather than their position in the JSON file. This means cells may be arranged for readability without changing the node's behavior.