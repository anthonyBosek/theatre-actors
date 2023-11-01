from .audition import Audition


class Actor:
    all = []

    def __init__(self, name, auditions, roles):
        self.name = name
        self.auditions = auditions
        self.roles = roles
        type(self).all.append(self)
