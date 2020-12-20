from unittest import TestCase, mock


class TestPodcastService(TestCase):

    def test_should_add_podcast(self):
        podcast_repository = mock.MagicMock()
        podcast_service = PodcastService(podcast_repository)
        podcast_data = {
            'name': 'Flow Podcast',
            'rss': 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss'
        }
        podcast_service.create(podcast_data)
        podcast_repository.add.assert_called()

        podcast = podcast_repository.add.mock_calls[0].args[0]
        self.assertEqual(podcast.name, 'Flow Podcast')
        self.assertEqual(podcast.rss, 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')

    def test_should_return_one_podcast(self):
        podcast_repository = mock.MagicMock()
        podcast_mock = mock.MagicMock()

        podcast_service = PodcastService(podcast_repository)
        podcast_repository.return_value = podcast_mock

        podcast = podcast_service.get_podcast('Flow Podcast')

        podcast_repository.get_by_name.assert_called()
        self.assertEqual(podcast, podcast_mock)

    def test_should_return_all_podcasts(self):
        podcast_repository = mock.MagicMock()
        podcasts_mock = mock.MagicMock()

        podcast_service = PodcastService(podcast_repository)
        podcast_repository.return_value = podcasts_mock

        podcasts = podcast_service.list_all()

        podcast_repository.list_all.assert_called()
        self.assertEqual(podcasts, podcasts_mock)


class TestEpisodeService(TestCase):

    def test_should_add_episode(self):
        episode_repository = mock.MagicMock()
        episode_service = EpisodeService(episode_repository)
        episode_data = {
            'name': 'ANDRÉ VIANCO - Flow Podcast #279',
            'podcast': 'Flow Podcast',
            'image': 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg',
            'description': 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark',
            'audio': 'https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3'
        }
        episode_service.create(episode_data)
        episode_repository.add.assert_called()

        episode = episode_repository.add.mock_calls[0].args[0]
        self.assertEqual(episode.name, 'ANDRÉ VIANCO - Flow Podcast #279')
        self.assertEqual(episode.podcast, 'Flow Podcast')
        self.assertEqual(episode.image, 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg')
        self.assertEqual(episode.description, 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark')
        self.assertEqual(episode.audio, 'https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3')


class TestRssReaderTest(TestCase):

    def test_should_read_rss_from_podcast(self):
        podcast = Podcast(name='Flow Podcast',
                          rss='https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')

        rss_service = RssReaderService(podcast)
        rss_service.read()

        self.assertIsInstance(rss_service, RssReaderService)
        self.assertEqual(rss_service.item, 'DontKnow')
