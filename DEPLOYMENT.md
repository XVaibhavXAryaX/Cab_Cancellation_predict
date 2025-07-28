# 🚕 Cab Cancellation Prediction - Flask Deployment Guide

## Overview
This guide will help you deploy the Cab Cancellation Prediction model using Flask.

## 🚀 Quick Start

### Option 1: Using the Runner Script (Recommended)
```bash
python run_app.py
```

### Option 2: Manual Setup
```bash
# 1. Install requirements
pip install -r requirements.txt

# 2. Train the model (if not already trained)
python src/pipeline/train_pipeline.py

# 3. Run the Flask app
python app.py
```

## 📋 Prerequisites
- Python 3.7+
- pip
- YourCabs.csv dataset in the `notebook/` folder

## 🏗️ Project Structure
```
Cab_Cancellation_predict/
├── app.py                 # Flask application
├── run_app.py            # Deployment runner script
├── requirements.txt      # Python dependencies
├── src/
│   ├── components/       # ML components
│   ├── pipeline/         # Training & prediction pipelines
│   └── utils/           # Utility functions
├── artifacts/           # Saved models and data
└── notebook/           # Dataset and notebooks
```

## 🌐 API Endpoints

### 1. Web Interface
- **URL**: `http://localhost:5000`
- **Method**: GET
- **Description**: Beautiful web interface for making predictions

### 2. Prediction API
- **URL**: `http://localhost:5000/predict`
- **Method**: POST
- **Content-Type**: application/json

**Request Body:**
```json
{
    "user_id": 1001,
    "vehicle_model_id": 1,
    "travel_type_id": 1,
    "package_id": 1,
    "from_area_id": 1,
    "to_area_id": 2,
    "from_city_id": 1,
    "to_city_id": 1,
    "from_lat": 12.9716,
    "from_long": 77.5946,
    "to_lat": 12.9716,
    "to_long": 77.5946
}
```

**Response:**
```json
{
    "success": true,
    "prediction": 0,
    "probability": 0.15,
    "prediction_text": "Not Cancelled"
}
```

### 3. Training API
- **URL**: `http://localhost:5000/train`
- **Method**: POST
- **Description**: Retrain the model with current data

**Response:**
```json
{
    "success": true,
    "accuracy": 0.934
}
```

### 4. Health Check
- **URL**: `http://localhost:5000/health`
- **Method**: GET
- **Description**: Check if the model is loaded

**Response:**
```json
{
    "status": "healthy",
    "model_loaded": true
}
```

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to `production` for production deployment
- `PORT`: Custom port (default: 5000)
- `HOST`: Custom host (default: 0.0.0.0)

### Production Deployment
```bash
# Set environment variables
export FLASK_ENV=production
export PORT=8080

# Run with production server
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

## 📊 Model Performance
- **Accuracy**: ~93.44%
- **Model Type**: Random Forest Classifier
- **Features**: 12 numerical features
- **Target**: Car_Cancellation (0/1)

## 🐛 Troubleshooting

### Common Issues

1. **Module not found errors**
   ```bash
   pip install -e .
   ```

2. **Model not found**
   ```bash
   python src/pipeline/train_pipeline.py
   ```

3. **Port already in use**
   ```bash
   # Change port in app.py or use different port
   python app.py --port 5001
   ```

4. **Dataset not found**
   - Ensure `YourCabs.csv` is in the `notebook/` folder

### Logs
- Check console output for detailed error messages
- Flask debug mode provides detailed error information

## 🔄 Updating the Model

### Retrain via Web Interface
1. Go to `http://localhost:5000`
2. Click "Train Model" button
3. Wait for training to complete

### Retrain via API
```bash
curl -X POST http://localhost:5000/train
```

### Retrain via Script
```bash
python src/pipeline/train_pipeline.py
```

## 📈 Monitoring

### Health Check
```bash
curl http://localhost:5000/health
```

### Model Performance
- Check accuracy in training logs
- Monitor prediction response times
- Track API usage

## 🔒 Security Considerations

### Production Checklist
- [ ] Set `FLASK_ENV=production`
- [ ] Use HTTPS
- [ ] Implement rate limiting
- [ ] Add authentication if needed
- [ ] Validate input data
- [ ] Use environment variables for secrets

### Input Validation
The API validates all required fields:
- user_id
- vehicle_model_id
- travel_type_id
- package_id
- from_area_id
- to_area_id
- from_city_id
- to_city_id
- from_lat
- from_long
- to_lat
- to_long

## 🚀 Deployment Options

### 1. Local Development
```bash
python run_app.py
```

### 2. Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

### 3. Cloud Deployment
- **Heroku**: Use Procfile with `web: gunicorn app:app`
- **AWS**: Use Elastic Beanstalk or ECS
- **Google Cloud**: Use App Engine or Cloud Run
- **Azure**: Use App Service

## 📞 Support
For issues or questions:
1. Check the troubleshooting section
2. Review console logs
3. Verify dataset and model files exist
4. Ensure all dependencies are installed

## 🎯 Next Steps
- Add more features to the model
- Implement model versioning
- Add data validation and cleaning
- Create automated retraining pipeline
- Add monitoring and alerting
- Implement A/B testing for model improvements 