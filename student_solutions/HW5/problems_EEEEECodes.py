import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

# Ensure results directory exists relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(script_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Load data
data_path = os.path.join(script_dir, "..", "data", "fraud_transactions.csv")
df = pd.read_csv(data_path)

# ---------------------------------------------------------
# FRAUD DETECTION PIPELINE
# ---------------------------------------------------------

# START STUDENT IMPLEMENTATION HERE

# Step 1: Preprocessing
drop_cols = ["nameOrig", "nameDest", "isFlaggedFraud"]
for c in drop_cols:
    if c in df.columns:
        df = df.drop(columns=c)

# One-hot encode 'type'
if "type" in df.columns:
    df = pd.get_dummies(df, columns=["type"], drop_first=True)

# Separate features and labels
y = df["isFraud"]
X = df.drop(columns=["isFraud"])

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 3: Train models
models = {
    "ridge": RidgeClassifier(alpha=1.0, solver="auto"),
    "random_forest": RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42),
    "adaboost": AdaBoostClassifier(n_estimators=50, learning_rate=1.0, random_state=42),
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)

# Utility: compute metrics and save confusion matrices
from sklearn.metrics import confusion_matrix
from matplotlib.colors import LogNorm

def save_confusion_matrix(cm, labels, path, title=None):
    fig, ax = plt.subplots(figsize=(5, 4))
    # Add 1 to avoid log(0)
    im = ax.imshow(cm + 1, cmap="Blues", norm=LogNorm())
    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    if title:
        ax.set_title(title)
    # annotate with raw counts
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, f"{cm[i, j]}", ha="center", va="center", color="black")
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)

def evaluate(name, model, X_tr, y_tr, X_te, y_te):
    results = {}
    for split, X_, y_, tag in [(X_tr, y_tr, "train"), (X_te, y_te, "test")]:
        y_pred = model.predict(X_)
        tn, fp, fn, tp = confusion_matrix(y_, y_pred).ravel()
        total = tn + fp + fn + tp
        acc = (tp + tn) / total if total else 0.0
        tpr = tp / (tp + fn) if (tp + fn) else 0.0
        fnr = fn / (tp + fn) if (tp + fn) else 0.0
        fpr = fp / (fp + tn) if (fp + tn) else 0.0
        tnr = tn / (tn + fp) if (tn + fp) else 0.0
        results[tag] = dict(accuracy=acc, TPR=tpr, FNR=fnr, FPR=fpr, TNR=tnr)
        cm = np.array([[tn, fp], [fn, tp]])
        save_confusion_matrix(cm, labels=["0", "1"],
                              path=os.path.join(results_dir, f"{name}_{tag}_cm.png"),
                              title=f"{name} - {tag}")
    return results

all_results = {}
for name, model in models.items():
    all_results[name] = evaluate(name, model, X_train_scaled, y_train, X_test_scaled, y_test)

# Step 6: Creative Analysis - feature importances and baseline
# Class distribution
class_counts = y.value_counts().to_dict()

# Baseline (always predict 0) accuracy on test
baseline_acc_test = (y_test == 0).mean()

# Feature importance for Random Forest
if "random_forest" in models:
    rf = models["random_forest"]
    importances = rf.feature_importances_
    feature_names = X.columns.tolist()
    idx = np.argsort(importances)[::-1][:10]
    top_feats = [feature_names[i] for i in idx]
    top_vals = importances[idx]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(range(len(top_vals))[::-1], top_vals, align="center")
    ax.set_yticks(range(len(top_vals)))
    ax.set_yticklabels(top_feats[::-1])
    ax.set_xlabel("Importance")
    ax.set_title("Top 10 Random Forest Feature Importances")
    fig.tight_layout()
    fig.savefig(os.path.join(results_dir, "rf_feature_importances.png"), dpi=150)
    plt.close(fig)

# Minimal console output
print("class_counts:", class_counts)
print("baseline_test_accuracy:", float(baseline_acc_test))
for name, metrics in all_results.items():
    print(name, metrics)

# END STUDENT IMPLEMENTATION HERE
