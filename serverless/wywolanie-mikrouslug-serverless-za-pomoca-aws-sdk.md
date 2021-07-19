Wywołanie funkcji lambda za pomocą AWS CLI
```
aws lambda invoke --function-name HelloWorld response.json
```

Wywołanie lambdy za pomocą AWS SDK for python
```
import boto3
import json
client = boto3.client('lambda')

response = client.invoke(
    FunctionName='HelloWorld',
    InvocationType='RequestResponse'
)

print(json.load(response['Payload']));
```

Wywołanie funkcji lambda za pomocą AWS CLI z parami wejsciowymi
```
aws lambda invoke --function-name HelloWorld --payload '{ "name": "YOUR_NAME" }' response.json
```

Wywołanie lambdy za pomocą AWS SDK for python z parametrami wejsciowymi
```
import boto3
import json
client = boto3.client('lambda')

inputParams = {
    "name":"YOUR_NAME"
}

response = client.invoke(
    FunctionName='HelloWorld',
    Payload = json.dumps(inputParams),
    InvocationType='RequestResponse'
)

print(json.load(response['Payload']));
```