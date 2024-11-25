class Word:
    _id_count: int = 0

    def __init__(self, in_spanish: str, in_english: str, category: str):
        Word._id_count += 1
        self.id = Word._id_count
        self.in_spanish = in_spanish
        self.in_english = in_english
        self.category = category