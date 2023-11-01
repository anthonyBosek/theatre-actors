class Audition:
    all = []

    def __init__(self, actor, location, hired):
        self.actor = actor
        self.location = location
        self.hired = hired
        type(self).all.append(self)
