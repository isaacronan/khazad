from math import trunc
from scipy.stats import uniform
from .value import Value

class Number(Value):
    def __init__(self, min=0, max=0, scale=0):
        self.min = min
        self.max = max
        self.scale = scale

    def resolve(self):
        raw = self.min + uniform.rvs() * (self.max - self.min)
        scaled = trunc(raw * 10 ** self.scale) / 10 ** self.scale
        return scaled