class Transcription:

    def __init__(
            self,
            podcast_id: str,
            episode_id: str,
            transcription: str,
            _id: str = None
    ) -> None:

        self._podcast_id = podcast_id
        self._episode_id = episode_id
        self._transcription = transcription
        self._id = _id

    @property
    def podcast_id(self):
        return self._podcast_id

    @property
    def episode_id(self):
        return self._episode_id

    @property
    def transcription(self):
        return self.transcription

    @property
    def id(self):
        return self._id
