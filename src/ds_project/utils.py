import os
import sys
from src.ds_project.exception import CustomException
from src.ds_project.loggers import logging
import pandas as pd
import pymysql

import pickle
import numpy as np

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
    
    
def save_object(file_path , obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path , exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj , file_obj)
    
    except Exception as e:
        raise CustomException(e , sys)