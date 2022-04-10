```
aws ec2 run-instances \
    --image-id ami-01720b5f421cf0179  \
    --instance-type t2.nano \
    --subnet-id REPLACE_ME \
    --security-group-ids REPLACE_ME \
    --key-name REPLACE_ME \
    --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=Tester}]"
```
