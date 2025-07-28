import os
import sys
# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join('artifacts', "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        try:
            preprocessor = StandardScaler()
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Reading train and test data")
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Obtaining preprocessing object")
            preprocessing_obj = self.get_data_transformer_object()

            target_column_name = "Car_Cancellation"  # Target column from the dataset
            
            # Get only numerical columns for preprocessing
            numerical_columns = train_df.select_dtypes(include=[np.number]).columns.tolist()
            if target_column_name in numerical_columns:
                numerical_columns.remove(target_column_name)
            
            # Drop non-numerical columns and target column
            input_feature_train_df = train_df[numerical_columns]
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df[numerical_columns]
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training dataframe and testing dataframe")
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Saved preprocessing object")
            # Save the preprocessor
            import pickle
            with open(self.transformation_config.preprocessor_obj_file_path, 'wb') as f:
                pickle.dump(preprocessing_obj, f)

            return train_arr, test_arr, self.transformation_config.preprocessor_obj_file_path

        except Exception as e:
            raise CustomException(e, sys)
