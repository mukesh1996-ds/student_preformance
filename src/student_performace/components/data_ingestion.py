## Reading the data from mysql database 
import os 
import sys
from src.student_performace.exception import CustomeException
from src.student_performace.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.student_performace.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        ## Reading from the mqsql database 
        try:
            ## Reading code
            #df = read_sql_data()
            df=pd.read_csv(os.path.join('notebook/data','raw.csv')) ## Remove at the end

            logging.info("Reading from MySql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) ## Making the aritfacts folder
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Data Ingestion is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomeException(e,sys)

