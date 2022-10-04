from aws_lambda_powertools.utilities.data_classes.cloud_watch_logs_event import CloudWatchLogsEvent
from aws_lambda_powertools.utilities.data_classes.kinesis_stream_event import KinesisStreamRecordPayload


def kinesis_to_cw_event(kinesis_payload: KinesisStreamRecordPayload) -> CloudWatchLogsEvent:
    """Converts a Cloudwatch Log received from Kinesis to a standard CloudWatchLogEvent"""
    payload = kinesis_payload.data_as_bytes()
    wrapped = {"awslogs": {"data": payload}}
    return CloudWatchLogsEvent(wrapped)
