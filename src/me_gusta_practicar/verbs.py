import json
from typing import List, Dict
from util import path_to_verbs

class Verb:
    def __init__(self, id: int, name: str, EN: str, is_regular: bool, is_reflexive: bool, 
                 conjugation: Dict[str, Dict[str, List[str]]]):
        self.id = id
        self.name = name
        self.EN = EN
        self.is_regular = is_regular
        self.is_reflexive = is_reflexive
        self.conjugation = conjugation

    @staticmethod
    def from_json(input: json) -> 'Verb':
        return Verb(
            id=input["id"],
            name=input["name"],
            EN=input["EN"],
            is_regular=input["is_regular"],
            is_reflexive=input["is_reflexive"],
            conjugation=input["conjugation"]
        )

    def __repr__(self):
        return f"Verb(id={self.id}, name='{self.name}', EN='{self.EN}', is_regular={self.is_regular}, is_reflexive={self.is_reflexive})"


def load_verbs() -> List[Verb]:
    verbs = []
    with open(path_to_verbs(), mode="r", encoding='utf-8') as handle:
        for verb in json.load(handle):
            verbs.append(Verb.from_json(verb))
    return verbs