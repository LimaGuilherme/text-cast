from typing import List

from catalog.src.entity import Podcast


class PodcastService:

    def __init__(self, repository, rss_reader, cache_repository) -> None:
        self.__repository = repository
        self.__rss_reader = rss_reader
        self.__cache_repository = cache_repository

    def create_podcast(self, podcast_data: dict) -> Podcast:
        podcast_infos = self.__rss_reader.read_podcast(podcast_data['rss'])
        podcast = Podcast(
            rss=podcast_data['rss'],
            name=podcast_infos['name'],
            image=podcast_infos['image'])
        return self.__repository.add(podcast)

    def list_episodes(self, podcast_id: str) -> Podcast:
        episodes = self.__cache_repository.get(podcast_id)
        podcast = self.__repository.list(podcast_id)

        if episodes:
            podcast.associate_episodes(episodes)
            return podcast

        episodes = self.__rss_reader.read_episodes(podcast.rss)
        self.__cache_repository.set(podcast_id, episodes)
        podcast.associate_episodes(episodes)
        return podcast

    def list_podcasts(self) -> List[Podcast]:
        return self.__repository.list_all()

    def remove_podcast(self, podcast_id: str) -> None:
        self.__repository.delete(podcast_id)
