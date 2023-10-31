from .audition import Audition


class Actor:
    all = []

    def __init__(self):
        type(self).all.append(self)
