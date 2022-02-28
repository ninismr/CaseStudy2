import mysql.connector as mysql
from mysql.connector import Error
import sqlalchemy
from urllib.parse import quote_plus as urlquote
import pandas as pd


class StudiKasus2:
    """
    This class is used to import data in the form of a .csv file into the database
    """
    def __init__(self, host, port, user, password):
        """
        This function is used to connect to the database

        :param host: this is the database host
        :param port: this is the database port
        :param user: this is the database user
        :param password: this is the database user password
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password

    def create_db(self, db_name):
        """
        This function is used to create a database

        :param db_name: this is the desired database name

        :return: a database according to the name entered in the parameter
        """
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
        # preparing a cursor object
        # creating database

    def create_table(self, db_name, table_name, df):
        """
        This function is used to create a table in a database that was previously
        created and load the data from the imported .csv file
        (that already become dataframe) into the database

        :param db_name: this is the desired database name
        :param table_name: this is the desired table name
        :param df: this is the dataframe from the imported .csv file

        :return: a table in the previously created database and table name
        according to the name entered in the parameter
        """
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

    def load_data(self, db_name, table_name):
        """
        This function is used to load existing data in a previously created database

        :param db_name: this is the name of the database whose data we want to load
        :param table_name: this is the name of the table in the database whose data we want to load

        :return: a data from the database/table whose data we want to load
        """
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

    def import_csv(self, path):
        """
        This function is used to import/read data in a .csv file and save it as a dataframe

        :param path: this is the path of the .csv file or if it is
        in the same folder we can just enter the .csv filename

        :return: a data from the .csv file in a dataframe format
        """
        return pd.read_csv(path, index_col=False, delimiter=',')
