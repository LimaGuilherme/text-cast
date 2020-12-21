class Podcast:

    def __init__(self, name: str, rss: str, _id: str = None) -> None:
        self.id = _id
        self.name = name
        self.rss = rss


class Episode:

    def __init__(self, name: str, podcast: str, image: str, description: str, audio: str, _id: str = None) -> None:
        self.id = _id
        self.name = name
        self.podcast = podcast
        self.image = image
        self.description = description
        self.audio = audio
