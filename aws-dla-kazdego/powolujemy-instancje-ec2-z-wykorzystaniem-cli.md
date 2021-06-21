
Uruchomienie serwera EC2 z wykorzystaniem CLI
```
aws ec2 run-instances \
    --image-id ami-01720b5f421cf0179  \
    --instance-type t2.nano \
    --subnet-id REPLACE_ME \
    --security-group-ids REPLACE_ME \
    --key-name REPLACE_ME \
    --monitoring Enabled=true \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=Tester}]" \
    --user-data file://userdata.txt
```

Zawartość pliku userdata.txt
```
#!/bin/bash
sudo yum update -y
sudo yum install php httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
sudo su

cat <<EOF> /var/www/html/index.html
<html>
	<body>
    <br/><br/><br/>
    <div style="text-align:center;">
      <img src="https://awspoland.s3-eu-west-1.amazonaws.com/cloud.png" align="middle">
      <h1> Cloudy page!!!</h1>
    </div>
	</body>
</html>
EOF
```
