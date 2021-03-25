from functools import reduce
from random import randint
from .value import Value
from .fixed import Fixed

class PoolValue:
    def __init__(self, value=Fixed(), weight=1):
        self.value = value
        self.weight = weight

class Pool(Value):
    def __init__(self, values=[PoolValue()]):
        self.values = values

    def resolve(self):
        weightsbyindex = [(index, value.weight) for (index, value) in enumerate(self.values)]
        poolsbyindex = [[index for i in range(weight)] for (index, weight) in weightsbyindex]
        pool = reduce(lambda a, b: a + b, poolsbyindex, [])
        index = pool[randint(0, len(pool) - 1)]
        return self.values[index].value.resolve()