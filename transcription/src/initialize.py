from transcription.src import web_app as web_app_module
from transcription.src import rpc

web_app = web_app_module.get_web_app()
api = web_app_module.get_api()

rpc.serve()
