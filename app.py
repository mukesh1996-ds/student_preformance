from src.student_performace.logger import logging
from src.student_performace.exception import CustomeException
from src.student_performace.components.data_ingestion import DataIngestion
import sys 

if __name__=="__main__":
    logging.info("The execution is started")
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)
    