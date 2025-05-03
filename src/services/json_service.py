import json
import os

def load_json(file_path: str) -> dict:
    """ Loads JSON file """

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {}
        

def save_json(file_path: str, json_dict: dict) -> None:
    """ Saves JSON file """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w") as f:
        json.dump(json_dict, f, indent=2)
