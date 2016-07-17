class Item:
    def __repr__(self):
        return "<%s>" % self.__class__.__name__

class Char(Item):
    def __init__(self, C): self.val = C

SRC = map(Char, open('src.src').read())

print SRC
