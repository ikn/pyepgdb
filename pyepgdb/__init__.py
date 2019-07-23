from . import serialisation, compression, structure, values


def parse (f, store=None):
    uncompressed_f = compression.parse(f)
    tokens = serialisation.parse(uncompressed_f)
    records = structure.parse(tokens)
    return values.parse(records, store)
