from pathlib import Path
import json


settings_path = Path("engine/settings.json")

loaded_settings = {}


stock_settings = {
    "Plugins": {},
    "Audio engine": "Unsupported"
}


def init_settings():
    check_settings()



def scan_for_plugins():
    pass


def check_settings():
    """
    Checks if settings file exists, if true
    then read, else create and load.
    """
    global loaded_settings

    if settings_path.is_file():
        with settings_path.open('r', encoding='utf-8') as s:
            loaded_settings = json.load(s)

    else:
        with settings_path.open('w', encoding='utf-8') as f:
            json.dump(stock_settings, f, indent=4)
            loaded_settings = stock_settings
            print(loaded_settings)
