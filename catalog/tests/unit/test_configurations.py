from unittest import TestCase

from catalog.src.configurations import EnvConfigRepository


class TestConfig(TestCase):
    def test_should_init(self):
        configurations = EnvConfigRepository(
            MONGO_HOST='local',
            MONGO_PORT='6669'
        )
        self.assertEqual(configurations.MONGO_HOST, 'local')
        self.assertEqual(configurations.MONGO_PORT, '6669')
