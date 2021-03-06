from typing import List

from src.entity import Podcast


class PodcastService:

    def __init__(self, repository, rss_reader, cache_repository, domain_service) -> None:
        self.__repository = repository
        self.__rss_reader = rss_reader
        self.__cache_repository = cache_repository
        self.__domain_service = domain_service

    def create_podcast(self, podcast_data: dict) -> Podcast:
        podcast_infos = self.__rss_reader.read_podcast(podcast_data['rss'])
        podcast = Podcast(
            rss=podcast_data['rss'],
            name=podcast_infos['name'],
            image=podcast_infos['image'])
        return self.__repository.add(podcast)

    def list_episode(self, episode_id: str):
        self.


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
        self.__domain_service.delete_transcriptions(podcast_id)

class UploadFileService:

    def __init__(self, aws_s3):
        self._aws_s3 = aws_s3




class TranscribeService:

    def __init__(self, aws_transcribe):
        self._aws_transcribe = aws_transcribe


    def transcribe(self):
        self._aws_transcribe.transcribe_file()
