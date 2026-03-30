from flask import Flask, request, jsonify, render_template_string
import pickle
import pandas as pd
import os

app = Flask(__name__)

# Load trained models
try:
    with open('models.pkl', 'rb') as f:
        models = pickle.load(f)

    lr = models['lr']
    dt = models['dt']
    knn = models['knn']
    scaler = models['scaler']
    encoders = models['encoders']
    feature_names = models['feature_names']
    print("✅ Models loaded successfully")
except FileNotFoundError:
    print("❌ Error: models.pkl not found. Please run model.py first to train models.")
    lr = dt = knn = scaler = encoders = feature_names = None
except Exception as e:
    print(f"❌ Error loading models: {e}")
    lr = dt = knn = scaler = encoders = feature_names = None
feature_names = models['feature_names']

# Read the HTML content
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

@app.route('/')
def home():
    return render_template_string(html_content)

@app.route('/predict', methods=['POST'])
def predict():
    if lr is None or scaler is None or encoders is None:
        return jsonify({'error': 'Models not loaded. Please ensure models.pkl exists.'}), 500

    try:
        data = request.get_json()

        # Create DataFrame from input
        input_df = pd.DataFrame([data])

        # Ensure all expected features are present
        for feature in feature_names:
            if feature not in input_df.columns:
                input_df[feature] = 0  # Default value

        # Keep only the features used in training
        input_df = input_df[feature_names]

        # Encode categorical features
        for col, encoder in encoders.items():
            if col in input_df.columns:
                try:
                    input_df[col] = encoder.transform(input_df[col].astype(str))
                except ValueError:
                    # Handle unknown categories by using the first class
                    input_df[col] = encoder.transform([encoder.classes_[0]])[0]

        # Scale the features
        input_scaled = scaler.transform(input_df)

        # Make predictions
        lr_pred = lr.predict_proba(input_scaled)[0][1]
        dt_pred = dt.predict_proba(input_scaled)[0][1]
        knn_pred = knn.predict_proba(input_scaled)[0][1]

        # Use logistic regression as the best model for final prediction
        final_pred = lr_pred >= 0.5

        return jsonify({
            'lr_prob': float(lr_pred),
            'dt_prob': float(dt_pred),
            'knn_prob': float(knn_pred),
            'final_prediction': bool(final_pred),
            'confidence': float(lr_pred)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)