```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyOutsideIreland",
      "Effect": "Deny",
      "NotAction": [
        "aws-portal:*",
        "lightsail:*",
        "awsbillingconsole:*",
        "iam:*",
        "sts:*",
        "health:*",
        "support:*",
        "budgets:*",
        "cloudfront:*",
        "organizations:*",
        "trustedadvisor:*",
        "shield:*",
        "waf:*",
        "waf-regional:*",
        "cloudformation:*",
        "route53:*",
        "route53domains:*",
        "tag:*",
        "resource-groups:*",
        "ssm:ListAssociations",
        "s3:Get*",
        "s3:List*",
        "s3:Head*",
        "glacier:List*",
        "glacier:Describe*",
        "glacier:Get*",
        "acm:*",
        "console:*",
        "aws-portal:*",
        "budgets:*",
        "ce:*",
        "cur:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "aws:RequestedRegion": [
            "eu-west-1"
          ]
        }
      }
    }
  ]
}
```