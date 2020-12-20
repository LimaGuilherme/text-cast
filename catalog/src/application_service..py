class PodcastService:

    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self, podcast_data):
        self.repository.add(podcast_data)


class EpisodeService:

    def __init__(self, repository) -> None:
        self.repository = repository

    def create(self, episode_data):
        self.repository.add(episode_data)
