# CaseStudy2
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
