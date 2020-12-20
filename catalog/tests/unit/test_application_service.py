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
