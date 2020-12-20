from unittest import TestCase

from catalog.src.configurations import Config, get_config


class TestPodcastRepository(TestCase):

    def setUp(self) -> None:
        self.config = get_config()
        self.podcast_repository = create_podcast_repository(self.config)
        self.podcast = Podcast({
            'name': 'Flow Podcast',
            'rss': 'https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss'
        })

    def tearDown(self) -> None:
        self.podcast_repository[self.config.MONGO_PODCAST_COLLECTION].drop()

    def test_should_add_podcast(self):
        self.podcast_repository.add(self.podcast)


class TestEpisodeRepository(TestCase):

    def setUp(self) -> None:
        self.config = get_config()
        self.podcast_repository = create_episode_repository(self.config)
        self.episode = Episode({
            'name': 'ANDRÉ VIANCO - Flow Podcast #279',
            'podcast': 'Flow Podcast',
            'image': 'https://artworks-flow.s3-sa-east-1.amazonaws.com/279_Andre_Vianco.jpg',
            'description': 'André Vianco é um escritor brabo que escreveu os livros que mais marcaram a vida do Monark',
            'audio': 'https://content.blubrry.com/flowpdc/279_ANDRE_VIANCO.mp3'
        })

    def tearDown(self) -> None:
        self.podcast_repository[self.config.MONGO_EPISODE_COLLECTION].drop()

    def test_should_add_podcast(self):
        self.podcast_repository.add(self.episode)

