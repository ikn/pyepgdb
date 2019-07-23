from . import bytedata
from .bytedata import define as d, parse as p

_p_uint = p.int_('big')
_p_str = p.str_('utf8')

_defn_field = sum([
    d.named('type', d.parse(1, _p_uint)),
    d.named('name size', d.parse(1, _p_uint)),
    d.named('value size', d.parse(4, _p_uint)),
    d.named('name', d.parse(('name size',), _p_str)),
])

_defns_value = {
    1: d.repeat_size(('value size',), _defn_field),
    2: d.parse(('value size',), p.int_('little')),
    3: d.parse(('value size',), _p_str),
    5: d.parse(('value size',), p.binary),
}

_defn_field += d.dispatch(('type',), {
    type_: d.named('value', defn)
    for type_, defn in _defns_value.items()
})

_defn_file = d.repeat_until_eof(sum([
    d.named('size', d.parse(4, _p_uint)),
    d.named('record', d.repeat_size(('size',), _defn_field)),
]))


def parse (f):
    return _defn_file.read(bytedata.StreamReader(f))
