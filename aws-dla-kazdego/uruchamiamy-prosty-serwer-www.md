Skrypt user-data dla serwera EC2:

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
      <img src="https://tomash-aws-masters.s3.eu-west-1.amazonaws.com/graphics/logo.png" align="middle">
      <h1> Pierwszy serwer w chmurze!!! </h1>
    </div>
	</body>
</html>
EOF
```
