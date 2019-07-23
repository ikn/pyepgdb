from . import bytedata


def _group_tokens (tokens):
    restorable_tokens = bytedata.result.RestorableIterator(tokens)
    finished = False

    def iter_group ():
        current_path = None
        for token in restorable_tokens:
            path_base = token.path[:1]
            if path_base != current_path:
                if current_path is not None:
                    restorable_tokens.add(token)
                    return
                current_path = path_base
            if len(token.path) >= 4 and token.path[1] == 'record':
                yield token

        nonlocal finished
        finished = True

    while not finished:
        yield iter_group()


def _transform_record (record):
    if isinstance(record, list):
        # value can only be missing if it was an empty sequence of tokens,
        # which should have become a list, which we should transform into a dict
        return {field['name']: field.get('value', {}) for field in record}
    else:
        return record


def parse (tokens):
    for record_tokens in _group_tokens(tokens):
        yield bytedata.result.build_record(record_tokens, _transform_record, 2)
