import feedparser

from src.entity import Episode
from src import InvalidRssUrl


class RssReader:

    def read_episodes(self, rss: str):
        episodes = []

        feed = feedparser.parse(rss)
        self.__check_feed_status(feed)

        for entry in feed.entries:
            episodes.append(Episode(name=entry.title,
                                    podcast=feed.feed.title,
                                    image=self.__scrap_image_entry(entry),
                                    description=entry.summary,
                                    audio=self.__scrap_audio_entry(entry.links)
                                    )
                            )
        return episodes

    def read_podcast(self, rss: str):
        feed = feedparser.parse(rss)
        self.__check_feed_status(feed)
        return {'name': feed.feed.title, 'image': feed.feed.image['href']}

    def __check_feed_status(self, feed):
        if feed.bozo:
            bozo_exception = feed.bozo_exception.getMessage()
            if bozo_exception == 'not well-formed (invalid token)':
                raise InvalidRssUrl

    def __scrap_image_entry(self, entry):
        try:
            return entry.image['href']
        except AttributeError:
            return None

    def __scrap_audio_entry(self, entry_links):
        for entry_link in entry_links:
            if entry_link['type'] == 'audio/mpeg':
                return entry_link['href']
        return None
