import json
from typing import Set
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

def load_verbs_set() -> Set[str]:
    verbs = []
    with open(get_asset_path("verbs_list.txt"), "r", encoding="utf-8") as file:
        for line in file:
            verbs.append(line.strip())
    return set(verbs)

def remove_article_and_make_lower(noun):
    noun = noun.lower()
    tokens = noun.split(" ")
    if tokens[0] in ["el", "la", "los", "las"]:
        return " ".join(tokens[1:])
    return noun

def path_to_nouns():
    return get_asset_path("nouns.json")

def load_nouns_json():
    return load_json_asset("nouns.json")

def load_nouns_set() -> Set[str]:
    nouns = []
    with open(get_asset_path("nouns_list.txt"), "r", encoding="utf-8") as file:
        for line in file:
            nouns.append(remove_article_and_make_lower(line.strip()))
    return set(nouns)

def path_to_prepositons():
    return get_asset_path("prepositions.json")

def load_prepositions_json():
    return load_json_asset("prepositions.json")
