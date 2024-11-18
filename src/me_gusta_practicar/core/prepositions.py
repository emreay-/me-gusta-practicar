from typing import List

from me_gusta_practicar.core.word import Word
from me_gusta_practicar.core.util import load_prepositions_json

def load_prepositions() -> List[Word]:
    preps = []
    for p in load_prepositions_json():
        preps.append(Word(name=p["name"], EN=p["EN"]))
    return preps
