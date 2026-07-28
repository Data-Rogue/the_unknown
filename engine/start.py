from engine.core import save_system
from engine.core import text_effects
from engine import commands
##read narratives and choose, when load saves by passing which story to start.


def choose_story():
    save_system.get_stories()


def start_boot():
    commands.clear_terminal()
    text_effects.typewriter_text("Initializing... ", .04, 0, 1)

    text_effects.delete_typewriter_text(16, .01, 0.1)
    choose_story()


# def start():
#     pass