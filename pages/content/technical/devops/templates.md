---
title: Templates
weight: 1
---

Tmplates for all sorts of things...

AWS
---

### S3 bucket access IAM policy
Used to lock down an IAM user to just one bucket for Wordpress backup plugins.

```json
{
"Version": "2012-10-17",
"Statement": [
{
"Effect": "Allow",
"Action": [
"s3:ListBucket",
"s3:GetBucketLocation",
"s3:ListBucketMultipartUploads"
],
"Resource": "arn:aws:s3:::<bucket name>",
"Condition": {}
},
{
"Effect": "Allow",
"Action": [
"s3:AbortMultipartUpload",
"s3:DeleteObject",
"s3:DeleteObjectVersion",
"s3:GetObject",
"s3:GetObjectAcl",
"s3:GetObjectVersion",
"s3:GetObjectVersionAcl",
"s3:PutObject",
"s3:PutObjectAcl",
"s3:PutObjectAclVersion"
],
"Resource": "arn:aws:s3:::<bucket name>/*",
"Condition": {}
},
{
"Effect": "Allow",
"Action": "s3:ListAllMyBuckets",
"Resource": "*",
"Condition": {}
}
]
}
```

Vault
-----

### Template for new policy

To restrict access to read-only for a given st of secrets...

```json
TO DO
```
