from unittest import TestCase, mock

from src import PodcastService, EpisodeService


class TestPodcastService(TestCase):

    def test_create_podcast(self):
        podcast_repository = mock.MagicMock()
        podcast_service = PodcastService(podcast_repository)
        podcast_data = {
            'name': 'Flow Podcast',
            'rss': 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss'
        }
        podcast_service.create_podcast(podcast_data)
        podcast_repository.add.assert_called()

        podcast = podcast_repository.add.mock_calls[0].args[0]
        self.assertEqual(podcast.name, 'Flow Podcast')
        self.assertEqual(podcast.rss, 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss')

    def test_list_podcasts(self):
        podcasts_mock = mock.MagicMock()
        repository_mock = mock.MagicMock()
        repository_mock.list_all.return_value = podcasts_mock

        service = PodcastService(repository_mock)
        podcasts = service.list_podcasts()

        repository_mock.list_all.assert_called()
        self.assertEqual(podcasts_mock, podcasts)

    def test_get_podcast(self):
        repository = mock.MagicMock()
        podcast_mock = mock.MagicMock()
        repository.list.return_value = podcast_mock

        podcast_service = PodcastService(repository)
        podcast = podcast_service.get_podcast('1')

        repository.list.assert_called()
        self.assertEqual(podcast_mock, podcast)

    def test_remove_product(self):
        podcast_mock = mock.MagicMock()
        repository = mock.MagicMock()

        repository.list.return_value = podcast_mock

        service = PodcastService(repository)
        service.remove_podcast('1')
        repository.delete.assert_called_with('1')


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
        episode_service.create_episode(episode_data)
        episode_repository.add.assert_called()

        episode = episode_repository.add.mock_calls[0].args[0]
        self.assertEqual(episode.name, 'ANDRÉ VIANCO - Flow Podcast #279')
        self.assertEqual(episode.podcast, 'Flow Podcast')
        self.assertEqual(episode.image, 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg')
        self.assertEqual(episode.description, 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark')
        self.assertEqual(episode.audio, 'https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3')

    def test_list_episodes(self):
        episodes_mock = mock.MagicMock()
        repository_mock = mock.MagicMock()
        repository_mock.list_all.return_value = episodes_mock

        service = EpisodeService(repository_mock)
        episodes = service.list_episodes()

        repository_mock.list_all.assert_called()
        self.assertEqual(episodes_mock, episodes)

    def test_get_podcast(self):
        repository_mock = mock.MagicMock()
        episode_mock = mock.MagicMock()
        repository_mock.list.return_value = episode_mock

        service = EpisodeService(repository_mock)
        episode = service.get_episode('1')

        repository_mock.list.assert_called()
        self.assertEqual(episode_mock, episode)

    def test_remove_product(self):
        episode_mock = mock.MagicMock()
        repository_mock = mock.MagicMock()

        repository_mock.list.return_value = episode_mock

        service = EpisodeService(repository_mock)
        service.remove_episode('1')
        repository_mock.delete.assert_called_with('1')
