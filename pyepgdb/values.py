from .network import util as networkutil

_EPISODE_KEY = 'e:'
_BROADCAST_KEY = 'b:'
_EPISODES_SECTION = 'episodes'
_BROADCASTS_SECTION = 'broadcasts'


class _Episode:
    def __init__ (self, fields):
        self.id_ = networkutil.read_value(
            fields, 'uri', networkutil.validate(str))
        self.fields = fields


class _Broadcast:
    def __init__ (self, fields):
        self.episode_id = networkutil.read_value(
            fields, 'episode', networkutil.validate(str))
        self.fields = fields


def parse (items, store=None):
    if store is None:
        store = {}
    section = None

    for item in items:
        if not isinstance(item, dict):
            pass
        elif '__section__' in item:
            section = item['__section__']
            pass
        elif section == _EPISODES_SECTION:
            episode = _Episode(item)
            store[_EPISODE_KEY + episode.id_] = episode
        elif section == _BROADCASTS_SECTION:
            broadcast = _Broadcast(item)
            episode = store.get(_EPISODE_KEY + broadcast.episode_id)
            if episode is None:
                store[_BROADCAST_KEY] = broadcast
            else:
                yield (episode.fields, broadcast.fields)

    for store_key, broadcast in store.items():
        if store_key.startswith(_BROADCAST_KEY):
            episode = store[_EPISODE_KEY + broadcast.episode_id]
            yield (episode.fields, broadcast.fields)
