from enum import Enum
import time

from . import util as networkutil

LANGUAGE = 'eng'


class Genre (Enum):
    UNKNOWN = None

    ARTS = b'\x02\x00\x00\x00\x00\x01p'
    CHILDRENS = b'\x02\x00\x00\x00\x00\x01P'
    EDUCATION = b'\x02\x00\x00\x00\x00\x01\x90'
    FILM = b'\x02\x00\x00\x00\x00\x01\x10'
    GAME_SHOW = b'\x02\x00\x00\x00\x00\x010'
    HOBBIES = b'\x02\x00\x00\x00\x00\x01\xa0'
    MUSIC = b'\x02\x00\x00\x00\x00\x01`'
    NEWS = b'\x02\x00\x00\x00\x00\x01 '
    POLITICAL = b'\x02\x00\x00\x00\x00\x01\x80'
    SPORT = b'\x02\x00\x00\x00\x00\x01@'


def _localise (strings):
    return networkutil.localise(LANGUAGE, strings)


class Programme:
    def __init__ (self, episode, broadcast):
        self.id_ = networkutil.read_value(
            episode, 'uri', networkutil.validate(str))
        self.genre = Genre(networkutil.read_value(
            episode, 'genre', networkutil.validate(bytes, True, None)))
        raw_title = _localise(networkutil.read_value(
            episode, 'title',
            networkutil.validate_map(networkutil.validate(str), True, {})))
        self.title = (raw_title[5:] if raw_title.startswith('New: ')
                      else raw_title)
        self.subtitle = _localise(networkutil.read_value(
            episode, 'subtitle',
            networkutil.validate_map(networkutil.validate(str), True, {})))

        self.start = time.gmtime(networkutil.read_value(
            broadcast, 'start', networkutil.validate(int)))
        self.stop = time.gmtime(networkutil.read_value(
            broadcast, 'stop', networkutil.validate(int)))
        self.channel = networkutil.read_value(
            broadcast, 'channel', networkutil.validate(str))
        self.summary = _localise(networkutil.read_value(
            broadcast, 'summary',
            networkutil.validate_map(networkutil.validate(str), True, {})))
        self.widescreen = bool(networkutil.read_value(
            broadcast, 'is_widescreen', networkutil.validate(int, True, 0)))
        self.subtitled = bool(networkutil.read_value(
            broadcast, 'is_subtitled', networkutil.validate(int, True, 0)))
        self.audio_desc = bool(networkutil.read_value(
            broadcast, 'is_audio_desc', networkutil.validate(int, True, 0)))
        self.signed = bool(networkutil.read_value(
            broadcast, 'is_deafsigned', networkutil.validate(int, True, 0)))


def parse (programmes):
    for episode, broadcast in programmes:
        yield Programme(episode, broadcast)
