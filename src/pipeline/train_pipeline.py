import os
import sys
# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        pass

    def initiate_train_pipeline(self):
        try:
            logging.info("Starting training pipeline")
            
            # Data Ingestion
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info("Data ingestion completed")

            # Data Transformation
            logging.info("Starting data transformation")
            data_transformation = DataTransformation()
            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            logging.info("Data transformation completed")

            # Model Training
            logging.info("Starting model training")
            model_trainer = ModelTrainer()
            accuracy = model_trainer.initiate_model_trainer(train_arr, test_arr)
            logging.info(f"Model training completed with accuracy: {accuracy}")

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    train_pipeline = TrainPipeline()
    accuracy = train_pipeline.initiate_train_pipeline()
    print(f"Training completed with accuracy: {accuracy}")
