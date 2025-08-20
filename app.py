from src.ds_project.loggers import logging
from src.ds_project.exception import CustomException
import sys
from src.ds_project.components.data_ingestion import Dataingestion
from src.ds_project.components.data_ingestion import DataIngestionConfig
from src.ds_project.components.data_transformation import DataTransformation, DataTransformtionConfig

from src.ds_project.components.model_trainer import ModelTrainerConfig, ModelTrainer

if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = Dataingestion()
        train_data_path , test_data_path =data_ingestion.initate_data_ingestion()
        
        data_transformation_config = DataTransformtionConfig()
        data_transformation = DataTransformation()
        train_arr, test_arr , _ = data_transformation.initiate_data_transformation(train_data_path , test_data_path)
        
        # Model training code
        model_trainer = ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr , test_arr))
        
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e , sys)

