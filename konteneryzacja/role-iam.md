
```
from flask import Flask
from flask import request
import os
import boto3
import uuid
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    return "AWS Masters!"


@app.route("/add")
def add():

    user = request.args.get('user')
    message = request.args.get('message')

    app.logger.info('Adding new item!')
    app.logger.info('User: %s', user)
    app.logger.info('Message: %s', message)

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("messages")
    table.put_item(
        Item={
            'id' : str(uuid.uuid4()),
            'user' : user,
            'message' : message
        }
    )

    return "Added!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True,host='0.0.0.0',port=port)

```