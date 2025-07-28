// Cab Cancellation Prediction App JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Form submission handler
    document.getElementById('predictionForm').addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const data = Object.fromEntries(formData);
        
        // Convert string values to numbers
        for (let key in data) {
            data[key] = parseFloat(data[key]);
        }
        
        document.getElementById('result').innerHTML = '<div class="loading">Making prediction...</div>';
        
        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            const result = await response.json();
            
            if (result.success) {
                const resultDiv = document.getElementById('result');
                const className = result.prediction === 1 ? 'cancelled' : 'not-cancelled';
                const text = result.prediction === 1 ? '🚫 Likely to be CANCELLED' : '✅ Likely to be CONFIRMED';
                
                resultDiv.innerHTML = `
                    <div class="result ${className}">
                        <div>${text}</div>
                        <div class="probability">Confidence: ${(result.probability * 100).toFixed(1)}%</div>
                    </div>
                `;
            } else {
                document.getElementById('result').innerHTML = `
                    <div class="result error">Error: ${result.error}</div>
                `;
            }
        } catch (error) {
            document.getElementById('result').innerHTML = `
                <div class="result error">Error: ${error.message}</div>
            `;
        }
    });
});

// Train model function
async function trainModel() {
    document.getElementById('trainResult').innerHTML = '<div class="loading">Training model...</div>';
    
    try {
        const response = await fetch('/train', {
            method: 'POST'
        });
        
        const result = await response.json();
        
        if (result.success) {
            document.getElementById('trainResult').innerHTML = `
                <div class="result not-cancelled">
                    Training completed! Accuracy: ${(result.accuracy * 100).toFixed(2)}%
                </div>
            `;
        } else {
            document.getElementById('trainResult').innerHTML = `
                <div class="result error">Error: ${result.error}</div>
            `;
        }
    } catch (error) {
        document.getElementById('trainResult').innerHTML = `
            <div class="result error">Error: ${error.message}</div>
        `;
    }
}

// Utility functions
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Form validation
function validateForm() {
    const requiredFields = [
        'user_id', 'vehicle_model_id', 'travel_type_id', 'package_id',
        'from_area_id', 'to_area_id', 'from_city_id', 'to_city_id',
        'online_booking', 'mobile_site_booking',
        'from_lat', 'from_long', 'to_lat', 'to_long'
    ];
    
    for (let field of requiredFields) {
        const input = document.getElementById(field);
        if (!input.value) {
            showNotification(`Please fill in ${field.replace('_', ' ')}`, 'error');
            return false;
        }
    }
    
    return true;
}

// Add form validation to submit button
document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.querySelector('button[type="submit"]');
    if (submitButton) {
        submitButton.addEventListener('click', function(e) {
            if (!validateForm()) {
                e.preventDefault();
            }
        });
    }
}); 