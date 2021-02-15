from typing import List, Union

import pymongo

from bson import ObjectId

from catalog.src.entity import Podcast
from transcription.src.entity import Transcription


class TranscriptionRepository:

    def __init__(self, collection):
        self.__collection = collection

    def _create_transcription_from_mongodb(self, transcription_document: dict) -> Podcast:
        return Transcription()

    def add(self, podcast: Podcast) -> Podcast:
        podcast_document = self.__collection.insert_one(
            {
                'rss': podcast.rss,
                'name': podcast.name,
                'image': podcast.image,
            }
        )

        podcast.set_id(str(podcast_document.inserted_id))
        return podcast

    def list(self, podcast_id: str) -> Union[Podcast, None]:
        podcast_document = self.__collection.find_one({'_id': ObjectId(podcast_id)})
        if not podcast_document:
            return None
        return self._create_transcription_from_mongodb(podcast_document)

    def list_all(self) -> List[Podcast]:
        return [self._create_transcription_from_mongodb(podcast_document) for podcast_document in self.__collection.find()]

    def delete(self, transcription_id: str) -> None:
        self.__collection.delete_one({'_id': ObjectId(transcription_id)})


def create_repository(configurations):
    mongo_client = pymongo.MongoClient(configurations.MONGO_HOST, int(configurations.MONGO_PORT))
    database = mongo_client[configurations.MONGO_DB]
    collection = database[configurations.MONGO_TRANSCRIPTION_COLLECTION]
    return TranscriptionRepository(collection)

