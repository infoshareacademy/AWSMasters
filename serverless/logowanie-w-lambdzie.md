
```
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

lambdaClient = boto3.client('lambda')

def lambda_handler(event, context):

    logger.info('New Execution');
    logger.info('Input event: %s', event);

    name = event["name"]
    logger.info('Name: %s', name);
    
    response = "Hello " + name + "!";
    
    logger.info('Response: %s', response);

    return response;
```