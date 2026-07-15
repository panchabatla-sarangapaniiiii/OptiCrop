# 📊 OptiCrop – Data Analysis

This folder contains the Exploratory Data Analysis (EDA) performed on the Crop Recommendation dataset used in the OptiCrop project. The objective of this analysis is to understand feature distributions, identify relationships between variables, detect patterns, and derive insights that support machine learning model development.

---

## 📁 Folder Structure

```text
Data_Analysis/
├── eda.py
├── plots/
│   ├── 01_univariate_histograms.png
│   ├── 02_univariate_boxplots.png
│   ├── 03_univariate_violinplots.png
│   ├── 04_crop_distribution.png
│   ├── 05_crop_pie_chart.png
│   ├── ...
│   └── 17_3d_scatter_plot.png
└── README.md
```

---

## 🎯 Objectives

* Understand the distribution of soil and environmental features.
* Detect missing values and outliers.
* Analyze relationships among variables.
* Identify patterns across crop categories.
* Support feature selection and model building.

---

## 📊 Dataset Summary

| Metric           | Value    |
| ---------------- | -------- |
| Total Samples    | 2,200    |
| Total Crops      | 22       |
| Features         | 7        |
| Dataset Type     | Balanced |
| Samples per Crop | 100      |

### Features Analyzed

* Nitrogen (N)
* Phosphorous (P)
* Potassium (K)
* Temperature
* Humidity
* pH
* Rainfall

---

## 🔍 Univariate Analysis

The following analyses were performed on individual features:

### Histograms

Visualize feature distributions and identify skewness.

### Boxplots

Detect outliers and observe spread.

### Violin Plots

Combine density estimation and boxplot information.

### Crop Distribution

Verify class balance across all crop categories.

### Crop Percentage Analysis

Pie chart representation of crop frequencies.

### Key Observations

* Dataset is perfectly balanced.
* No missing values detected.
* Features span different numeric ranges.
* Several features contain mild outliers.

---

## 🔗 Bivariate Analysis

Relationships between pairs of variables were analyzed using:

* Scatter plots
* Correlation heatmaps
* Nutrient relationship visualizations
* Climate parameter comparisons

### Important Findings

* Certain crops exhibit unique nutrient patterns.
* High potassium levels are common in fruit crops.
* Rainfall strongly influences crop suitability.
* Temperature and humidity jointly affect crop growth.

---

## 📈 Multivariate Analysis

Multivariate techniques were used to understand complex feature interactions.

### Techniques Used

* Pairplots
* Cluster Maps
* Feature Importance Analysis
* Radar Charts
* 3D Scatter Visualization

### Insights

* N, P, and K are the most influential predictors.
* Environmental variables significantly improve classification performance.
* Crop groups naturally form clusters in feature space.

---

## 📊 Generated Visualizations

| Category              | Number of Plots |
| --------------------- | --------------- |
| Univariate Analysis   | 5               |
| Bivariate Analysis    | 6               |
| Multivariate Analysis | 6               |
| Total Visualizations  | 17              |

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 🚀 Running the Analysis

```bash
cd Data_Analysis
python eda.py
```

Generated plots will be saved inside the `plots/` directory.

---

## 📌 Conclusion

The exploratory analysis confirmed that the dataset is clean, balanced, and well-suited for machine learning applications. Strong relationships between soil nutrients, climatic conditions, and crop categories justify the use of supervised learning techniques for crop recommendation.

---

### 🌾 Part of OptiCrop – Smart Agricultural Production Optimization Engine
