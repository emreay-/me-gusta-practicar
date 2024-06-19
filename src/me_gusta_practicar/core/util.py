import json
from importlib import resources


def get_asset_path(filename: str):
    with resources.path('assets', filename) as path:
        return str(path)

def load_json_asset(filename: str):
    with resources.path('assets', filename) as path:
        return json.load(path.open(encoding="utf-8"))

def path_to_verbs():
    return get_asset_path("verbs.json")

def load_verbs_json():
    return load_json_asset("verbs.json")
