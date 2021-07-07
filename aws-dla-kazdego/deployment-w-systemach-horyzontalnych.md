Nowy fragment skryptu User Data
```
sudo yum install ruby -y
sudo yum install wget
cd /home/ec2-user
wget https://aws-codedeploy-eu-west-1.s3.amazonaws.com/latest/install
sudo chmod +x install
sudo ./install auto
```


Pobranie kodów źródłowych nowej wersji aplikacji
```

cd ~/environment
mkdir myapp
cd myapp
aws s3 cp s3://tomash-aws-masters/content/heman-app.zip .
unzip heman-app.zip
rm heman-app.zip

```

Utworzenie nowego bucketu S3
```

aws s3 mb s3://REPLACEME

```

Spakowanie i przesłanie aplikacji do S3.
```

cd ~/environment
cd myapp
zip -r heman-app.zip .
aws s3 cp heman-app.zip s3://REPLACEME/heman-app.zip
rm heman-app.zip

```
