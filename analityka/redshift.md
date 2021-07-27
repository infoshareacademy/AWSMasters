
```
CREATE SCHEMA awsmasters
```

```
 CREATE TABLE awsmasters.people (
   id  integer,
   age  integer,
   firstname  varchar(20),
   lastname  varchar(20),
   country  varchar(20),
   sex  varchar(20),
   numberofkids  integer,
   revenue  real,
   leavingincity  varchar(20),
   likemusic  varchar(20),
   likecinema  varchar(20),
   bankbalance  real,
   happinnessratio  real,
   height  integer,
   weight  integer
 );
```

```
 COPY awsmasters.people FROM 's3://REPLACE/bigdata-with-header'
 iam_role 'REPLACE'
 CSV
 IGNOREHEADER 1
 ```