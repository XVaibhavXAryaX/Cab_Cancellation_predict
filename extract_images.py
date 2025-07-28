#!/usr/bin/env python3
"""
Script to extract images from Jupyter notebook for README documentation
"""

import json
import base64
import os
from pathlib import Path

def extract_images_from_notebook(notebook_path, output_dir):
    """
    Extract images from Jupyter notebook and save them to output directory
    """
    print(f"Extracting images from {notebook_path}")
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    image_count = 0
    
    # Process each cell
    for cell_idx, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code':
            # Check outputs for images
            for output_idx, output in enumerate(cell.get('outputs', [])):
                if 'data' in output and 'image/png' in output['data']:
                    # Extract image data
                    image_data = output['data']['image/png']
                    
                    # Generate filename
                    filename = f"cell_{cell_idx}_output_{output_idx}.png"
                    
                    # Save image
                    image_path = os.path.join(output_dir, filename)
                    with open(image_path, 'wb') as img_file:
                        img_file.write(base64.b64decode(image_data))
                    
                    print(f"Saved: {image_path}")
                    image_count += 1
    
    print(f"\nExtracted {image_count} images to {output_dir}")
    return image_count

def create_image_mapping():
    """
    Create a mapping of suggested image names based on typical EDA patterns
    """
    mapping = {
        # Target variable analysis
        "target_distribution.png": "Distribution of cancellation vs confirmed bookings",
        "class_balance.png": "Class balance analysis",
        
        # Feature analysis
        "correlation_matrix.png": "Feature correlation matrix",
        "feature_importance.png": "Feature importance plot",
        "missing_values.png": "Missing values analysis",
        
        # Booking analysis
        "booking_types.png": "Online vs mobile booking distribution",
        "travel_types.png": "Travel type distribution and cancellation rates",
        "vehicle_models.png": "Vehicle model distribution",
        
        # Geographic analysis
        "geographic_distribution.png": "Pickup and drop location distribution",
        "area_analysis.png": "Cancellation rates by area",
        "distance_analysis.png": "Distance vs cancellation rate",
        
        # Time analysis
        "time_patterns.png": "Cancellation patterns over time",
        "hourly_patterns.png": "Hourly booking patterns",
        "daily_patterns.png": "Daily booking patterns",
        "monthly_patterns.png": "Monthly trends",
        
        # Model performance
        "confusion_matrix.png": "Model confusion matrix",
        "roc_curve.png": "ROC curve",
        "precision_recall.png": "Precision-Recall curve",
        
        # Web interface
        "web_interface.png": "Flask web application interface"
    }
    
    return mapping

def generate_image_instructions():
    """
    Generate instructions for organizing extracted images
    """
    mapping = create_image_mapping()
    
    print("\n" + "="*60)
    print("IMAGE ORGANIZATION INSTRUCTIONS")
    print("="*60)
    
    print("\n1. Extract images from your notebook:")
    print("   python extract_images.py")
    
    print("\n2. Rename extracted images according to this mapping:")
    for suggested_name, description in mapping.items():
        print(f"   {suggested_name}: {description}")
    
    print("\n3. Move renamed images to the 'images/' directory")
    
    print("\n4. Update the README.md file with the correct image paths")
    
    print("\n5. For the web interface screenshot:")
    print("   - Take a screenshot of your Flask app running at http://localhost:5000")
    print("   - Save it as 'images/web_interface.png'")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    notebook_path = "notebook/yourcab.ipynb"
    output_dir = "extracted_images"
    
    if os.path.exists(notebook_path):
        extract_images_from_notebook(notebook_path, output_dir)
        generate_image_instructions()
    else:
        print(f"Notebook not found at {notebook_path}")
        print("Please ensure the notebook exists and run this script again.") 