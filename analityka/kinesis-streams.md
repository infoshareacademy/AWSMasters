

```
{
    "name": "{{name.firstName}}",
    "lastname": "{{name.lastName}}",
    "date": "{{date.now("dddd, MMMM Do YYYY, h:mm:ss a")}}",
    "sensorId": {{random.number(50)}},
    "currentTemperature": {{random.number(
        {
            "min":10,
            "max":150
        }
    )}},
    "status": "{{random.arrayElement(
        ["OK","FAIL","WARN"]
    )}}"
}
```

```
import json
import base64
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    print("EVENT");
    print(event);
    
    records = event["Records"]
    
    for record in records:
        sequenceNumber = record["kinesis"]["sequenceNumber"]
        decodedData = base64.b64decode(record["kinesis"]["data"]).decode("utf-8")
        sendData = json.loads(decodedData)
        
        table = dynamodb.Table("streamevents")
        table.put_item(
            Item={
                'sequenceNumber' : sequenceNumber,
                'name' : sendData["name"],
                'lastname' : sendData["lastname"],
                'data' : sendData["date"],
                'sensorId' : sendData["sensorId"],
                'currentTemperature' : sendData["currentTemperature"],
                'status' :  sendData["status"]
            }
        )
        
    
    return "OK"
```