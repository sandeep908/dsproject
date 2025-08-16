from src.ds_project.loggers import logging
from src.ds_project.exception import CustomException
import sys
from src.ds_project.components.data_ingestion import Dataingestion
from src.ds_project.components.data_ingestion import DataIngestionConfig

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = Dataingestion()
        data_ingestion.initate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e , sys)

