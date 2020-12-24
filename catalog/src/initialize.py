
from catalog.src import web_app as web_app_module
from catalog.src import configurations as config_module
from catalog.src import endpoints
from catalog.src.application_service import PodcastService
from catalog.src.repositories import create_repository
from catalog.src.rss_reader import RssReader

web_app = web_app_module.get_web_app()
api = web_app_module.get_api()
configurations = config_module.get_config()

rss_reader = RssReader()
repository = create_repository(configurations, rss_reader)

podcast_service = PodcastService(repository)


endpoints.register(
    podcast_service=podcast_service
)
