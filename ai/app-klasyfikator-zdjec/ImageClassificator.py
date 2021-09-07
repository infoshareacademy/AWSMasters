import json
import boto3
import time

sagemakerRuntime = boto3.client('sagemaker-runtime')
s3 = boto3.resource('s3')

def lambda_handler(event, context):

    time.sleep(2)

    categories = event["categories"].split(" ");
    endpoint = event["endpointName"]
    bucket = "REPLACEME_NAZWA_TWOJEGO_BUCKET_S3"
    image = "validate.png";

    s3.meta.client.download_file(bucket, image, "/tmp/"+image)

    img = open("/tmp/"+image, 'rb').read()

    response = sagemakerRuntime.invoke_endpoint(
        EndpointName=endpoint,
        ContentType='application/x-image',
        Body=bytearray(img)
    )

    result = response['Body'].read()
    result = json.loads(result)

    items = []
    categoryScore = 0
    it = -1
    for score in result:
        it = it + 1;
        if (score > categoryScore):
            categoryScore = score
            category = categories[it];

        item = {"category": categories[it], "score":score}
        items.append(item);

    print(category);
    print(categoryScore);


    return {
        'winner': category,
        'score':categoryScore,
        'items' : items
    }
