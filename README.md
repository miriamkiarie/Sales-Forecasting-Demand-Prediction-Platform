# Sales-Forecasting-Demand-Prediction-Platform
Enterprise-grade sales forecasting platform leveraging SARIMA, Prophet, Machine Learning, Hybrid Models, and LSTM Deep Learning for demand prediction, uncertainty estimation, and business decision support.


# 📈 Sales Forecasting & Inventory Analytics Platform

## Project Overview

This project is an end-to-end sales forecasting and business analytics platform developed to demonstrate how data-driven forecasting can support inventory planning, demand management, and strategic business decision-making.

The project combines traditional statistical forecasting methods, machine learning models, deep learning approaches, and interactive business intelligence dashboards into a single analytical workflow.

The solution was developed using Python and Streamlit and is designed to be adaptable across multiple industries including:

* Retail
* E-commerce
* FMCG
* Pharmaceutical Distribution
* Supply Chain Operations
* Inventory Management

---

## Business Problem

Organizations often struggle to answer critical operational questions such as:

* What will future sales look like?
* Which products are likely to experience increased demand?
* How much inventory should be ordered?
* Which forecasting model provides the most accurate predictions?
* How can management monitor performance through a single dashboard?

This project addresses these challenges through forecasting, analytics, and visualization.

---

# Project Workflow

## 1. Data Ingestion

The platform supports loading datasets from:

* CSV files
* Excel files
* SQL Databases (extensible)
* Data warehouses (future integration)

Implemented through:

```text
07_dataset_switcher.ipynb
08_dataset_loader.ipynb
```

### Features

* Automatic file loading
* Dataset validation
* Missing value identification
* Dataset switching
* Interactive previews

---

## 2. Exploratory Data Analysis (EDA)

Implemented in:

```text
01_EDA_decomposition.ipynb
```

### Objectives

* Understand sales behavior
* Identify trends
* Detect seasonality
* Detect outliers
* Evaluate data quality

### Analysis Performed

* Descriptive statistics
* Time-series decomposition
* Trend analysis
* Seasonal analysis
* Missing value analysis
* Distribution analysis

### Business Value

Provides insight into historical sales patterns and helps identify key drivers of demand.

---

## 3. Feature Engineering

Implemented in:

```text
02_feature_engineering.ipynb
```

### Features Created

* Lag Features
* Rolling Averages
* Moving Statistics
* Date-based Features

  * Day
  * Month
  * Quarter
  * Year
* Seasonal Indicators

### Business Value

Transforms raw sales data into predictive features suitable for forecasting models.

---

# Forecasting Models

The project evaluates multiple forecasting techniques to identify the best-performing model.

---

## 4. SARIMA Forecasting

Implemented in:

```text
02_SARIMA.ipynb
```

### Purpose

Captures:

* Trend
* Seasonality
* Autocorrelation

### Strengths

* Interpretable
* Effective for seasonal sales patterns
* Industry-standard forecasting approach

---

## 5. Prophet Forecasting

Implemented in:

```text
03_prophet.ipynb
```

### Purpose

Forecasts demand while handling:

* Trend changes
* Seasonality
* Missing observations

### Advantages

* Robust forecasting
* Easy interpretation
* Business-friendly outputs

---

## 6. Machine Learning Forecasting

Implemented in:

```text
04_ML_forecasting.ipynb
```

### Models Evaluated

* Random Forest
* XGBoost
* LightGBM

### Features Used

* Lag Variables
* Rolling Windows
* Seasonal Features

### Advantages

* Captures nonlinear patterns
* Handles complex demand behavior
* Improved forecasting accuracy

---

## 7. Hybrid Forecasting Model

Implemented in:

```text
05_hybrid_model.ipynb
```

### Approach

Combines:

* Statistical Forecasting
* Machine Learning Forecasting

### Benefits

* Improved forecast stability
* Reduced forecast error
* Better handling of changing demand patterns

---

## 8. Deep Learning Forecasting

Implemented in:

```text
06_deep_learning_LSTM.ipynb
```

### Model

Long Short-Term Memory (LSTM)

### Purpose

Captures:

* Long-term temporal dependencies
* Complex demand relationships
* Sequential patterns

### Advantages

* Powerful for large-scale forecasting
* Learns temporal structures automatically

---

# Model Evaluation

Models were compared using:

### MAE

Mean Absolute Error

Measures average prediction error.

### RMSE

Root Mean Squared Error

Penalizes larger forecasting errors.

### MAPE

Mean Absolute Percentage Error

Provides business-friendly accuracy measurements.

---

# Interactive Dashboard

Built using:

```text
Streamlit
```

### Dashboard Capabilities

#### Executive Dashboard

Displays:

* Dataset Overview
* Key Metrics
* Data Quality Indicators

#### Forecasting Dashboard

Visualizes:

* Historical Sales
* Forecast Results
* Model Comparisons

#### Product Analytics

Displays:

* Product Performance
* Sales Distribution
* Demand Patterns

#### Inventory Planning

Provides:

* Reorder Recommendations
* Demand Monitoring
* Inventory Insights

#### Data Ingestion

Allows:

* CSV Upload
* Excel Upload
* Dynamic Dataset Switching

---

# Pharmaceutical Distribution Adaptation

The forecasting framework was designed to be industry-agnostic and can be adapted to pharmaceutical distribution environments.

Potential pharmaceutical applications include:

### Product Analytics

* Fast-moving medicines
* Slow-moving medicines
* Category demand analysis

### Inventory Management

* Reorder point calculation
* Safety stock recommendations
* Demand forecasting

### Pricing Analytics

* Competitor price comparisons
* Margin optimization
* Pricing strategy evaluation

### Customer Analytics

* Pharmacy performance
* Payment reliability analysis
* Customer segmentation

---

# Technology Stack

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Plotly
* Streamlit

### Forecasting

* SARIMA
* Prophet

### Machine Learning

* XGBoost
* LightGBM
* Random Forest

### Deep Learning

* TensorFlow
* Keras
* LSTM

### Databases

* SQL
* MySQL (Extensible)

---

# Key Outcomes

This project demonstrates the ability to:

✅ Clean and transform data

✅ Perform exploratory data analysis

✅ Engineer predictive features

✅ Build forecasting models

✅ Compare model performance

✅ Develop interactive dashboards

✅ Support inventory planning decisions

✅ Generate business insights

✅ Adapt forecasting frameworks to different industries

---

## Future Enhancements

* Real-time database integration
* Automated forecasting pipelines
* Inventory optimization engine
* Forecast report generation
* Cloud deployment
* Pharmaceutical ERP integration

---

## Author

Miriam Kiarie

Data Analytics | Forecasting | Machine Learning  | SQL | Python

---



