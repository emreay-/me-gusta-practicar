import json
from typing import List, Dict
from enum import Enum

from me_gusta_practicar.core.word import Word
from me_gusta_practicar.core.util import load_nouns_json

class Gender(Enum):
    Masculine = 1
    Feminine = 2

class Noun(Word):
    def __init__(self, id: int, name: str, EN: str, gender: Gender):
        super().__init__(name, EN)
        self.id = id
        self.gender = gender

    @staticmethod
    def from_json(input: json) -> 'Noun':
        return Noun(
            id=input["id"],
            name=input["name"],
            EN=input["EN"],
            gender=Gender.Masculine if input["género"].lower() == "masculine" else Gender.Feminine,
        )

    def __repr__(self):
        return f"Noun(id={self.id}, name='{self.name}', EN='{self.EN}', género={self.gender}"

def load_nouns() -> List[Noun]:
    nouns = []
    for noun in load_nouns_json():
        nouns.append(Noun.from_json(noun))
    return nouns
