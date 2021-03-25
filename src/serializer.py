from src.entity import Podcast, Episode


def __create_episode_json(episode: Episode) -> dict:
    return {
        'name': episode.name,
        'description': episode.description,
        'audio': episode.audio,
        'podcast': episode.podcast,
        'image': episode.image
    }


def serialize_podcast_to_json(podcast: Podcast) -> dict:
    podcast_json = {
        'id': podcast.id,
        'name': podcast.name,
        'rss': podcast.rss
    }

    if podcast.episodes:
        podcast_json['episodes'] = [__create_episode_json(episode) for episode in podcast.episodes]

    return podcast_json


