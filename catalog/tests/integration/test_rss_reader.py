from unittest import TestCase

from catalog.src.exceptions import InvalidRssUrl
from catalog.src.rss_reader import RssReader


class Test(TestCase):

    def test_should_read_flow_rss_and_return_a_list_of_episodes(self):
        rss = RssReader("https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rss")
        episodes = rss.read()
        self.assertGreaterEqual(len(episodes), 305)

    def test_should_raise_when_given_a_invalid_rss_url(self):
        with self.assertRaises(InvalidRssUrl):
            rss = RssReader("https://rss-feed-flowpodcast-2eqj3fl3la-ue.a.run.app/feed/rs")
            rss.read()

    def test_should_read_b9_rss_and_return_a_list_of_episodes(self):
        rss = RssReader("https://feeds.simplecast.com/AZQtlzze")
        episodes = rss.read()
        self.assertGreaterEqual(len(episodes), 346)
