import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (semicolon separated!)
df = pd.read_csv("student-mat.csv", sep=";")

# Quick overview
print("Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nData types:")
print(df.info())
print("\nStatistics:")
print(df.describe())

# Create Pass/Fail target column
df["result"] = (df["G3"] >= 10).astype(int)

print("\nPass/Fail distribution:")
print(df["result"].value_counts())

from sklearn.preprocessing import LabelEncoder, StandardScaler

# Separate features and target
X = df.drop(columns=["G1", "G2", "G3", "result"])  # remove grades and target
y = df["result"]

# Encode categorical (text) columns
le = LabelEncoder()
for col in X.select_dtypes(include="object").columns:
    X[col] = le.fit_transform(X[col])

# Normalize numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset: 70% train, 30% test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.30, random_state=42
)

print("Training samples:", X_train.shape[0])
print("Testing samples:", X_test.shape[0])
print("Preprocessing complete!")

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Fix the pandas warning
for col in X.select_dtypes(include="str").columns:
    X[col] = le.fit_transform(X[col])

# --- Model 1: Logistic Regression ---
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# --- Model 2: Decision Tree ---
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

# --- Model 3: k-Nearest Neighbors ---
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

# --- Print Results ---
models = {
    "Logistic Regression": lr_pred,
    "Decision Tree": dt_pred,
    "k-NN": knn_pred
}

for name, pred in models.items():
    print(f"\n========== {name} ==========")
    print(f"Accuracy: {accuracy_score(y_test, pred) * 100:.2f}%")
    print(classification_report(y_test, pred))

    import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

# --- Accuracy Comparison Bar Chart ---
model_names = ["Logistic Regression", "Decision Tree", "k-NN"]
accuracies = [
    accuracy_score(y_test, lr_pred),
    accuracy_score(y_test, dt_pred),
    accuracy_score(y_test, knn_pred)
]

plt.figure(figsize=(8, 5))
bars = plt.bar(model_names, [a * 100 for a in accuracies], color=["#4CAF50", "#2196F3", "#FF9800"])
plt.ylabel("Accuracy (%)")
plt.title("Model Accuracy Comparison")
plt.ylim(0, 100)
for bar, acc in zip(bars, accuracies):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f"{acc*100:.2f}%", ha="center", fontweight="bold")
plt.tight_layout()
plt.savefig("accuracy_comparison.png")
plt.show()

# --- Confusion Matrices ---
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for ax, (name, pred) in zip(axes, models.items()):
    ConfusionMatrixDisplay.from_predictions(y_test, pred, ax=ax, colorbar=False)
    ax.set_title(name)
plt.tight_layout()
plt.savefig("confusion_matrices.png")
plt.show()

print("Charts saved!")