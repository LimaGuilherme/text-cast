from typing import List

from catalog.src.entity import Podcast, Episode


class PodcastService:

    def __init__(self, repository) -> None:
        self.__repository = repository

    def create_podcast(self, podcast_data: dict) -> Podcast:
        podcast = Podcast(**podcast_data)
        return self.__repository.add(podcast)

    def get_podcast(self, podcast_id: str) -> Podcast:
        return self.__repository.list(podcast_id)

    def list_podcasts(self) -> List[Podcast]:
        return self.__repository.list_all()

    def remove_podcast(self, podcast_id: str) -> None:
        self.__repository.delete(podcast_id)


class EpisodeService:

    def __init__(self, repository) -> None:
        self.__repository = repository

    def create_episode(self, episode_data: dict) -> Episode:
        episode = Episode(**episode_data)
        return self.__repository.add(episode)

    def get_episode(self, episode_id: str) -> Episode:
        return self.__repository.list(episode_id)

    def list_episodes(self) -> List[Episode]:
        return self.__repository.list_all()

    def remove_episode(self, episode_id: str) -> None:
        self.__repository.delete(episode_id)
