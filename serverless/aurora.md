```
wget http://cdn.mysql.com/Downloads/Connector-Python/mysql-connector-python-2.0.4.zip#md5=3df394d89300db95163f17c843ef49df
unzip mysql-connector-python-2.0.4.zip
cd mysql-connector-python-2.0.4
sudo python3 setup.py install
```

```
aws s3 cp s3://cloudbuildersday/lab-bigdata . --recursive
```


```
import mysql.connector
import os

mydb = mysql.connector.connect(
  host="REPLACEME",
  user="REPLACEME",
  password="REPLACEME"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE bigdata")
mycursor.execute("USE bigdata")
mycursor.execute("CREATE TABLE bigdata.people ( id INTEGER, age INTEGER, firstname VARCHAR(255), lastname VARCHAR(255), country VARCHAR(255), sex VARCHAR(255), numberofkids INTEGER, revenue DOUBLE, leavingincity VARCHAR(255), likemusic VARCHAR(255), likecinema VARCHAR(255), bankbalance DOUBLE, happinnessratio DOUBLE, height INT, weight INT )")
mycursor.execute("COMMIT");
```

```
import mysql.connector
import os


def load_data():
    mydb = mysql.connector.connect(
      host="REPLACEME",
      user="REPLACEME",
      password="REPLACEME"
    )
    
    
    mycursor = mydb.cursor()
    mycursor.execute("USE bigdata")
    
    directory = os.fsencode("data")
        
    limit = 0
    for file in os.listdir(directory):
        limit = limit+1
        if (limit < 5):
            filename = "data/" + os.fsdecode(file)
            print(filename);
            
        
            with open(filename) as f:
                for line in f:
                    line = line.strip()
                    attributes = line.split(",")
                    mycursor.execute("INSERT INTO people VALUES ('" + attributes[0] + "','" + attributes[1] + "','" + attributes[2] + "','" + attributes[3] + "','" + attributes[4] + "','" + attributes[5] + "','" + attributes[6] + "','" + attributes[7] + "','" + attributes[8] + "','" + attributes[9] + "','" + attributes[10] + "','" + attributes[11] + "','" + attributes[12] + "','" + attributes[13] + "','" + attributes[14] + "')");
            
    mycursor.execute("COMMIT");
    
    
load_data();
```