from flask import request
from flask_restful import Resource

from catalog.src.serializer import serialize_podcast_to_json
from catalog.src.web_app import get_api

api = get_api()


class ResourceBase(Resource):

    def __init__(self, *args, **kwargs):
        super(ResourceBase, self).__init__(*args, **kwargs)


class PodcastResource(ResourceBase):

    def __init__(self, podcast_service):
        super(PodcastResource, self).__init__()
        self.podcast_service = podcast_service

    def post(self):
        podcast_data = request.json
        podcast = self.podcast_service.create_podcast(podcast_data)
        return serialize_podcast_to_json(podcast), 201

    def get(self):
        podcasts = self.podcast_service.list_podcasts()
        return [serialize_podcast_to_json(podcast) for podcast in podcasts], 200

    def delete(self, podcast_id: str):
        self.podcast_service.remove_podcast(podcast_id)
        return {'result': 'Podcast Deleted'}, 204


class PodcastEpisodeResource(Resource):

    def __init__(self, podcast_service):
        self.podcast_service = podcast_service

    def get(self, podcast_id: str):
        podcast_episodes = self.podcast_service.list_episodes(podcast_id)
        return serialize_podcast_to_json(podcast_episodes), 200


class TranscribeResource(Resource):

    def __init__(self, podcast_service):
        self.podcast_service = podcast_service

    def get(self, episode_id: str):
        episode = self.podcast_service.list_episode(episode_id)
        # salvar no s3
        # file_uri =
        self.transribe_service.transribe(file_uri)


def register(podcast_service, transcribe_service) -> None:
    api.add_resource(PodcastResource,
                     '/api/podcasts',
                     '/api/podcasts/<string:podcast_id>',
                     resource_class_kwargs={
                         'podcast_service': podcast_service
                     })

    api.add_resource(PodcastEpisodeResource,
                     '/api/podcasts/<string:podcast_id>/episodes',
                     resource_class_kwargs={
                         'podcast_service': podcast_service
                     })

    api.add_resource(TranscribeResource,
                     '/api/episodes/<string:episode_id>/transcribe',
                     resource_class_kwargs={
                         transcribe_service
                     })
