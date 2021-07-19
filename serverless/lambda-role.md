```
import json
import boto3
import urllib.request

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    image_link = "https://tomash-aws-masters.s3.eu-west-1.amazonaws.com/content/unicorn.png"
    name = "unicorn.png"
    bucket = "a-chmurowy-wehikul";
    
    urllib.request.urlretrieve(image_link, '/tmp/' + name)
    s3.upload_file('/tmp/' + name, bucket, name)
    
    return "OK"
```