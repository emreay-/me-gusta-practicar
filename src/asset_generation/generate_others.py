import json
from typing import List, Optional, Dict

from ai_backend import AIBackend
from utils import dump_json_to_file

from me_gusta_practicar.core.util import load_others_set, load_others_json, path_to_others, remove_article_and_make_lower

def _get_prompt(word):
    return """
I want to create a json structure for various Spanish words as below:

{
    "id": 0,
    "in_spanish": "la cocina",
    "in_english": "kitchen",
    "category": "adjective"
}

You should understand the category of the word, such as word, verb, adjective, adverb, preposition and so on. If a word has multiple
categories (both an word and an adjective) pick the most common used.

Please curate this structure for the word """ + word

def _get_word_info(ai_backend: AIBackend, word: str) -> Optional[str]:
    return ai_backend.ask(_get_prompt(word))


def _has_entity(data: Dict, entity: str) -> bool:
    return entity in data

def _parse_word_info(info: str) -> Optional[Dict]:
    data = json.loads(info)
    if all([_has_entity(data, i) for i in ["in_spanish", "in_english", "category"]]):
        return data
    return None

def _post_process_curated_words(words: Dict) -> List[Dict]:
    name_to_word = {remove_article_and_make_lower(i["in_spanish"]): i for i in words}
    res = []

    for i, name in enumerate(sorted(name_to_word.keys())):
        word = name_to_word[name]
        word["in_spanish"] = word["in_spanish"].lower()
        word["id"] = i
        res.append(word)
    
    return res

def update_others_database():
    curated_words = load_others_json()
    new_words = load_others_set().difference(set(remove_article_and_make_lower(i["in_spanish"]) for i in curated_words))

    print(f"There are {len(new_words)} new words to be added to assets")

    ai_backend = AIBackend()

    for i, word in enumerate(new_words):
        try:
            print(f"{i+1}/{len(new_words)}: {word}")
            word_info = _get_word_info(ai_backend, word)
            
            if not word_info:
                print(f"Unable to fetch info for word {word}, maybe try again later")
                continue
            
            parsed_info = _parse_word_info(word_info)
            if not parsed_info:
                print(f"Unable to parse word info for {word}, potentially missing fields: {word_info}")
            
            curated_words.append(parsed_info)

        except Exception as e:
            print(f"Error occured for word {word}: {e}")
    
    dump_json_to_file(_post_process_curated_words(curated_words), path_to_others())

if __name__ == "__main__":
    update_others_database()
