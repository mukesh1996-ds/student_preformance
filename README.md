# 🎓 Student Performance Indicator

A machine learning project that predicts student performance based on various attributes. This project follows a modular ML pipeline—from data ingestion to deployment—ensuring maintainability, reproducibility, and scalability.

---

## 🚀 Project Stages

### 1. 📦 Requirements

All dependencies for the project are listed in [`requirements.txt`](./requirements.txt). Install them using:

```bash
pip install -r requirements.txt
```

---

### 2. 🏗️ Project Structure

The entire project structure is auto-generated using a custom `template.py` script to scaffold folders and files needed for a clean ML pipeline.

```
├── artifacts/
├── config/
├── data/
├── logs/
├── notebooks/
├── src/
│   ├── components/
│   ├── pipelines/
│   ├── utils/
│   └── ...
├── templates/
├── app.py
├── requirements.txt
└── README.md
```

---

### 3. 🔁 Training Pipeline

#### 📂 Data Source
Raw student performance data is collected from academic datasets (e.g., Kaggle or institutional sources).

#### 🛠️ Data Ingestion
Splits the data into **training** and **testing** sets using stratified sampling to preserve distribution.

#### 📊 Data Transformation
- Exploratory Data Analysis (EDA)
- Missing value treatment
- Feature engineering & scaling
- Outlier detection

#### 🤖 Model Training
Trains multiple models (e.g., Random Forest, XGBoost, Logistic Regression) and evaluates them using:
- Accuracy
- F1 Score
- ROC-AUC

#### 📈 Model Monitoring (CI/CD)
Implements **Evidently AI** for continuous monitoring of:
- Data Drift
- Model Performance Drift

Integrated into a **CI/CD pipeline** via GitHub Actions for automated testing, training, and deployment.

#### 🚀 Model Deployment
The best model is serialized and deployed using **Flask/Streamlit**, making it accessible via a simple web UI.

---

### 4. 🔍 Prediction Pipeline

Once deployed, the model can be used to make predictions via a REST API or Web UI. It includes:
- Input data validation
- Preprocessing steps (replicating training logic)
- Final prediction output with probability scores

---

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **ML Libraries**: Scikit-learn, XGBoost, Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Monitoring**: Evidently AI
- **Deployment**: Flask / Streamlit
- **Automation**: GitHub Actions (CI/CD)
- **Version Control**: Git

---

