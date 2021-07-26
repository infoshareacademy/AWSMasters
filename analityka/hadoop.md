```
hadoop fs -cp  s3://cloudbuildersday/lab-bigdata /bigdata
```

```
hive
```

```
-- sprawdz 10 wierszy
SELECT * FROM chmurolandia_dane limit 10;

-- jaka jest calkowita ilosc wierszy w plikach?
SELECT count(*) FROM chmurolandia_dane;

-- jaka jest ilosc wierszy w plikach, per kraj, posortowane po ilosci wierszy?
SELECT country, count(*) num FROM chmurolandia_dane group by country order by num desc;

```