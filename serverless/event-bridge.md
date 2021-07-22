
```
import json
import boto3
import uuid
from datetime import datetime

ddb = boto3.resource('dynamodb')
    
def lambda_handler(event, context):

    ts = (int)(datetime.now().timestamp())
    
    message = ''
    source = ''
    
    table = ddb.Table('events')
    table.put_item(
        Item={
            'timestamp': (str)(ts),
            'date' : datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'),
            'source' : source,
            'message' : message
        });
        
                        
    return "OK"
```


```
import boto3

client = boto3.client('events')


client.put_events(
    Entries=[
        {
            'Source': 'awsmasters-app',
            'DetailType' : 'new-user',
            'Detail': '{"author":"Tomasz","city":"Warsaw"}',
            'EventBusName': 'my-bus'
        },
    ]
);
```