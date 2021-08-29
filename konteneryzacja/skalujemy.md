
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


@app.route("/pi")
def pi():

    pi = 0
    n = 4
    d = 1

    for i in range(1,10000):
        a = 2 * (i % 2)
        pi += a * n / d
        d += 2


    return "Pi: " + str(pi)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))
    app.run(debug=True,host='0.0.0.0',port=port)

```