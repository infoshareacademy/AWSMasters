```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "limitedSize",
      "Effect": "Deny",
      "Action": "ec2:RunInstances",
      "Resource": "arn:aws:ec2:*:*:instance/*",
      "Condition": {
        "ForAnyValue:StringNotLike": {
          "ec2:InstanceType": [
            "*.nano",
            "*.small",
            "*.micro",
            "*.medium"
          ]
        }
      }
    }
  ]
}
```