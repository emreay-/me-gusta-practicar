import json
from typing import List, Dict

from me_gusta_practicar.core.word import Word
from me_gusta_practicar.core.util import load_verbs_json

class Verb(Word):
    def __init__(self, in_spanish: str, in_english: str, is_regular: bool, is_reflexive: bool, 
                 conjugation: Dict[str, Dict[str, List[str]]]):
        super().__init__(in_spanish, in_english, "verb")
        self.is_regular = is_regular
        self.is_reflexive = is_reflexive
        self.conjugation = conjugation

    @staticmethod
    def from_json(input: json) -> 'Verb':
        return Verb(
            in_spanish=input["in_spanish"],
            in_english=input["in_english"],
            is_regular=input["is_regular"],
            is_reflexive=input["is_reflexive"],
            conjugation=input["conjugation"]
        )

    def __repr__(self):
        return f"Verb(id={self.id}, in_spanish='{self.in_spanish}', in_english='{self.in_english}', is_regular={self.is_regular}, is_reflexive={self.is_reflexive})"

def load_verbs() -> List[Verb]:
    verbs = []
    for verb in load_verbs_json():
        verbs.append(Verb.from_json(verb))
    return verbs