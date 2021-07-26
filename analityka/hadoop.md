```
hadoop fs -cp  s3://cloudbuildersday/lab-bigdata /bigdata
```

```
hive
```


```
CREATE EXTERNAL TABLE IF NOT EXISTS chmurolandia_dane (
 `id` int,
 `age` int,
 `firstname` string,
 `lastname` string,
 `country` string,
 `sex` string,
 `numberofkids` int,
 `revenue` double,
 `leavingincity` string,
 `likemusic` string,
 `likecinema` string,
 `bankbalance` double,
 `happinnessratio` double,
 `height` int,
 `weight` int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
) LOCATION '/bigdata';
```


```
-- sprawdz 10 wierszy
SELECT * FROM chmurolandia_dane limit 10;

-- jaka jest calkowita ilosc wierszy w plikach?
SELECT count(*) FROM chmurolandia_dane;

-- jaka jest ilosc wierszy w plikach, per kraj, posortowane po ilosci wierszy?
SELECT country, count(*) num FROM chmurolandia_dane group by country order by num desc;

```