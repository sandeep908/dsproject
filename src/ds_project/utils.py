import os
import sys
from src.ds_project.exception import CustomException
from src.ds_project.loggers import logging
import pandas as pd
import pymysql

from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

def read_sql_data():
    logging.info("Reading start from database")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connnection established",mydb)
        df = pd.read_sql_query("select * from students" , mydb)
        print(df.head())
        
        return df
        
    except Exception as e:
        raise CustomException(e)