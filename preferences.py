import json

def load_config():
    """
    Loads cofig.json or creates config.json if not exist.
    """

    try:
        with open('config.json', 'r') as f:
            config = json.load(f)
    except FileNotFoundError:
        config = {"THEME": "dark"}
    return config


def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f)

def get_theme():
    config = load_config()
    return config["THEME"]

def set_theme(theme):
    config = load_config()
    config["THEME"] = theme
    save_config(config)
