
```
aws s3 mb s3://awsmasters-analityka-tst
```

```
aws s3 cp s3://cloudbuildersday/lab-bigdata/ s3://awsmasters-analityka-tst/bigdata --recursive
aws s3 cp s3://cloudbuildersday/lab-bigdata-with-header/ s3://awsmasters-analityka-tst/bigdata-with-header --recursive
```


```
aws s3 cp s3://athena-examples/elb/raw/ s3://awsmasters-analityka-tst/bigdata-huge --recursive
```