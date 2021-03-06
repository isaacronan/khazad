from random import random
from .value import Value
from .fixed import Fixed

class ObjectField:
    def __init__(self, label='', value=Fixed(), presence=1):
        self.label = label
        self.value = value
        self.presence = presence

class Object(Value):
    def __init__(self, fields=[]):
        self.fields = fields

    def resolve(self):
        presentfields = [(field.label, field.value) for field in self.fields if random() < field.presence]
        return dict([(label, value.resolve()) for (label, value) in presentfields])