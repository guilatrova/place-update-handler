from typing import Any

from aws_lambda_powertools.utilities.batch import sqs_batch_processor
from aws_lambda_powertools.utilities.parser import parse
from aws_lambda_powertools.utilities.parser.models import SqsRecordModel
from aws_lambda_powertools.utilities.typing import LambdaContext
from rich import inspect

from place_update_handler.models import PlaceUpdateEvent
from place_update_handler.storages import save

LAMBDA_EVENT_TYPE = dict[str, Any]
OK_RESPONSE = {"statusCode": 200}


def handle_individual_record(record: dict):
    inspect(record)

    sqs_record = parse(model=SqsRecordModel, event=record)
    place_event = parse(model=PlaceUpdateEvent, event=PlaceUpdateEvent)
    place_id = sqs_record.messageAttributes["place_id"].stringValue

    save(place_id, place_event)


@sqs_batch_processor(record_handler=handle_individual_record)
def on_receive_place_update_event(event: dict[str, Any], context: LambdaContext):
    return OK_RESPONSE
