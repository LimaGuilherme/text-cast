from unittest import TestCase, mock

from catalog.src.configurations import Config, get_config
from catalog.src.exceptions import ConfigError


class TestConfig(TestCase):
    def test_should_init(self):
        configurations = Config(
            MONGO_HOST='local',
            MONGO_PORT='6669'
        )
        self.assertEqual(configurations.MONGO_HOST, 'local')
        self.assertEqual(configurations.MONGO_PORT, '6669')

    @mock.patch('catalog.src.configurations.os')
    def test_should_get_configurations(self, os_mock):
        os_mock.environ = {
            'MONGO_HOST': 'mock-host',
            'MONGO_PORT': 'mock-port'
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
