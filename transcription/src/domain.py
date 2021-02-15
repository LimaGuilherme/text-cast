from catalog.src.protos import something_pb2, something_pb2_grpc


class TranscriptionDeleteServicer(something_pb2_grpc.DeleteEpisodeTranscriptionServicer):

    def DeleteTranscriptions(self, request, context):
        return something_pb2.DeleteReply(response='success')
