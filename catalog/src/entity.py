from typing import List


class Episode:

    def __init__(self, name: str, podcast: str, image: str, description: str, audio: str, _id: str = None) -> None:
        self.id = _id
        self.name = name
        self.podcast = podcast
        self.image = image
        self.description = description
        self.audio = audio


class Podcast:

    def __init__(self, rss: str, name, image, _id: str = None) -> None:
        self._id = _id
        self._rss = rss
        self._name = name
        self._image = image
        self._episodes = None

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return self._image

    @property
    def rss(self):
        return self._rss

    @property
    def id(self):
        return self._id

    @property
    def episodes(self):
        return self._episodes

    def set_id(self, mongodb_id):
        self._id = mongodb_id

    def associate_episodes(self, episodes: List[Episode]) -> None:
        self._episodes = episodes
