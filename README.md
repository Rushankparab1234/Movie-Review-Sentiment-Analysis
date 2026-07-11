# 🎬 Movie Review Sentiment Analysis using NLP & Machine Learning

## 📌 Project Overview

This project is a **Natural Language Processing (NLP)** based Sentiment Analysis system that classifies movie reviews as **Positive** or **Negative**. The project demonstrates the complete machine learning workflow, including text preprocessing, feature extraction using TF-IDF, model training, evaluation, and prediction of new movie reviews.

The objective is to build an accurate sentiment classification model while gaining practical experience with NLP preprocessing techniques and supervised machine learning algorithms.

---

# 🚀 Features

* Clean and preprocess movie review text
* Remove HTML tags, punctuation, numbers, URLs, and stopwords
* Apply Porter Stemming
* Convert text into numerical features using **TF-IDF**
* Train two machine learning models:

  * Logistic Regression
  * Multinomial Naive Bayes
* Evaluate models using:

  * Accuracy
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix
  * Classification Report
* Predict sentiment of custom movie reviews





# 📊 Dataset

**Dataset:** IMDB Movie Reviews Dataset

* Total Reviews: **50,000**
* Positive Reviews: **25,000**
* Negative Reviews: **25,000**

Dataset Columns:

| Column    | Description          |
| --------- | -------------------- |
| review    | Movie review text    |
| sentiment | Positive or Negative |



# 🛠️ Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* NLTK
* Scikit-learn
* Matplotlib
* Seaborn



# 🧹 NLP Preprocessing Pipeline

The following preprocessing steps were applied to each review:

* Convert text to lowercase
* Remove HTML tags
* Remove URLs
* Remove punctuation
* Remove numbers
* Tokenize text
* Remove English stopwords
* Apply Porter Stemming

Example:

**Original Review**


This movie was AMAZING!!! I loved it. Rating: 10/10


**Processed Review**


movi amaz love rate




# 🔍 Feature Extraction

The cleaned reviews were converted into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.


TfidfVectorizer(max_features=5000)


TF-IDF assigns higher importance to informative words while reducing the influence of commonly occurring words.



# 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

### 1. Logistic Regression

* Linear classification algorithm
* Performs exceptionally well on high-dimensional text data
* Selected as the best-performing model

### 2. Multinomial Naive Bayes

* Probabilistic classifier
* Efficient for text classification
* Fast training and prediction



# 📈 Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

## Logistic Regression Performance

| Metric    | Score    |
| --------- | -------- |
| Accuracy  | **88%**  |
| Precision | **0.88** |
| Recall    | **0.88** |
| F1 Score  | **0.88** |

### Classification Report

| Class    | Precision | Recall | F1-Score | Support |
| -------- | --------: | -----: | -------: | ------: |
| Negative |      0.89 |   0.87 |     0.88 |    4961 |
| Positive |      0.87 |   0.90 |     0.89 |    5039 |



## Multinomial Naive Bayes Performance

| Metric    | Score    |
| --------- | -------- |
| Accuracy  | **85%**  |
| Precision | **0.85** |
| Recall    | **0.85** |
| F1 Score  | **0.85** |

### Classification Report

| Class    | Precision | Recall | F1-Score | Support |
| -------- | --------: | -----: | -------: | ------: |
| Negative |      0.85 |   0.84 |     0.84 |    4961 |
| Positive |      0.84 |   0.85 |     0.85 |    5039 |



# 🏆 Best Model

After comparing both models, **Logistic Regression** achieved the highest overall performance.

| Model               | Accuracy  |
| ------------------- | --------- |
| Logistic Regression | **88%** ✅ |
| Naive Bayes         | **85%**   |

Therefore, Logistic Regression was selected as the final sentiment classification model.



# 💻 Predicting New Reviews

Example:

```python
review = "This movie was absolutely fantastic. I loved every minute."

print(predict_sentiment(review))
```

Output:

Positive 


Another example:

```python
review = "Worst movie ever. Completely boring and a waste of time."

print(predict_sentiment(review))
```

Output:

```
Negative 
```



# 📚 Skills Demonstrated

* Natural Language Processing (NLP)
* Text Cleaning
* Stopword Removal
* Stemming
* TF-IDF Feature Extraction
* Logistic Regression
* Multinomial Naive Bayes
* Model Evaluation
* Classification Metrics
* Sentiment Analysis
* Python Programming
* Data Preprocessing
* Machine Learning Workflow


# 📌 Future Improvements

* Add WordCloud visualization
* Hyperparameter tuning
* Try advanced models such as Support Vector Machine (SVM), Random Forest, XGBoost, and transformer-based models like BERT
* Perform cross-validation for more robust evaluation



# 🎯 Learning Outcomes

Through this project, I learned how to:

* Perform end-to-end NLP preprocessing
* Convert text into machine learning features using TF-IDF
* Train and compare multiple classification models
* Evaluate models using standard performance metrics
* Predict sentiment for unseen movie reviews
* Build a complete machine learning pipeline for text classification


# 📄 License

This project is intended for educational and learning purposes.
