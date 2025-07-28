#!/usr/bin/env python3
"""
Cab Cancellation Prediction Flask App Runner
"""

import os
import sys
import subprocess

def install_requirements():
    """Install required packages"""
    print("Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        return False
    return True

def train_model():
    """Train the model if it doesn't exist"""
    print("Training model...")
    try:
        from src.pipeline.train_pipeline import TrainPipeline
        train_pipeline = TrainPipeline()
        accuracy = train_pipeline.initiate_train_pipeline()
        print(f"Model trained successfully with accuracy: {accuracy:.2%}")
        return True
    except Exception as e:
        print(f"Error training model: {e}")
        return False

def run_app():
    """Run the Flask application"""
    print("Starting Flask application...")
    try:
        from app import app
        app.run(debug=True, host='0.0.0.0', port=5000)
    except OSError as e:
        if "Address already in use" in str(e):
            print("Port 5000 is busy, trying port 5001...")
            app.run(debug=True, host='0.0.0.0', port=5001)
        else:
            print(f"Error starting app: {e}")
    except Exception as e:
        print(f"Error starting app: {e}")

if __name__ == "__main__":
    print("🚕 Cab Cancellation Prediction App")
    print("=" * 40)
    
    # Install requirements
    if not install_requirements():
        print("Failed to install requirements. Exiting.")
        sys.exit(1)
    
    # Train model if needed
    if not os.path.exists('artifacts/model.pkl'):
        print("Model not found. Training new model...")
        if not train_model():
            print("Failed to train model. Exiting.")
            sys.exit(1)
    else:
        print("Model found. Skipping training.")
    
    # Run the app
    run_app() 