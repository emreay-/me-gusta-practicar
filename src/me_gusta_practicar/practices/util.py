from typing import List

from me_gusta_practicar.practices.practice_base import PracticeBase
from me_gusta_practicar.practices.verb_practice import VerbPractice
from me_gusta_practicar.practices.noun_practice import NounPractice
from me_gusta_practicar.practices.prepositions_practice import PrepositionPractice
from me_gusta_practicar.practices.others_practice import OthersPractice
from me_gusta_practicar.practices.mixed_words_practice import MixedWordsPractice

def get_practice_display_names() -> List[str]:
    return [VerbPractice.display_name, NounPractice.display_name, PrepositionPractice.display_name, OthersPractice.display_name, MixedWordsPractice.display_name]


def create_practices(display) -> List[PracticeBase]:
    practices = {
        VerbPractice.display_name: VerbPractice(display),
        NounPractice.display_name: NounPractice(display),
        PrepositionPractice.display_name: PrepositionPractice(display),
        OthersPractice.display_name: OthersPractice(display),
        MixedWordsPractice.display_name: MixedWordsPractice(display)
    }

    assert len(practices) == len(get_practice_display_names())

    return practices