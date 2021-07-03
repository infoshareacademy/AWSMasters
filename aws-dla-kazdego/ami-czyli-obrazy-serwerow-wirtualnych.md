
```
sudo yum update -y
sudo yum install php httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd

sudo su
cd /var/www/html
aws s3 cp --no-sign-request s3://tomash-public/examples/heman/index.php .
```
