from scipy.stats import bernoulli
from .value import Value

class ObjectValue(Value):
    def __init__(self, fields=[]):
        self.fields = fields

    def addfield(self, label, value, presence=1):
        self.fields.append({ 'label': label, 'value': value, 'presence': presence })
        return self

    def resolve(self):
        presentfields = [(field['label'], field['value']) for field in self.fields if bernoulli.rvs(field['presence']) == 1]
        return dict([(label, value.resolve()) for (label, value) in presentfields])