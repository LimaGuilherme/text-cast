from unittest import TestCase, mock

from src.configurations import Config, get_config
from src import ConfigError


class TestConfig(TestCase):
    def test_should_init(self):
        configurations = Config(
            MONGO_HOST='local',
            MONGO_PORT='6669',
            MONGO_DB='textcast',
            MONGO_PODCAST_COLLECTION='podcasts',
            MONGO_EPISODE_COLLECTION='episodes',

        )
        self.assertEqual(configurations.MONGO_HOST, 'local')
        self.assertEqual(configurations.MONGO_PORT, '6669')
        self.assertEqual(configurations.MONGO_DB, 'textcast')
        self.assertEqual(configurations.MONGO_PODCAST_COLLECTION, 'podcasts')
        self.assertEqual(configurations.MONGO_EPISODE_COLLECTION, 'episodes')

    @mock.patch('catalog.src.configurations.os')
    def test_should_get_configurations(self, os_mock):
        os_mock.environ = {
            'MONGO_HOST': 'mock-host',
            'MONGO_PORT': 'mock-port',
            'MONGO_DB': 'mock-db',
            'MONGO_PODCAST_COLLECTION': 'mock-podcast-collection',
            'MONGO_EPISODE_COLLECTION': 'mock-episode-collection'
        }

        configurations = get_config()
        self.assertIsInstance(configurations, Config)
        self.assertEqual(configurations.MONGO_HOST, 'mock-host')
        self.assertEqual(configurations.MONGO_PORT, 'mock-port')

    @mock.patch('catalog.src.configurations.os')
    def test_should_raise_config_error_when_missing_env_variable(self, os_mock):
        os_mock.environ = {
            'MONGO_HOST': 'mock-host',
        }

        with self.assertRaises(ConfigError):
            get_config()
