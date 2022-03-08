# Case Study 2 SE Project (Mulya and Tito)
This repository contains several files on how to import or load the data contained in the .csv file into the database we created, so we don't need to enter the data in the .csv file one by one into our database.

In this repository there are several files, such as covid.csv (as an example of a .csv file to be imported), StudiKasus2.py (as a .py file containing the StudiKasus2 class with several functions in it), main.py (as a .py file that aims to run or call functions in the StudiKasus2.py file), and there are requirements.txt (which contains all the python libraries needed for this project).

## Installation

This project can basically be run on any computer by opening and running the main.py file with the desired Python IDE e.g. PyCharm, Visual Studio Code, etc.

But if you want to develop it again with the same settings as the developer had, you can easily create a virtual environment using the below methods (if you are not using PyCharm). Actually, you can use other methods and the below methods are not required to be followed.

```bash
python3 -m venv venv
```

Activate the virtual environment for Linux

```bash
. venv/bin/activate
```

Activate the virtual environment for Windows

```bash
. venv/Scripts/activate
```

Install the required libraries/packages for this project

```bash
pip3 install -r requirements.txt
```

## Usage 
### StudiKasus2.py

Import the required libraries

```python
import mysql.connector as mysql
from mysql.connector import Error
import sqlalchemy
from urllib.parse import quote_plus as urlquote
import pandas as pd
```

StudiKasus2 class contains several functions

```python
class StudiKasus2:
```

__init__ function is used to connect to the database

```python
def __init__(self, host, port, user, password):
        
    self.host = host
    self.port = port
    self.user = user
    self.password = password
```

create_db function is used to create a database

```python
def create_db(self, db_name):
        
    conn = mysql.connect(
        host=self.host,
        port=self.port,
        user=self.user,
        passwd=self.password
    )
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE {}".format(db_name))
    except Error as e:
        print("Error while connecting to MySQL", e)
```

create_table function is used to create a table in a database that was previously created and load the data from the imported .csv file (that already become dataframe) into the database

```python
def create_table(self, db_name, table_name, df):

    conn = mysql.connect(
        host=self.host,
        port=self.port,
        user=self.user,
        passwd=self.password
    )
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("USE {}".format(db_name))
            cursor.execute("CREATE TABLE {}".format(table_name))
    except Error as e:
        print("Error while connecting to MySQL", e)

    engine_stmt = 'mysql+mysqldb://%s:%s@%s:%s/%s' % (self.user, urlquote(self.password),
                                                      self.host, self.port, db_name)
    engine = sqlalchemy.create_engine(engine_stmt)

    df.to_sql(name=table_name, con=engine,
              if_exists='append', index=False, chunksize=1000)
```

load_data function is used to load existing data in a previously created database

```python
def load_data(self, db_name, table_name):
        
    conn = mysql.connect(
        host=self.host,
        port=self.port,
        user=self.user,
        passwd=self.password
    )
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM {}.{}".format(db_name, table_name))
            result = cursor.fetchall()
            return result
    except Error as e:
        print("Error while connecting to MySQL", e)
```

import_csv function is used to import/read data in a .csv file and save it as a dataframe

```python
def import_csv(self, path):
        
    return pd.read_csv(path, index_col=False, delimiter=',')
```

### main.py

Import StudiKasus2.py to run/use all its functions

```python
import StudiKasus2
import os
```

To call and use all the functions in StudiKasus2.py

```python
if __name__ == "__main__":
    case = StudiKasus2.StudiKasus2("localhost", "3306", "root", os.environ["MySQL_Pswd"]) #connect to database
    df = case.import_csv("covid.csv") #save the .csv file data in a df value
    print(case.create_db("covidCase1")) #create a database
    print(case.create_table("covidCase1", "case1", df)) #create a table in a database
    print(case.load_data("covidCase1", "case1")) #load the data in a database
```

To view the documentation of the project

```python
print(help(StudiKasus2))
```

Result of the above code

```
'$', 14000000, 1565000000), ('Exports', 2021, '16/05/2021', 'Sunday', 'China', 'Meat and edible offal', 'All', '$', 4000000, 1569000000), ('Exports', 2021, '17/05/2021', 'Monday', 'China', 'Meat and edible offal', 'All', '$', 7000000, 1576000000), ('Exports', 2021, '18/05/2021', 'Tuesday', 'China', 'Meat and edible offal', 'All', '$', 6000000, 1582000000), ('Exports', 2021, '19/05/2021', 'Wednesday', 'China', 'Meat and edible offal', 'All', '$', 4000000, 1586000000), ('Exports', 2021, '20/05/2021', 'Thursday', 'China', 'Meat and edible offal', 'All', '$', 15000000, 1601000000), ('Exports', 2021, '21/05/2021', 'Friday', 'China', 'Meat and edible offal', 'All', '$', 13000000, 1614000000), ('Exports', 2021, '22/05/2021', 'Saturday', 'China', 'Meat and edible offal', 'All', '$', 5000000, 1619000000), ('Exports', 2021, '23/05/2021', 'Sunday', 'China', 'Meat and edible offal', 'All', '$', 26000000, 1646000000), ('Exports', 2021, '24/05/2021', 'Monday', 'China', 'Meat and edible offal', 'All', '$', 14000000, 1660000000), ('Exports', 2021, '25/05/2021', 'Tuesday', 'China', 'Meat and edible offal', 'All', '$', 8000000, 1667000000), ('Exports', 2021, '26/05/2021', 'Wednesday', 'China', 'Meat and edible offal', 'All', '$', 7000000, 1675000000), ('Exports', 2021, '27/05/2021', 'Thursday', 'China', 'Meat and edible offal', 'All', '$', 3000000, 1678000000), ('Exports', 2021, '28/05/2021', 'Friday', 'China', 'Meat and edible offal', 'All', '$', 12000000, 1689000000), ('Exports', 2021, '29/05/2021', 'Saturday', 'China', 'Meat and edible offal', 'All', '$', 7000000, 1697000000), ('Exports', 2021, '30/05/2021', 'Sunday', 'China', 'Meat and edible offal', 'All', '$', 4000000, 1701000000), ('Exports', 2021, '31/05/2021', 'Monday', 'China', 'Meat and edible offal', 'All', '$', 18000000, 1719000000), ('Exports', 2021, '01/06/2021', 'Tuesday', 'China', 'Meat and edible offal', 'All', '$', 10000000, 1729000000), ('Exports', 2021, '02/06/2021', 'Wednesday', 'China', 'Meat and edible offal', 'All', '$', 3000000, 1732000000), ('Exports', 2021, '03/06/2021', 'Thursday', 'China', 'Meat and edible offal', 'All', '$', 18000000, 1750000000), ('Exports', 2021, '04/06/2021', 'Friday', 'China', 'Meat and edible offal', 'All', '$', 6000000, 1756000000), ('Exports', 2021, '05/06/2021', 'Saturday', 'China', 'Meat and edible offal', 'All', '$', 15000000, 1770000000), ('Exports', 2021, '06/06/2021', 'Sunday', 'China', 'Meat and edible offal', 'All', '$', 19000000, 1790000000), ('Exports', 2021, '07/06/2021', 'Monday', 'China', 'Meat and edible offal', 'All', '$', 14000000, 1804000000), ('Exports', 2021, '08/06/2021', 'Tuesday', 'China', 'Meat and edible offal', 'All', '$', 8000000, 1812000000), ('Exports', 2021, '09/06/2021', 'Wednesday', 'China', 'Meat and edible offal', 'All', '$', 2000000, 1814000000), ('Exports', 2021, '10/06/2021', 'Thursday', 'China', 'Meat and edible offal', 'All', '$', 12000000, 1826000000), ('Exports', 2021, '11/06/2021', 'Friday', 'China', 'Meat and edible offal', 'All', '$', 5000000, 1831000000), ('Exports', 2021, '12/06/2021', 'Saturday', 'China', 'Meat and edible offal', 'All', '$', 7000000, 1838000000), ('Exports', 2021, '13/06/2021', 'Sunday', 'China', 'Meat and edible offal', 'All', '$', 15000000, 1853000000), ('Exports', 2021, '14/06/2021', 'Monday', 'China', 'Meat and edible offal', 'All', '$', 17000000, 1870000000), ('Exports', 2021, '15/06/2021', 'Tuesday', 'China', 'Meat and edible offal', 'All', '$', 22000000, 1892000000), ('Exports', 2021, '16/06/2021', 'Wednesday', 'China', 'Meat and edible offal', 'All', '$', 7000000, 1899000000), ...

Help on module StudiKasus2:

NAME
    StudiKasus2

CLASSES
    builtins.object
        StudiKasus2
    
    class StudiKasus2(builtins.object)
     |  StudiKasus2(host, port, user, password)
     |  
     |  This class is used to import data in the form of a .csv file into the database
     |  
     |  Methods defined here:
     |  
     |  __init__(self, host, port, user, password)
     |      This function is used to connect to the database
     |      
     |      :param host: this is the database host
     |      :param port: this is the database port
     |      :param user: this is the database user
     |      :param password: this is the database user password
     |  
     |  create_db(self, db_name)
     |      This function is used to create a database
     |      
     |      :param db_name: this is the desired database name
     |      
     |      :return: a database according to the name entered in the parameter
     |  
     |  create_table(self, db_name, table_name, df)
     |      This function is used to create a table in a database that was previously
     |      created and load the data from the imported .csv file
     |      (that already become dataframe) into the database
     |      
     |      :param db_name: this is the desired database name
     |      :param table_name: this is the desired table name
     |      :param df: this is the dataframe from the imported .csv file
     |      
     |      :return: a table in the previously created database and table name
     |      according to the name entered in the parameter
     |  
     |  import_csv(self, path)
     |      This function is used to import/read data in a .csv file and save it as a dataframe
     |      
     |      :param path: this is the path of the .csv file or if it is
     |      in the same folder we can just enter the .csv filename
     |      
     |      :return: a data from the .csv file in a dataframe format
     |  
     |  load_data(self, db_name, table_name)
     |      This function is used to load existing data in a previously created database
     |      
     |      :param db_name: this is the name of the database whose data we want to load
     |      :param table_name: this is the name of the table in the database whose data we want to load
     |      
     |      :return: a data from the database/table whose data we want to load
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
```
