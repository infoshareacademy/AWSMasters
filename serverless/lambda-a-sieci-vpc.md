```
#!/bin/bash
sudo yum update -y
sudo yum install php httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd

sudo su
aws s3 cp --no-sign-request s3://tomash-aws-masters/content/unicorn.png /var/www/html/unicorn.png
```