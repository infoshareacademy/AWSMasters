
```
cd ~/environment
mkdir pas-app
cd pas-app
aws s3 cp s3://tomash-aws-masters/content/my-php-app.zip .
unzip my-php-app.zip
rm my-php-app.zip
```

```
cd ~/environment/pas-app
zip -r my-php-app.zip .
```
