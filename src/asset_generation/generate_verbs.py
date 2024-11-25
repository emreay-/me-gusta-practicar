"""
We store verbs with their various information such as their conjugations, 
english translation, whether they are regualar and so on in a JSON file.
We curate this information using the AI Backend where we enter a prompt
with what we need for a given verb. We automate this with this script using 
a list of verbs we store as a text. This script will find the new verbs in the 
list and fetch their information from the AI Backend and aggregate the JSON file. 
"""

import json
from typing import List, Optional, Dict

from ai_backend import AIBackend
from utils import dump_json_to_file

from me_gusta_practicar.core.util import load_verbs_set, load_verbs_json, path_to_verbs

def _get_prompt(verb):
    return """
I want to create a json structure for Spanish verbs as below:

{
    "id": 0,
    "in_spanish": "abandonar",
    "in_english": "to abandon",
    "is_regular": true,
    "is_reflexive": false,
    "conjugation": {
        "indicativo": {
            "present": ["abandono", "abandonas", "abandona", "abandonamos", "abandonáis", "abandonan"],
            "preterite": ["abandoné", "abandonaste", "abandonó", "abandonamos", "abandonasteis", "abandonaron"],
            "imperfect": ["abandonaba", "abandonabas", "abandonaba", "abandonábamos", "abandonabais", "abandonaban"],
            "future": ["abandonaré", "abandonarás", "abandonará", "abandonaremos", "abandonaréis", "abandonarán"],
            "conditional": ["abandonaría", "abandonarías", "abandonaría", "abandonaríamos", "abandonaríais", "abandonarían"]
        },
        "subjuntivo": {
            "present": ["abandone", "abandones", "abandone", "abandonemos", "abandonéis", "abandonen"],
            "imperfect": ["abandonara", "abandonaras", "abandonara", "abandonáramos", "abandonarais", "abandonaran"],
            "future": ["abandonare", "abandonares", "abandonare", "abandonáremos", "abandonareis", "abandonaren"]
        },
        "imperativo": {
            "affirmative": ["-", "abandona", "abandone", "abandonemos", "abandonad", "abandonen"],
            "negative": ["-", "no abandones", "no abandone", "no abandonemos", "no abandonéis", "no abandonen"]
        }
    }
}

It is important to check that the verb is regular or not as if it is in reflexive form. For instance hacer is irregular because it is hago for yo.

Please curate this structure for verb """ + verb

def _get_verb_info(ai_backend: AIBackend, verb: str) -> Optional[str]:
    return ai_backend.ask(_get_prompt(verb))


def _has_entity(data: Dict, entity: str) -> bool:
    return entity in data

def _parse_verb_info(info: str) -> Optional[Dict]:
    data = json.loads(info)
    if all([_has_entity(data, i) for i in ["in_spanish", "in_english", "is_regular", "is_reflexive", "conjugation"]]):
        return data
    return None

def _post_process_curated_verbs(verbs: Dict) -> List[Dict]:
    name_to_verb = {i["in_spanish"]: i for i in verbs}
    res = []

    for i, name in enumerate(sorted(name_to_verb.keys())):
        verb = name_to_verb[name]
        verb["id"] = i
        res.append(verb)
    
    return res


def update_verbs_database():
    curated_verbs = load_verbs_json()
    new_verbs = load_verbs_set().difference(set(i["in_spanish"] for i in curated_verbs))

    print(f"There are {len(new_verbs)} new words to be added to assets")

    ai_backend = AIBackend()

    for i, verb in enumerate(new_verbs):
        try:
            print(f"{i+1}/{len(new_verbs)}: {verb}")
            verb_info = _get_verb_info(ai_backend, verb)
            
            if not verb_info:
                print(f"Unable to fetch info for verb {verb}, maybe try again later")
                continue
            
            parsed_info = _parse_verb_info(verb_info)
            if not parsed_info:
                print(f"Unable to parse verb info for {verb}, potentially missing fields: {verb_info}")
            
            curated_verbs.append(parsed_info)

        except Exception as e:
            print(f"Error occured for verb {verb}: {e}")
    
    dump_json_to_file(_post_process_curated_verbs(curated_verbs), path_to_verbs())

if __name__ == "__main__":
    update_verbs_database()
