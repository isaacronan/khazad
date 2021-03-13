from functools import reduce
from scipy.stats import randint
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
        index = pool[randint.rvs(0, len(pool))]
        return self.values[index].value.resolve()