from typing import List

from catalog.src.entity import Podcast


class PodcastService:

    def __init__(self, repository) -> None:
        self.__repository = repository

    def create_podcast(self, podcast_data: dict) -> Podcast:
        podcast = Podcast(**podcast_data)
        return self.__repository.add(podcast)

    def list_episodes(self, podcast_id: str) -> Podcast:
        podcast = self.__repository.list(podcast_id)
        return podcast

    def list_podcasts(self) -> List[Podcast]:
        return self.__repository.list_all()

    def remove_podcast(self, podcast_id: str) -> None:
        self.__repository.delete(podcast_id)
