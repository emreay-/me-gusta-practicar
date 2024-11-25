import json
from typing import List, Dict
from enum import Enum

from me_gusta_practicar.core.word import Word
from me_gusta_practicar.core.util import load_nouns_json

class Gender(Enum):
    Masculine = 1
    Feminine = 2

class Noun(Word):
    def __init__(self, in_spanish: str, in_english: str, gender: Gender):
        super().__init__(in_spanish, in_english, "noun")
        self.gender = gender

    @staticmethod
    def from_json(input: json) -> 'Noun':
        return Noun(
            in_spanish=input["in_spanish"],
            in_english=input["in_english"],
            gender=Gender.Masculine if input["género"].lower() == "masculine" else Gender.Feminine,
        )

    def __repr__(self):
        return f"Noun(id={self.id}, in_spanish='{self.in_spanish}', in_english='{self.in_english}', género={self.gender}"

def load_nouns() -> List[Noun]:
    nouns = []
    for noun in load_nouns_json():
        nouns.append(Noun.from_json(noun))
    return nouns
