import pickle
from redis import StrictRedis


class CacheRepository:
    redis_client = StrictRedis.from_url(url='redis://localhost:6379/7')

    @classmethod
    def set(cls, podcast_id, episodes):
        cls.redis_client.set(podcast_id, pickle.dumps(episodes), ex=3600)

    @classmethod
    def get(cls, podcast_id):
        result = cls.redis_client.get(podcast_id)
        if result:
            episodes = pickle.loads(result)
            return episodes
        return None
