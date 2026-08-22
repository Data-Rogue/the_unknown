## Map Key
- [File placement](file-placement)
- [Story writing](story-writing)


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

After you have completed the steps above (see [File placement](file-placement)), create and open `story.json`.
Then add 2 curly brackets like this:
```JSON
{

}
```

Before writing the story, we must add the following cells:
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
  },
}
```
A few notes on these cells; 
 - Indentation is important here. Be mindful of the row your working on
 - The 'id' should be equal to the title but lowercased
 - The 'default_settings' will be used for printing if each node doesn't specify its own. More on this [later](default-settings)


### Default settings
These settings will be used throughout the story if each node doesn't specify it's own parameter.
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

### Nodes
Nodes are the heart of the the story. They orchestrate just about everything, so having proper structure will make everything flow smoothly.

Besides the special nodes like `"metadata"` and `"default_settings"`, we have the `"start"` node. This acts like the doorway into the story that allows the user to enter into the world you've created!

Take a look at the following example of a start node:
```JSON
"start": {
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
  |_text <- (Text to print or ask user)
  |_choices
    |_Choice 1: "Who's there?" <- (This is text that will be printed
    |_Choice 2: "Say nothing." <-  as an option to choose from)
```

This is important because ***the node is read top to bottom.***
So if you put important arguments such as `"effect"`, `"speed"`, `"newline"` and `"pause"` AFTER `"text"`, then those arguments *WON'T* affect the print. Same goes for `"text"`. If you put `"choices"` or `"next"`(If you don't have 'choices' for that node) BEFORE `"text"` this will print just the choices or go to the next node.