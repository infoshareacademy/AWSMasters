
```
mkdir data 
mkdir archived
aws s3 cp s3://cloudbuildersday/lab-bigdata-with-header/ data --recursive
```

```
import gzip
import os

for filename in os.listdir("data"):
    f = open("data/" + filename, "rb")
    data = f.read()
    bindata = bytearray(data)
    with gzip.open("archived/" + filename + ".gz", "wb") as f:
        f.write(bindata)
```



```
mkdir data 
mkdir archived
aws s3 cp archived/ s3://awsmasters-analityka-tst/bigdata-with-header-archived --recursive
```