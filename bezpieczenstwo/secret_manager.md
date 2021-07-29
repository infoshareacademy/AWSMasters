
```
import boto3

def get_secret(secret_name):


    client = boto3.client('secretsmanager')
    secret = client.get_secret_value(SecretId=secret_name)['SecretString']
    print(secret);
    
get_secret("REPLACEME");

```