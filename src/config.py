import json

def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"scenario": "normal"}

def save_config(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

# Default config
if __name__ == "__main__":
    config = load_config()
    print("Current config:", config)
    config["scenario"] = "focus_meeting"
    save_config(config)
    print("Updated config:", load_config())