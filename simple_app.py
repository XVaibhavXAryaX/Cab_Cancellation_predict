from flask import Flask, request, jsonify, render_template
import os
import sys

# Add the project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)

# Initialize prediction pipeline as None
predict_pipeline = None

def load_model():
    """Load the prediction pipeline when needed"""
    global predict_pipeline
    if predict_pipeline is None:
        try:
            print("Loading prediction pipeline...")
            from src.pipeline.predict_pipeline import PredictPipeline
            predict_pipeline = PredictPipeline()
            print("Model loaded successfully!")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False
    return True

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Load model if not already loaded
        if not load_model():
            return jsonify({'success': False, 'error': 'Model could not be loaded'})
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = [
            'user_id', 'vehicle_model_id', 'travel_type_id', 'package_id',
            'from_area_id', 'to_area_id', 'from_city_id', 'to_city_id',
            'online_booking', 'mobile_site_booking',
            'from_lat', 'from_long', 'to_lat', 'to_long'
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({'success': False, 'error': f'Missing required field: {field}'})
        
        # Add an ID field if not present
        if 'id' not in data:
            data['id'] = 1
        
        result = predict_pipeline.predict(data)
        
        return jsonify({
            'success': True,
            'prediction': result['prediction'],
            'probability': result['probability'],
            'prediction_text': result['prediction_text']
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/train', methods=['POST'])
def train():
    try:
        from src.pipeline.train_pipeline import TrainPipeline
        train_pipeline = TrainPipeline()
        accuracy = train_pipeline.initiate_train_pipeline()
        
        # Reload the prediction pipeline with the new model
        global predict_pipeline
        predict_pipeline = None
        load_model()
        
        return jsonify({
            'success': True,
            'accuracy': accuracy
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'model_loaded': predict_pipeline is not None
    })

if __name__ == '__main__':
    print("🚕 Cab Cancellation Prediction Flask App")
    print("=" * 40)
    print("Starting Flask application...")
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except OSError as e:
        if "Address already in use" in str(e):
            print("Port 5000 is busy, trying port 5001...")
            app.run(debug=True, host='0.0.0.0', port=5001)
        else:
            print(f"Error starting Flask app: {e}") 