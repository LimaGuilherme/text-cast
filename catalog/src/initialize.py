
from catalog.src import web_app as web_app_module
from catalog.src import configurations as config_module
from catalog.src import endpoints
from catalog.src.application_service import PodcastService
from catalog.src.domain import DomainService
from catalog.src.infrascructure.cache import CacheRepository
from catalog.src.infrascructure.mongodb_repository import create_repository
from catalog.src.rss_reader import RssReader

web_app = web_app_module.get_web_app()
api = web_app_module.get_api()
configurations = config_module.get_config()

cache_repository = CacheRepository()
rss_reader = RssReader()
mongodb_repository = create_repository(configurations)
domain_service = DomainService()

podcast_service = PodcastService(mongodb_repository, rss_reader, cache_repository, domain_service)


endpoints.register(
    podcast_service=podcast_service
)
