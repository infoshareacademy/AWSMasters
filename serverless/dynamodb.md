```
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("s3objects")
table.put_item(
    Item={
        'name' : REPLACE_ME
    }
)
```

Link: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html