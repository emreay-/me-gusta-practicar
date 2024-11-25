"""
We store nouns with their various information and theirenglish translation in a JSON file.
We curate this information using the AI Backend where we enter a prompt
with what we need for a given noun. We automate this with this script using 
a list of nouns we store as a text. This script will find the new nouns in the 
list and fetch their information from the AI Backend and aggregate the JSON file. 
"""

import json
from typing import List, Optional, Dict

from ai_backend import AIBackend
from utils import dump_json_to_file

from me_gusta_practicar.core.util import load_nouns_set, load_nouns_json, path_to_nouns, remove_article_and_make_lower

def _get_prompt(noun):
    return """
I want to create a json structure for Spanish nouns as below:

{
    "id": 0,
    "in_spanish": "la cocina",
    "in_english": "kitchen",
    "género": "femenino"
}

It is important to check that the noun is masculine or feminine. For instance cocina is feminine.

Please curate this structure for noun """ + noun

def _get_noun_info(ai_backend: AIBackend, noun: str) -> Optional[str]:
    return ai_backend.ask(_get_prompt(noun))


def _has_entity(data: Dict, entity: str) -> bool:
    return entity in data

def _parse_noun_info(info: str) -> Optional[Dict]:
    data = json.loads(info)
    if all([_has_entity(data, i) for i in ["in_spanish", "in_english", "género"]]):
        return data
    return None

def _post_process_curated_nouns(nouns: Dict) -> List[Dict]:
    name_to_noun = {remove_article_and_make_lower(i["in_spanish"]): i for i in nouns}
    res = []

    for i, name in enumerate(sorted(name_to_noun.keys())):
        noun = name_to_noun[name]
        noun["in_spanish"] = noun["in_spanish"].lower()
        noun["id"] = i
        res.append(noun)
    
    return res

def update_nouns_database():
    curated_nouns = load_nouns_json()
    new_nouns = load_nouns_set().difference(set(remove_article_and_make_lower(i["in_spanish"]) for i in curated_nouns))

    print(f"There are {len(new_nouns)} new words to be added to assets")

    ai_backend = AIBackend()

    for i, noun in enumerate(new_nouns):
        try:
            print(f"{i+1}/{len(new_nouns)}: {noun}")
            noun_info = _get_noun_info(ai_backend, noun)
            
            if not noun_info:
                print(f"Unable to fetch info for noun {noun}, maybe try again later")
                continue
            
            parsed_info = _parse_noun_info(noun_info)
            if not parsed_info:
                print(f"Unable to parse noun info for {noun}, potentially missing fields: {noun_info}")
            
            curated_nouns.append(parsed_info)

        except Exception as e:
            print(f"Error occured for noun {noun}: {e}")
    
    dump_json_to_file(_post_process_curated_nouns(curated_nouns), path_to_nouns())

if __name__ == "__main__":
    update_nouns_database()
