from src import web_app as web_app_module, configurations as config_module, endpoints
from src import aws as aws_module
from src import PodcastService, TranscribeService
from src.domain import DomainService
from src.infrascructure import CacheRepository
from src.infrascructure import create_repository
from src.rss_reader import RssReader
from src.transcribe import AWSTranscribe

web_app = web_app_module.get_web_app()
api = web_app_module.get_api()
configurations = config_module.get_config()
transcribe_client = aws_module.get_transcribe_client()
s3_client = aws_module.get_s3_client()

cache_repository = CacheRepository()
rss_reader = RssReader()
mongodb_repository = create_repository(configurations)
domain_service = DomainService()
aws_transcribe = AWSTranscribe(transcribe_client)

podcast_service = PodcastService(mongodb_repository, rss_reader, cache_repository, domain_service)
transcribe_service = TranscribeService(aws_transcribe, s3_client)

endpoints.register(
    podcast_service=podcast_service,
    transcribe_service=transcribe_service
)
