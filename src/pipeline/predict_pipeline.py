import os
import sys
# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np
import pickle

class PredictPipeline:
    def __init__(self):
        self.model_path = os.path.join('artifacts', 'model.pkl')
        self.preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
        self.model = None
        self.preprocessor = None
        self.load_model()

    def load_model(self):
        try:
            logging.info("Loading trained model and preprocessor")
            
            # Check if model files exist
            if not os.path.exists(self.model_path):
                raise FileNotFoundError(f"Model file not found: {self.model_path}")
            if not os.path.exists(self.preprocessor_path):
                raise FileNotFoundError(f"Preprocessor file not found: {self.preprocessor_path}")
            
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            
            with open(self.preprocessor_path, 'rb') as f:
                self.preprocessor = pickle.load(f)
            
            logging.info("Model and preprocessor loaded successfully")
        except Exception as e:
            raise CustomException(f"Error loading model: {e}", sys)

    def predict(self, data):
        try:
            logging.info("Making prediction")
            
            # Ensure data is in the correct format
            if isinstance(data, dict):
                df = pd.DataFrame([data])
            elif isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                df = data

            # Get the expected feature names from training
            expected_features = self.get_feature_names()
            
            # Add missing features with default values
            for feature in expected_features:
                if feature not in df.columns:
                    if feature in ['online_booking', 'mobile_site_booking']:
                        df[feature] = 0  # Default to 0 for booking type
                    else:
                        df[feature] = 0  # Default to 0 for other missing features
            
            # Select only the expected features in the correct order
            features = df[expected_features]
            
            # Transform features using the preprocessor
            features_scaled = self.preprocessor.transform(features)
            
            # Make prediction
            prediction = self.model.predict(features_scaled)
            prediction_proba = self.model.predict_proba(features_scaled)
            
            logging.info("Prediction completed successfully")
            
            return {
                'prediction': int(prediction[0]),
                'probability': float(prediction_proba[0][1]),  # Probability of cancellation
                'prediction_text': 'Cancelled' if prediction[0] == 1 else 'Not Cancelled'
            }
            
        except Exception as e:
            raise CustomException(f"Error making prediction: {e}", sys)

    def get_feature_names(self):
        """Get the feature names used by the model"""
        try:
            # This should match the features used during training
            sample_data = pd.read_csv('notebook/YourCabs.csv')
            numerical_columns = sample_data.select_dtypes(include=[np.number]).columns.tolist()
            if 'Car_Cancellation' in numerical_columns:
                numerical_columns.remove('Car_Cancellation')
            return numerical_columns
        except Exception as e:
            logging.warning(f"Could not get feature names: {e}")
            return []

if __name__ == "__main__":
    # Test the prediction pipeline
    predict_pipeline = PredictPipeline()
    
    # Sample data for testing
    sample_data = {
        'id': 1,
        'user_id': 1001,
        'vehicle_model_id': 1,
        'travel_type_id': 1,
        'package_id': 1,
        'from_area_id': 1,
        'to_area_id': 2,
        'from_city_id': 1,
        'to_city_id': 1,
        'from_lat': 12.9716,
        'from_long': 77.5946,
        'to_lat': 12.9716,
        'to_long': 77.5946
    }
    
    result = predict_pipeline.predict(sample_data)
    print(f"Prediction: {result}")
