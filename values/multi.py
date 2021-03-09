from functools import reduce
from scipy.stats import randint
from .value import Value

class MultiValue(Value):
    def __init__(self, values=[]):
        self.values = values

    def addvalue(self, value, weight=1):
        self.values.append({ 'value': value, 'weight': weight })
        return self

    def resolve(self):
        weightsbyindex = [(index, value['weight']) for (index, value) in enumerate(self.values)]
        poolsbyindex = [[index for i in range(weight)] for (index, weight) in weightsbyindex]
        pool = reduce(lambda a, b: a + b, poolsbyindex, [])
        index = pool[randint.rvs(0, len(pool))]
        return self.values[index]['value'].resolve()