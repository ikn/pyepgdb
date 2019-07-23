import itertools


def validate (type_, allow_none=False, default=None):
    def validate_fn (value):
        if value is None:
            if allow_none:
                return default
            else:
                raise ValueError('field is missing')
        if not isinstance(value, type_):
            raise ValueError('expected: {}; got: {}'.format(type_, repr(value)))
        return value

    return validate_fn


def validate_map (validate_fn, allow_none=False, default=None):
    validate_outer = validate(dict, allow_none, default)

    def validate_map_fn (value):
        valid_value = validate_outer(value)
        deep_valid_value = {}
        for key, inner_value in valid_value.items():
            try:
                deep_valid_value[key] = validate_fn(inner_value)
            except ValueError as e:
                raise ValueError({'key': key}, *e.args)
        return deep_valid_value

    return validate_map_fn


def read_value (fields, name, validate_fn):
    value = fields.get(name)
    try:
        return validate_fn(value)
    except ValueError as e:
        raise ValueError('found item with unexpected value',
                         {'field': name, 'fields': fields},
                         *e.args)


def localise (lang, strings):
    return strings.get(lang, next(itertools.chain(strings.values(), ('',))))

