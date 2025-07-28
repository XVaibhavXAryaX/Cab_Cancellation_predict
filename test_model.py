#!/usr/bin/env python3
"""
Test script to check if the model loading works
"""

import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_model_loading():
    """Test if the model can be loaded successfully"""
    try:
        print("Testing model loading...")
        from src.pipeline.predict_pipeline import PredictPipeline
        print("Import successful!")
        
        predict_pipeline = PredictPipeline()
        print("Model loaded successfully!")
        
        # Test prediction
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
            'online_booking': 1,
            'mobile_site_booking': 0,
            'from_lat': 12.9716,
            'from_long': 77.5946,
            'to_lat': 12.9716,
            'to_long': 77.5946
        }
        
        result = predict_pipeline.predict(sample_data)
        print(f"Prediction test successful: {result}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚕 Testing Cab Cancellation Model")
    print("=" * 40)
    
    success = test_model_loading()
    
    if success:
        print("✅ Model test successful!")
    else:
        print("❌ Model test failed!") 