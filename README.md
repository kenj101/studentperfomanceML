# Student Performance ML Prediction System

A machine learning system that predicts whether a student is likely to pass or fail based on various academic and personal factors.

## Features

- **Three ML Models**: Logistic Regression, Decision Tree, and k-Nearest Neighbors
- **Web Interface**: Beautiful, responsive web app built with HTML/CSS/JavaScript
- **Flask Backend**: RESTful API for real-time predictions
- **Production Ready**: Deployed with Waitress WSGI server

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train Models

```bash
python model.py
```

This will:
- Load and preprocess the student-mat.csv dataset
- Train three ML models
- Save models to `models.pkl` for production use
- Generate accuracy comparison charts

### 3. Run Development Server

```bash
python app.py
```

Access at: http://127.0.0.1:5000

### 4. Production Deployment

#### Windows (Recommended)
```powershell
# Using PowerShell script
.\deploy.ps1

# Or manually
python -m waitress --host 0.0.0.0 --port 8000 --threads 4 app:app
```

## 🚀 Deploy to Cloud (Free & Live)

### Option 1: Render (Easiest)

1. **Sign up**: https://render.com (free tier available)
2. **Connect GitHub**: Dashboard → New → Web Service → Connect your repo
3. **Auto-configure**:
   - Runtime: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python run.py`
4. **Deploy**: Push to GitHub → Auto-deploy

### Option 2: Railway

1. **Sign up**: https://railway.app
2. **New Project**: Deploy from GitHub repo
3. **Auto-deploy**: Railway detects Python and deploys automatically

### Option 3: Fly.io

1. **Install CLI**: `curl -L https://fly.io/install.sh | sh`
2. **Deploy**: `fly launch` in your project directory
3. **Follow prompts**: Choose region, etc.

## 📋 Pre-Deployment Checklist

- ✅ Run `python model.py` locally to train models
- ✅ Commit `models.pkl` to Git (trained models)
- ✅ Ensure `requirements.txt` has all dependencies
- ✅ App respects `PORT` environment variable
- ✅ No hardcoded localhost URLs in frontend

#### Linux/Unix (Alternative)
```bash
# Install Gunicorn first
pip install gunicorn

# Run with Gunicorn
gunicorn --workers 4 --bind 0.0.0.0:8000 app:app
```

Access production app at: http://127.0.0.1:8000

## API Usage

### POST /predict

Send student data as JSON to get predictions:

```json
{
  "school": "GP",
  "sex": "F",
  "age": 16,
  "address": "U",
  "famsize": "GT3",
  "studytime": 2,
  "failures": 0,
  "absences": 4,
  "Medu": 3,
  "Fedu": 3,
  "traveltime": 1,
  "Walc": 1,
  "Dalc": 1,
  "higher": 1,
  "internet": 1,
  "famsup": 1,
  "schoolsup": 0,
  "romantic": 0,
  "freetime": 3,
  "G1": 11,
  "G2": 12
}
```

Response:
```json
{
  "lr_prob": 0.85,
  "dt_prob": 0.78,
  "knn_prob": 0.82,
  "final_prediction": true,
  "confidence": 0.85
}
```

## Model Performance

- **Logistic Regression**: 71.4% accuracy (best model)
- **Decision Tree**: 66.4% accuracy
- **k-Nearest Neighbors**: 64.7% accuracy

## Project Structure

```
student_performance/
├── app.py              # Flask web application
├── model.py            # ML model training and evaluation
├── index.html          # Web interface
├── models.pkl          # Trained models (generated)
├── requirements.txt    # Python dependencies
├── deploy.ps1          # Windows deployment script
├── run.py              # Alternative run script
├── student-mat.csv     # Math dataset
├── student-por.csv     # Portuguese dataset
└── README.md           # This file
```

## Technologies Used

- **Backend**: Flask, scikit-learn, pandas, numpy
- **Frontend**: HTML5, CSS3, JavaScript (Chart.js, PapaParse)
- **ML**: Logistic Regression, Decision Tree, k-NN
- **Deployment**: Waitress (Windows), Gunicorn (Linux/Unix)

## Dataset

The system uses the [Student Performance Dataset](https://archive.ics.uci.edu/dataset/320/student+performance) from UCI Machine Learning Repository, containing data from two Portuguese schools with information about students' academic performance.
