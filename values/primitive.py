from functools import reduce
from scipy.stats import randint
from .value import Value

class PrimitiveValue(Value):
    def __init__(self, values=[None]):
        self.values = values

    def resolve(self):
        return self.values[randint.rvs(0, len(self.values))]