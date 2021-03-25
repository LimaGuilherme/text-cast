from unittest import TestCase

import pymongo

from src.configurations import get_config
from src.entity import Podcast, Episode
from src import InvalidRepository
from src.infrascructure import create_repository, PodcastRepository, EpisodeRepository


class TestCreateRepository(TestCase):

    def setUp(self) -> None:
        self.config = get_config()

    def test_should_raise_invalid_repository_when_given_a_invalid_type(self) -> None:
        with self.assertRaises(InvalidRepository):
            self.config = get_config()
            create_repository(self.config, 'bonus')

    def test_should_return_a_podcast_repository(self) -> None:
        podcast_repository = create_repository(self.config, 'podcast')
        self.assertIsInstance(podcast_repository, PodcastRepository)

    def test_should_return_a_episode_repository(self) -> None:
        episode_repository = create_repository(self.config, 'episode')
        self.assertIsInstance(episode_repository, EpisodeRepository)


class TestPodcastRepository(TestCase):

    def setUp(self) -> None:
        configurations = get_config()
        mongo_client = pymongo.MongoClient(configurations.MONGO_HOST, int(configurations.MONGO_PORT))
        self.database = mongo_client[configurations.MONGO_DB]
        self.collection = self.database[configurations.MONGO_PODCAST_COLLECTION]
        self.podcast_repository = PodcastRepository(self.collection)

        self.podcast = Podcast(
            name='Flow Podcast',
            rss='https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss'
        )

    def tearDown(self) -> None:
        self.database.drop_collection(self.collection)

    def test_should_add_podcast(self) -> None:
        podcast = self.podcast_repository.add(self.podcast)
        self.assertEqual(podcast.name, 'Flow Podcast')
        self.assertEqual(podcast.rss, 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')
        self.assertTrue(hasattr(podcast, 'id'))
        self.assertIsInstance(podcast, Podcast)

    def test_should_get_podcast(self) -> None:
        created_podcast = self.podcast_repository.add(self.podcast)
        podcast = self.podcast_repository.list(created_podcast.id)
        self.assertEqual(podcast.name, 'Flow Podcast')
        self.assertEqual(podcast.rss, 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')
        self.assertIsInstance(podcast, Podcast)

    def test_should_get_all_podcasts(self) -> None:
        for x in range(3):
            self.podcast_repository.add(self.podcast)

        podcasts = self.podcast_repository.list_all()
        self.assertIsInstance(podcasts, list)
        self.assertEqual(len(podcasts), 3)

    def test_should_delete_podcast(self) -> None:
        podcast = self.podcast_repository.add(self.podcast)
        self.podcast_repository.delete(podcast.id)
        podcast = self.podcast_repository.list(podcast.id)
        self.assertEqual(podcast, None)


class TestEpisodeRepository(TestCase):

    def setUp(self) -> None:
        configurations = get_config()
        mongo_client = pymongo.MongoClient(configurations.MONGO_HOST, int(configurations.MONGO_PORT))
        self.database = mongo_client[configurations.MONGO_DB]
        self.collection = self.database[configurations.MONGO_EPISODE_COLLECTION]
        self.episode_repository = EpisodeRepository(self.collection)

        self.episode = Episode(
            name='ANDRÉ VIANCO - Flow Podcast #279',
            podcast='Flow Podcast',
            image='https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg',
            description='André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark',
            audio='https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3'
        )

    def tearDown(self) -> None:
        self.database.drop_collection(self.collection)

    def test_should_add_episode(self) -> None:
        episode = self.episode_repository.add(self.episode)
        self.assertEqual(episode.name, 'ANDRÉ VIANCO - Flow Podcast #279')
        self.assertEqual(episode.podcast, 'Flow Podcast')
        self.assertEqual(episode.image, 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg')
        self.assertEqual(episode.description, 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark')
        self.assertEqual(episode.audio, 'https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3')
        self.assertTrue(hasattr(episode, 'id'))
        self.assertIsInstance(episode, Episode)

    def test_should_get_episode(self) -> None:
        created_episode = self.episode_repository.add(self.episode)
        episode = self.episode_repository.list(created_episode.id)
        self.assertEqual(episode.name, 'ANDRÉ VIANCO - Flow Podcast #279')
        self.assertEqual(episode.podcast, 'Flow Podcast')
        self.assertEqual(episode.image, 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg')
        self.assertEqual(episode.description, 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark')
        self.assertEqual(episode.audio, 'https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3')
        self.assertIsInstance(episode, Episode)

    def test_should_get_all_episodes(self) -> None:
        for x in range(3):
            self.episode_repository.add(self.episode)

        episodes = self.episode_repository.list_all()
        self.assertIsInstance(episodes, list)
        self.assertEqual(len(episodes), 3)

    def test_should_delete_podcast(self) -> None:
        created_episode = self.episode_repository.add(self.episode)
        self.episode_repository.delete(created_episode.id)
        episode = self.episode_repository.list(created_episode.id)
        self.assertEqual(episode, None)
