class Podcast:

    def __init__(self, name, rss):
        self.name = name
        self.rss = rss


class Episode:

    def __init__(self, name, podcast, image, description):
        self.name = name
        self.podcast = podcast
        self.image = image
        self.description = description
