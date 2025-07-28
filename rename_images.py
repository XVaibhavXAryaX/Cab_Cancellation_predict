#!/usr/bin/env python3
"""
Script to rename extracted images with meaningful names for README
"""

import os
import shutil

def rename_images():
    """Rename extracted images with meaningful names"""
    
    # Mapping of cell outputs to meaningful names
    # Based on typical EDA patterns and the order they appear
    image_mapping = {
        # Cell 44 outputs (likely early EDA visualizations)
        'cell_44_output_0.png': 'target_distribution.png',
        'cell_44_output_1.png': 'correlation_matrix.png',
        'cell_44_output_2.png': 'missing_values.png',
        'cell_44_output_3.png': 'feature_distribution.png',
        'cell_44_output_4.png': 'booking_types.png',
        'cell_44_output_5.png': 'travel_types.png',
        'cell_44_output_6.png': 'vehicle_models.png',
        'cell_44_output_7.png': 'geographic_distribution.png',
        'cell_44_output_8.png': 'time_patterns.png',
        
        # Cell 48 outputs (likely model performance)
        'cell_48_output_0.png': 'confusion_matrix.png',
        'cell_48_output_1.png': 'roc_curve.png',
        'cell_48_output_2.png': 'precision_recall.png',
        'cell_48_output_3.png': 'feature_importance.png',
        'cell_48_output_4.png': 'model_comparison.png',
        'cell_48_output_5.png': 'prediction_distribution.png',
        'cell_48_output_6.png': 'accuracy_metrics.png',
        'cell_48_output_7.png': 'classification_report.png',
        'cell_48_output_8.png': 'model_performance.png',
        
        # Cell 69 and 72 outputs (likely additional analysis)
        'cell_69_output_1.png': 'area_analysis.png',
        'cell_72_output_1.png': 'distance_analysis.png',
        'cell_77_output_1.png': 'final_model_results.png'
    }
    
    images_dir = 'images'
    
    print("🖼️ Renaming extracted images...")
    print("=" * 50)
    
    # Check if images directory exists
    if not os.path.exists(images_dir):
        print(f"❌ Images directory '{images_dir}' not found!")
        return
    
    # Get list of files in images directory
    files = os.listdir(images_dir)
    
    # Rename files
    renamed_count = 0
    for old_name, new_name in image_mapping.items():
        old_path = os.path.join(images_dir, old_name)
        new_path = os.path.join(images_dir, new_name)
        
        if os.path.exists(old_path):
            try:
                shutil.move(old_path, new_path)
                print(f"✅ {old_name} → {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"❌ Error renaming {old_name}: {e}")
        else:
            print(f"⚠️  File not found: {old_name}")
    
    print(f"\n🎉 Successfully renamed {renamed_count} images!")
    
    # List remaining files
    remaining_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]
    if remaining_files:
        print(f"\n📁 Remaining files in {images_dir}/:")
        for file in remaining_files:
            print(f"   - {file}")
    
    print("\n📝 Next steps:")
    print("1. Review the renamed images")
    print("2. Update README.md with correct image paths")
    print("3. Take a screenshot of your Flask app for 'web_interface.png'")

if __name__ == "__main__":
    rename_images() 