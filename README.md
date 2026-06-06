# Veloria Tech ML Internship Assignment

## Candidate Information

**Name:** Ajay Bansal

---

# Project Overview

This project was completed as part of the Veloria Tech AI/ML Engineering Internship Assignment.

The assignment consists of:

1. Data Collection using Web Scraping
2. Machine Learning Prediction Model
3. Semantic Search using Vector Embeddings (Optional)

---

# Task 1: Data Collection Using Web Scraping

## Objective

Collect cricket match information from a publicly available cricket statistics website and save it into a CSV file.

## Tools Used

* Python
* Requests
* BeautifulSoup
* Pandas

## Data Collected

The scraper extracts ODI cricket match information including:

* Match Date
* Series
* Match Number
* Venue
* Match Result

The extracted data is stored in:

```text
match_data.csv
```

## How to Run

```bash
python Task1.py
```

---

# Task 2: Machine Learning Prediction Model

## Objective

Build a machine learning model to predict match outcomes using historical match data.

## Dataset

The dataset generated from Task 1 was used as the training dataset.

## Data Preparation

The following preprocessing steps were performed:

* Removed missing values
* Removed duplicate records
* Converted categorical values into numerical values using Label Encoding

## Features Used

* Series
* Match Number
* Venue

## Target Variable

* Winner

## Machine Learning Algorithm

### Logistic Regression

Reason for selection:

* Simple and efficient classification algorithm
* Easy to interpret
* Suitable for baseline prediction tasks

## Evaluation Metrics

The model was evaluated using:

* Accuracy Score
* F1 Score
* Confusion Matrix

## Results

Accuracy: **50.00%**

F1 Score: **0.375**

## How to Run

```bash
python Task2_Model.py
```

---


# Task 3 – Semantic Search Using Vector Embeddings

The match records were converted into natural language sentences and encoded into vector embeddings using the Sentence Transformers library.

Model Used:

* all-MiniLM-L6-v2

Approach:

1. Load match_data.csv
2. Convert each match record into a text description
3. Generate vector embeddings
4. Compare user queries against stored embeddings using cosine similarity
5. Return the 3 most relevant matches

Example Query:
"Show me matches won by India"

The system returns the most semantically similar match records based on the meaning of the query rather than exact keyword matching.


# Challenges Faced

1. Some cricket websites blocked automated requests and returned HTTP 403 errors.
2. Website structures varied and required inspection before extracting data.
3. The dataset contained a limited number of matches, which affected model performance.
4. Limited historical data reduced the predictive power of the model.

---

# Libraries Used

```text
requests
beautifulsoup4
pandas
scikit-learn
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

# Project Structure

```text
veloria-tech-ml-intern-assignment/

│
├── Task1.py
├── Task2_Model.py
├── match_data.csv
├── README.md
└── requirements.txt
```

---

# Future Improvements

* Collect larger historical cricket datasets.
* Include team-level statistics.
* Include home/away information.
* Experiment with Random Forest and XGBoost models.
* Implement semantic search using vector embeddings.

---

# Conclusion

This project demonstrates practical experience in:

* Web Scraping
* Data Cleaning
* Machine Learning
* Python Programming
* Data Analysis

The assignment was completed using publicly available cricket match data and standard Python machine learning libraries.
