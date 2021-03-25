import grpc

from src import something_pb2, something_pb2_grpc


class DomainService(object):

    def __init__(self):
        self.something_pb2 = something_pb2
        self.channel = grpc.insecure_channel('0.0.0.0:8080')
        self.stub = something_pb2_grpc.DeleteEpisodeTranscriptionStub(self.channel)

    def delete_transcriptions(self, podcast_id):
        request = something_pb2.DeleteRequest(
            podcast_id=podcast_id,
            episode_id='asadasdas'
        )

        try:
            response = self.stub.DeleteTranscriptions(request)
            print('User fetched.')
            print(response)
        except grpc.RpcError as err:
            print(err.details())
            print('{}, {}'.format(err.code().name, err.code().value))  # pylint: disable=no-member
