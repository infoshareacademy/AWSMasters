Uruchomienie nowego serwera DDoS-owego

```
aws ec2 run-instances \
    --image-id ami-0aef57767f5404a3c  \
    --instance-type c5.large \
    --subnet-id REPLACE_ME \
    --security-group-ids REPLACE_ME \
    --key-name workshop \
    --monitoring Enabled=true \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=DDOS-er}]"
```

Dodanie nowego pliku do strony
```
aws s3 cp --no-sign-request s3://tomash-public/examples/php/pi.php .
```

Komendy do zainstalowania Apache Bench i przeprowadzenia ataku
```
sudo su
apt-get update
apt-get install apache2-utils -y
ab -V

ab -n 100000 -c 500 ENDPOINT
```
