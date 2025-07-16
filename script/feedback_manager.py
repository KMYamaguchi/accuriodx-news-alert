import json
import os
import yaml

def load_feedback():
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    path = config["feedback_file"]
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_feedback(feedback):
    with open("config/config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    with open(config["feedback_file"], "w", encoding="utf-8") as f:
        json.dump(feedback, f, ensure_ascii=False, indent=2)
