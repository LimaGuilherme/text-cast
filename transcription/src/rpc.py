import grpc

from concurrent import futures

from transcription.src.domain import TranscriptionDeleteServicer
from transcription.src.protos import something_pb2_grpc


def serve():
    while True:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        something_pb2_grpc.add_DeleteEpisodeTranscriptionServicer_to_server(TranscriptionDeleteServicer(), server)
        server.add_insecure_port('0.0.0.0:8080')
        server.start()
        server.wait_for_termination()
        print('API server started. Listening at 0.0.0.0:8080.')
