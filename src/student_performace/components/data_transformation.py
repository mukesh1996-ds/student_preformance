import sys 
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from src.student_performace.exception import CustomeException
from src.student_performace.logger import logging
from src.student_performace.utils import save_object
import os 
import pickle

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file=os.path.join('artifacts','preprocessor.pkl') ## Path to save the file

class DataTransformation:
    def __init__(self):
        self.data_transfromation_config=DataTransformationConfig()

    def get_data_transformer_obj(self):
        """
        This function will be responsible for data transformation
        """
        try:
            ## I have hard coded the column as i have very few of them
            numerical_feature = [
                "writing_score","reading_score"
            ]
            categorical_feature = [
                "gender","race_ethnicity","parental_level_of_education","lunch",
                "test_preparation_course"
            ]
            num_pipeline = Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scalar',StandardScaler())
            ])
            cat_pipeline = Pipeline(steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ("one_hot_encoder",OneHotEncoder()),
                ("scalar",StandardScaler(with_mean=False))
            ])
            logging.info(f"Categorical Columns:- {categorical_feature}")
            logging.info(f"Numerical Columns:- {numerical_feature}")

            ## Combining the Pipeline 
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_feature),
                    ("cat_pipeline",cat_pipeline,categorical_feature)
                ]
            )
            return preprocessor   
        except Exception as e:
            raise CustomeException(e, sys)
    
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Reading the train and test path")
            preprocessing_obj= self.get_data_transformer_obj()
            target_column = "math_score"
            numerical_feature = [
                "writing_score","reading_score"
            ]
            ## Training data preparation
            input_features_train_df = train_df.drop(columns=[target_column],axis=1)
            target_features_train_df= train_df[target_column]
            ## Test data preparation
            input_features_test_df = test_df.drop(columns=[target_column],axis=1)
            target_features_test_df= test_df[target_column]

            logging.info("Applying preprocessing on Train and test data")
            
            input_feature_training_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_testing_arr=preprocessing_obj.transform(input_features_test_df)

            ## Combining all my data 
            train_arr = np.c_[
                input_feature_training_arr,np.array(target_features_train_df)
            ]
            test_arr = np.c_[
                input_feature_testing_arr,np.array(target_features_test_df)
            ]
            logging.info(f"Save Preprocessing Object")
            save_object(
                file_path=self.data_transfromation_config.preprocessor_obj_file,
                obj=preprocessing_obj
            )
            return (
                train_arr,test_arr,self.data_transfromation_config.preprocessor_obj_file
            )




        except Exception as e:
            raise CustomeException(e, sys)
        

