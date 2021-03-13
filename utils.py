from values.pool import Pool, PoolValue
from values.object import Object, ObjectField
from values.array import Array
from values.number import Number
from values.fixed import Fixed

def strip(d, *fields):
    copy = dict(d)
    for field in fields:
        del copy[field]
    return copy

def withvalue(d):
    copy = dict(d)
    if 'value' in d:
        copy['value'] = fromjson(copy['value'])
    return copy

def fromjson(config):
    if config['type'] == 'pool':
        if 'values' in config:
            values = [PoolValue(**withvalue(value)) for value in config['values']]
            return Pool(values=values, **strip(config, 'values', 'type'))
        else:
            return Pool(**strip(config, 'type'))
    if config['type'] == 'object':
        if 'fields' in config:
            fields = [ObjectField(**withvalue(field)) for field in config['fields']]
            return Object(fields=fields, **strip(config, 'fields', 'type'))
        else:
            return Object(**strip(config, 'type'))
    if config['type'] == 'array':
        return Array(**strip(withvalue(config), 'type'))
    if config['type'] == 'number':
        return Number(**strip(config, 'type'))
    if config['type'] == 'fixed':
        return Fixed(**strip(config, 'type'))