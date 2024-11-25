from typing import List

from me_gusta_practicar.core.word import Word
from me_gusta_practicar.core.util import load_prepositions_json

def load_prepositions() -> List[Word]:
    preps = []
    for p in load_prepositions_json():
        preps.append(Word(in_spanish=p["in_spanish"], in_english=p["in_english"], category="preposition"))
    return preps
