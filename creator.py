from values.object import ObjectValue
from values.array import ArrayValue
from values.multi import MultiValue
from values.number import NumberValue
from values.primitive import PrimitiveValue

def create(blueprint):
    if blueprint['type'] == 'object':
        return ObjectValue([{ 'label': field['label'], 'value': create(field['value']), 'presence': field['presence'] } for field in blueprint['fields']])
    if blueprint['type'] == 'array':
        return ArrayValue(create(blueprint['value']), blueprint['minlength'], blueprint['maxlength'])
    if blueprint['type'] == 'multi':
        return MultiValue([{ 'value': create(value['value']), 'weight': value['weight'] } for value in blueprint['values']])
    if blueprint['type'] == 'number':
        return NumberValue(blueprint['min'], blueprint['max'], blueprint['scale'])
    if blueprint['type'] == 'primitive':
        return PrimitiveValue(blueprint['values'])