from typing import List

import pymongo

from bson import ObjectId

from catalog.src.entity import Podcast, Episode
from catalog.src.exceptions import InvalidRepository


class PodcastRepository:

    def __init__(self, collection):
        self.__collection = collection

    def add(self, podcast: Podcast) -> Podcast:
        podcast_document = self.__collection.insert_one(
            {
                'name': podcast.name,
                'rss': podcast.rss
            }
        )
        return Podcast(name=podcast.name, rss=podcast.rss, _id=str(podcast_document.inserted_id))

    def list(self, podcast_id: str) -> Podcast:
        podcast_document = self.__collection.find_one({'_id': ObjectId(podcast_id)})

        if podcast_document:
            return Podcast(name=podcast_document['name'], rss=podcast_document['rss'], _id=str(podcast_document['_id']))

        return None

    def list_all(self) -> List[Podcast]:
        return [Podcast(name=podcast_document['name'], rss=podcast_document['rss'],
                        _id=str(podcast_document['_id'])) for podcast_document in self.__collection.find()]

    def delete(self, podcast_id: str) -> None:
        self.__collection.delete_one({'_id': ObjectId(podcast_id)})


class EpisodeRepository:

    def __init__(self, collection):
        self.__collection = collection

    def add(self, episode: Episode) -> Episode:
        episode_document = self.__collection.insert_one(
            {
                'name': episode.name,
                'podcast': episode.podcast,
                'image': episode.image,
                'description': episode.description,
                'audio': episode.audio
            }
        )
        return Episode(name=episode.name, podcast=episode.podcast, image=episode.image,
                       description=episode.description, audio=episode.audio, _id=str(episode_document.inserted_id))

    def list(self, episode_id: str) -> Episode:
        episode_document = self.__collection.find_one({'_id': ObjectId(episode_id)})

        if episode_document:
            return Episode(name=episode_document['name'], podcast=episode_document['podcast'], image=episode_document['image'],
                           description=episode_document['description'], audio=episode_document['audio'],
                           _id=str(episode_document['_id']))
        return None

    def list_all(self) -> List[Episode]:
        return [Episode(name=episode_document['name'], podcast=episode_document['podcast'], image=episode_document['image'],
                        description=episode_document['description'], audio=episode_document['audio'],
                        _id=str(episode_document['_id'])) for episode_document in self.__collection.find()]

    def delete(self, episode_id: str) -> None:
        self.__collection.delete_one({'_id': ObjectId(episode_id)})


def create_repository(configurations, repository):
    mongo_client = pymongo.MongoClient(configurations.MONGO_HOST, int(configurations.MONGO_PORT))
    database = mongo_client[configurations.MONGO_DB]

    if repository == 'podcast':
        collection = database[configurations.MONGO_PODCAST_COLLECTION]
        return PodcastRepository(collection)

    if repository == 'episode':
        collection = database[configurations.MONGO_EPISODE_COLLECTION]
        return EpisodeRepository(collection)

    raise InvalidRepository(f'Cant create repository because this type {repository} '
                            f'is invalid. Valid options: [podcast, episode]')

