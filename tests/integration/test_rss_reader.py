from unittest import TestCase

from src import InvalidRssUrl
from src.rss_reader import RssReader


class Test(TestCase):

    def test_should_read_flow_rss_and_return_a_list_of_episodes(self):
        episodes = RssReader().read("https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss")
        self.assertGreaterEqual(len(episodes), 305)

    def test_should_raise_when_given_a_invalid_rss_url(self):
        with self.assertRaises(InvalidRssUrl):
            RssReader().read("https://rss-feed-flowpodcast-2eqj3-ue.a.run.app/feed/rss")

    def test_should_read_b9_rss_and_return_a_list_of_episodes(self):
        episodes = RssReader().read("https://feeds.simplecast.com/AZQtlzze")
        self.assertGreaterEqual(len(episodes), 346)
