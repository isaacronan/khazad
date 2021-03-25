from random import randint
from .value import Value

class Fixed(Value):
    def __init__(self, values=[None]):
        self.values = values

    def resolve(self):
        return self.values[randint(0, len(self.values) - 1)]