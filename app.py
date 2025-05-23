from src.student_performace.logger import logging
from src.student_performace.exception import CustomeException
from src.student_performace.components.data_ingestion import DataIngestion
from src.student_performace.components.data_transformation import DataTransformation,DataTransformationConfig
from src.student_performace.components.model_trainer import ModelTrainer,ModelTrainerConfig

import sys 

if __name__=="__main__":
    logging.info("The execution is started")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformationConfig()
        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        ## model training 
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)
    