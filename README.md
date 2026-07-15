# 🌾 OptiCrop – Smart Agricultural Production Optimization Engine

---

## 📌 Project Description

**OptiCrop** is an AI-powered agricultural recommendation system that helps farmers identify the most suitable crops based on soil nutrients and environmental conditions. By leveraging Machine Learning algorithms, the platform provides accurate crop recommendations, enabling better resource utilization, improved productivity, and data-driven agricultural decisions.

This project demonstrates the integration of **Machine Learning, Flask, Python, and Web Technologies** to build an intelligent decision-support system for modern agriculture.

---

## 🚀 Features

### ✅ Implemented Features

* **AI-Powered Crop Recommendation** – Predicts the most suitable crop using Machine Learning
* **High Accuracy Model** – Random Forest model achieving **99.86% accuracy**
* **22 Supported Crops** – Recommendations across a wide range of crops
* **Real-Time Predictions** – Instant results based on user inputs
* **Confidence Scores** – Displays prediction confidence percentages
* **Top Crop Matches** – Shows alternative crop recommendations
* **AI Assistant** – Interactive chatbot for guidance and support
* **Responsive Interface** – User-friendly and accessible design

---

## 🛠 Tech Stack

### 🖥 Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Font Awesome 6

### ⚙️ Backend

* Python 3.11
* Flask 2.2.2
* Jinja2 Templates

### 🤖 Machine Learning

* Scikit-learn
* Random Forest Classifier
* Logistic Regression
* K-Nearest Neighbors (KNN)
* K-Means Clustering
* Pandas
* NumPy

### 🗄 Database Design

* MongoDB Schema Design
* SQL Schema Design

---

## 📊 Dataset Information

### Dataset Overview

| Metric           | Value    |
| ---------------- | -------- |
| Total Samples    | 2,200    |
| Total Crops      | 22       |
| Features         | 7        |
| Dataset Type     | Balanced |
| Samples per Crop | 100      |

### Input Features

| Feature         | Description              |
| --------------- | ------------------------ |
| Nitrogen (N)    | Soil Nitrogen Content    |
| Phosphorous (P) | Soil Phosphorous Content |
| Potassium (K)   | Soil Potassium Content   |
| Temperature     | Average Temperature (°C) |
| Humidity        | Relative Humidity (%)    |
| pH              | Soil pH Level            |
| Rainfall        | Annual Rainfall (mm)     |

### Supported Crops

Rice, Maize, Chickpea, Kidneybeans, Pigeonpeas, Mothbeans, Mungbean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, and Coffee.

---

## 📂 Project Structure

```bash
OptiCrop/
│
├── 1. Brainstorming & Ideation/
│   ├── Brainstorming & Idea Prioritization.pdf
│   ├── Define Problem Statements.pdf
│   ├── Empathy Map.pdf
│   └── Literature Survey.pdf
│
├── 2. Requirement Analysis/
│   ├── Customer Journey Map.pdf
│   ├── Data Flow Diagram.pdf
│   ├── Solution Requirements.pdf
│   └── Technology Stack.pdf
│
├── 3. Project Design Phase/
│   ├── Problem-Solution Fit.pdf
│   ├── Proposed Solution.pdf
│   └── Solution Architecture.pdf
│
├── 4. Project Planning Phase/
│   └── Project Planning.pdf
│
├── 5. Project Development Phase/
│   ├── Application/
│   │   ├── app.py
│   │   ├── app.ipynb
│   │   ├── model_training.ipynb
│   │   ├── requirements.txt
│   │   ├── templates/
│   │   │   ├── index.html
│   │   │   ├── features.html
│   │   │   ├── recommendation.html
│   │   │   ├── about.html
│   │   │   ├── contact.html
│   │   │   └── result.html
│   │   └── static/
│   │
│   ├── Model/
│   │   ├── evaluate.ipynb
│   │   ├── models/
│   │   │   ├── crop_model.pkl
│   │   │   └── scaler.pkl
│   │   └── results/
│   │       ├── accuracy.txt
│   │       ├── confusion_matrix.png
│   │       └── elbow_graph.png
│   │
│   ├── Preprocessing/
│   │   ├── preprocessing.ipynb
│   │   └── processed/
│   │
│   ├── Code-Layout, Readability and Reusability.pdf
│   ├── Coding & Solution.pdf
│   ├── No. of Functional Features Included in the Solution.pdf
│   └── run.py
│
├── 6. Project Testing/
│   ├── Performance Testing.pdf
│
│
├── 7. Project Documentation/
│   ├── Project Executable Files.pdf
│   ├── Sample Project Documentation.pdf
│ 
│
├── 8. Project Demonstration/
│   ├── Communication.pdf
│   ├── Demonstration of Proposed Features.pdf
│   ├── Project Demo Planning.pdf
│   ├── Scalability & Future Plan.pdf
│   └── Team Involvement in Demonstration.pdf
│
├── Dataset/
│   └── Crop_recommendation.csv
│
├── Procfile
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

### Home Page
![Home Page](8.%20Project%20Demonstration/screenshots/Home.png)

### Features Section
![Features](8.%20Project%20Demonstration/screenshots/Features.png)

### Crop Recommendation Page
![Crop Recommendation](8.%20Project%20Demonstration/screenshots/recommendation.png)

### Soil Parameters Input
![Soil Parameters](8.%20Project%20Demonstration/screenshots/soilparameters.png)

### Prediction Results
![Results Page](8.%20Project%20Demonstration/screenshots/result.png)

### Recommendation Result
![Recommendation Result](8.%20Project%20Demonstration/screenshots/recommendedresult.png)

### About Page
![About Page](8.%20Project%20Demonstration/screenshots/about.png)

### AI Assistant
![AI Assistant](8.%20Project%20Demonstration/screenshots/contact.png)

### Contact Links
![Contact Links](8.%20Project%20Demonstration/screenshots/contactlink.png)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sasichintada/OptiCrop.git
cd OptiCrop
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application

```bash
python run.py
```

### 6️⃣ Open in Browser

```text
http://127.0.0.1:5000
```

---

## ▶️ Usage

1. Launch the application in your browser.
2. Navigate to the **Crop Recommendation** section.
3. Enter the required soil and environmental parameters:

   * Nitrogen (N)
   * Phosphorous (P)
   * Potassium (K)
   * Temperature
   * Humidity
   * pH Level
   * Rainfall
4. Click **Predict Best Crop**.
5. View recommended crops along with confidence scores.

---

## 📊 Model Performance

| Metric     | Score         |
| ---------- | ------------- |
| Best Model | Random Forest |
| Accuracy   | 99.86%        |
| Precision  | 99.85%        |
| Recall     | 99.85%        |
| F1 Score   | 99.85%        |

### Algorithms Evaluated

| Algorithm           | Accuracy |
| ------------------- | -------- |
| Random Forest       | 99.86%  |
| Logistic Regression | 96.36%   |
| KNN                 | 95.68%   |

---

## 🤖 AI Assistant

The built-in AI Assistant can answer questions related to:

* Crop recommendations
* Supported crops
* Model accuracy
* Dataset information
* Application features
* Technical architecture
* Support and guidance
* Future enhancements

---

## 🔮 Future Improvements

* Mobile Application Support
* Fertilizer Recommendation System
* Yield Prediction Module
* Weather Forecast Integration
* IoT Sensor Integration
* Multi-Language Support
* Irrigation Planning System
* Regional Crop Optimization

---

## 👩‍💻 Team

### Team OptiCrop

**Team Lead**

- Mohammad Firdose

**Members**

- Yuvateja Lanke
- Irshad Hussain

---

## 📄 License

This project is developed for educational and research purposes.

---

### 🌾 OptiCrop – Empowering Agriculture with Artificial Intelligence

Built with ❤️ by Team OptiCrop
