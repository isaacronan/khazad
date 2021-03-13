from scipy.stats import randint
from .value import Value
from .fixed import Fixed

class Array(Value):
    def __init__(self, value=Fixed(), minlength=0, maxlength=0):
        self.value = value
        self.minlength = minlength
        self.maxlength = maxlength

    def resolve(self):
        length = randint.rvs(self.minlength, self.maxlength + 1)
        return [self.value.resolve() for i in range(length)]