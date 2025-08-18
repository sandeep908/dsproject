from src.ds_project.loggers import logging
from src.ds_project.exception import CustomException
import sys
from src.ds_project.components.data_ingestion import Dataingestion
from src.ds_project.components.data_ingestion import DataIngestionConfig
from src.ds_project.components.data_transformation import DataTransformation, DataTransformtionConfig

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = Dataingestion()
        train_data_path , test_data_path =data_ingestion.initate_data_ingestion()
        
        data_transformation_config = DataTransformtionConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path , test_data_path)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e , sys)

