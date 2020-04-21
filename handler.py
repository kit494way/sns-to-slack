import json
import os
from base64 import b64decode

import boto3
import requests


def sns_message_to_slack(event, context):
    message = event["Records"][0]["Sns"]["Message"]
    subject = event["Records"][0]["Sns"]["Subject"]

    if subject:
        payload = {
            "text": subject,
            "blocks": [
                {"type": "section", "text": {"text": message, "type": "mrkdwn"}}
            ],
        }
    else:
        payload = {"text": message}

    webhook = (
        boto3.client("kms")
        .decrypt(CiphertextBlob=b64decode(os.environ["ENCRYPTED_SLACK_WEBHOOK"]))[
            "Plaintext"
        ]
        .decode("utf-8")
        .strip()
    )

    requests.post(webhook, json=payload)

    response = {"statusCode": 200, "body": ""}

    return response
