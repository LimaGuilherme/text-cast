import boto3

transcribe_client = None
s3_client = None


def get_transcribe_client():
    global transcribe_client

    if not transcribe_client:
        transcribe_client = boto3.client(
            'transcribe',
            aws_session_token='mine'
        )

    return transcribe_client


def get_s3_client():
    global s3_client

    if not s3_client:
        s3_client = boto3.client(
            's3',
            aws_session_token='mine'
        )

    return s3_client
