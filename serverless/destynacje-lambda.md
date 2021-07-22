```
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

lambdaClient = boto3.client('lambda')

def lambda_handler(event, context):

    file = (int)(event['Records'][0]['s3']['object']['key'][0:-4])

    logger.info('New File Detected!');
    logger.info('File: %s', file);
    
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("items")
    table.put_item(
        Item={
            'file' : file
        }
    )

    return "OK";
```