import os
import io
import boto3
import json
import csv
import base64

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
sagemaker = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    payload = json.loads(json.dumps(event['body']))

    if "isBase64Encoded" in event:
        payload = base64.b64decode(payload)

    response = sagemaker.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)

    result = response['Body'].read().decode();

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            },
        'body': result
    };
