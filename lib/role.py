from .audition import Audition


class Role:
    all = []

    def __init__(self, character_name, auditions):
        self.character_name = character_name
        self.auditions = auditions
        type(self).all.append(self)
