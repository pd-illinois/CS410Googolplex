# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

Important 

Download stopwords before running the program

python -m nltk.downloader stopwords (if not downloaded while loading libraries)
pip install wordcloud
pip install emot
pip install textblob
pip install langdetect
pip install nltk


**Introduction**

This is the master script for Our Project - US Midterm Elections 2022 - Twitter Sentiment Analysis.

This Jupyter Notebook is divided into Various sections as per our Project Proposal.
Broadly , these are
1) Raw Data Capture (Using Snscrape)
2) Ingest and Store (Twitter_Scrap.ipynb)
3) NLP Pipeline
    - Data Preproccessing ()
    - Sentiment analysis and Prediction using 
        - Naive Bayes (Twitter_NB.ipynb)
        - K Nearest Neighbor (Twitter_KNN.ipynb)
    - Topic Analysis using
        - Latent Dirichlet Allocation (Twitter_LDA.ipnyb)
4) Visualizations
    - Overall Results of Sentiment and Topic Anlaysis
    - Top findings in contrast with Midterm Elections 

**Important Note** : Before running this script , please ensure you have all the pre requisites completed as mentioned in README.md.


**1. Raw Data Capture**

We used SNSCRAPE for capturing the tweets. The tweets were captures in 5 parts. We captured 20000 tweets per month from July, August, September and October to 8th November (Midterm Election Day in US). In addition we also captured another set of 20000 tweets across July to 8th November to get a generalized data (tweets_knn.csv)

**2. Ingestion and Storage**

All the 100000 tweets are available in Data Folder as tweets_all.csv file. Due to the performance limitation of local machines, we reduced the dataset for KNN and limited it to 20000 tweets accross the July - Nov timeframe.

**This is a one time activity and does not require re download** . We will be using tweets_all.csv as our initial data source for this project. In case of KNN, we had to take a smaller sample set of 20000 Tweets ( tweets_knn.csv ) as the training times for KNN was pretty huge with a dataset of 100000 tweets.

    
**3. NLP Pipeline**
**3.1 Data Preprocessing**
- Write up on Lemmatization , normalization etc

**3.2 Sentiment Analysis**
**3.3 Naive Bayes** --> What are we predicting - put sample code
**3.4 K-Nearest Neighbor** - --> What are we predicting - put sample code
**3.5 Latent Dirichlet Allocation**

**4. Visualization**



**----------------------------REFERENCES-----------------------**
https://towardsdatascience.com/4-python-libraries-to-detect-english-and-non-english-language-c82ad3efd430

https://pypi.org/project/langdetect/
https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af

https://github.com/cjhutto/vaderSentiment
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.



