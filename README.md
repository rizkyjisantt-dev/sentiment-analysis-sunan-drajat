# Sentiment Analysis of Sunan Drajat Tourism in Lamongan with K‑Nearest Neighbors (KNN)

## 📌 Project Overview
This project analyzes public sentiment toward the Sunan Drajat tourism site in Lamongan by classifying opinion texts as positive, neutral, or negative, using the K‑Nearest Neighbors (KNN) classification algorithm.

## 🚀 Objectives
- Collect and preprocess public reviews or comments about Sunan Drajat tourism in Lamongan.
- Perform Exploratory Data Analysis (EDA) to understand sentiment distribution.
- Represent text data using appropriate features (e.g. TF‑IDF or bag-of-words).
- Train and evaluate a KNN classifier for sentiment classification.
- Identify which sentiment category appears most frequently.
- Offer insights or recommendations for improving tourist satisfaction.

## 🔍 Methodology
1. **Data Collection & Preprocessing**  
   - Web scraping or gathering review/comments data
   - Text normalization: tokenization, lowercasing, stop-word removal, stemming/lemmatizing

2. **Exploratory Data Analysis**  
   - Visualize sentiment distribution (bar charts, pie charts)
   - Word frequency analysis for each sentiment category

3. **Feature Engineering**  
   - Apply TF‑IDF or bag-of-words to vectorize text
   - Optional: Use techniques like Information Gain for feature selection

4. **Machine Learning: K‑Nearest Neighbors (KNN)**
   - Train a KNN classifier using the extracted features
   - Tune hyperparameters (e.g. k, distance metric)
     
6. **Model Evaluation**
   - Evaluate using metrics: Accuracy, Precision, Recall, F1-score
   - Use confusion matrix and cross-validation if applicable
     
7. **Conclusion & Insights**
   - Identify the dominant sentiment (positive/neutral/negative)
   - Suggest recommendations for tourism stakeholders based on sentiment trends

## 🛠 Dependencies & Technologies
- Programming Language: Python
- Libraries: pandas, NumPy, scikit-learn, matplotlib / seaborn
- Text Processing: NLTK or spaCy; scikit-learn’s TF‑IDF
- Machine Learning Model: scikit-learn’s KNeighborsClassifier

## 📁 Repository Structure
sentiment-analysis-sunan-drajat/  
├── data/                # Raw and cleaned review text data  
├── notebooks/           # EDA and modeling notebooks  
├── src/                 # Scripts for preprocessing, feature extraction, modeling  
├── results/             # Model evaluation results & visualizations  
├── README.md            # Project documentation  

## 🎯 How to Reproduce
1. Clone the repository:
   git clone https://github.com/rizkyjisantt-dev/sentiment-analysis-sunan-drajat.git
   cd sentiment-analysis-sunan-drajat
2. Install dependencies:
   pip install -r requirements.txt
3. Run notebooks or scripts for preprocessing, modeling, and evaluation.

## 📊 Related Research
Sentiment analysis of Indonesian tourism has shown KNN to be effective in classifying public sentiment, similar to other case studies on tourism sentiment using KNN and SVM methods

## 📈 Expected Outcome
- Visualizations showing public sentiment distribution toward Sunan Drajat tourism.
- Performance metrics of your KNN classifier.
- Clear insights and recommendations for tourism stakeholders.

## 📌 Contributions & License
This repository is open for contributions. Feel free to submit pull requests or open issues for feedback and collaboration.
