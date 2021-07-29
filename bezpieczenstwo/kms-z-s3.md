
```
aws s3 cp s3://tomash-aws-masters/graphics/unicorn.png unicorn.png
```

```
aws s3 cp unicorn.png s3://REPLACEME/unicorn-plain.png
```

```
aws s3 cp unicorn.png s3://REPLACEME/kms/unicorn-plain-public.png --acl public-read
```

```
aws s3 cp unicorn.png s3://REPLACEME/unicorn-plain-public-sse.png --acl public-read --sse 
```

```
aws s3 cp unicorn.png s3://REPLACEME/unicorn-plain-public-sse-cmk.png --acl public-read --sse aws:kms --sse-kms-key-id KEYREPLACEME
```

```
aws s3 cp unicorn.png s3://REPLACEME/unicorn-plain-public-sse-ownkey.png --acl public-read --sse-c --sse-c-key 12345678901234567890123456789012
```