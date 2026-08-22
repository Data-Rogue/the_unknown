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


Each story must begin with the "start" node.