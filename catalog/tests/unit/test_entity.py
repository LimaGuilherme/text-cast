from unittest import TestCase

from catalog.src.entity import Episode, Podcast


class TestPodcastEntity(TestCase):

    def test_should_create_podcast_entity_properly(self):
        podcast = Podcast(name='Flow Podcast',
                          rss='https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')

        self.assertEqual(podcast.name, 'Flow Podcast')
        self.assertEqual(podcast.rss, 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')
        self.assertIsInstance(podcast, Podcast)


class TestEpisodeEntity(TestCase):

    def test_should_create_episode_entity_properly(self):
        episode = Episode(name='ANDRÉ VIANCO - Flow Podcast #279',
                          podcast='Flow Podcast',
                          image='https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg',
                          description='André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark')

        self.assertEqual(episode.name, 'ANDRÉ VIANCO - Flow Podcast #279')
        self.assertEqual(episode.podcast, 'Flow Podcast')
        self.assertEqual(episode.image, 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg')
        self.assertEqual(episode.description, 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark')
        self.assertIsInstance(episode, Episode)
