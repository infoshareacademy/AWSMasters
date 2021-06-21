Pierwsze kroki z AWS CLI:

```
aws iam list-users

aws ec2 describe-instances

aws ec2 describe-instances --query "Reservations[*].Instances[*].InstanceId"

aws ec2 describe-instances --query "Reservations[*].Instances[*].InstanceId" --output table

aws sts get-caller-identity --query Arn
```
