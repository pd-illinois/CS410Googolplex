# CourseProject

Please fork this repository and paste the github link of your fork on Microsoft CMT. Detailed instructions are on Coursera under Week 1: Course Project Overview/Week 9 Activities.

**Introduction**

The social network has the capability to influence and change what people think, do, and react to everything happening around them. The social network has the capability to incept thoughts and ideas at an individual and societal level. 

Around election season, when there is a political environment around the nation, social media tools add fuel to political polarity. Through this project, we would like to identify the political sentiments and top topics that are discussed.

**Project Overview**
We scraped Twitter data, preprocessed it and performed the following for US Midterm Election as a key area.
* Sentiment Analysis and prediction
        With Naïve Bayes Classification
        With K-Nearest Neighbor Classification
* Topic Analysis with Latent Dirichlet Allocation

**Goals**

Key Goals for the project that we set and achieved were
    *Sentiment Analysis*  : Identify overall positive , negative and neutral sentiments towards elections and respective parties in US
    *Prediction* : Predict tweets for sentiments using Naïve Bayes and KNN. Also perform a comparison which Algorithm performs better and impact of data cleaning techniques on precision and accuracy of predictions.
    *Topic Analysis* : Identify top topics in tweets and predict the dominant topic and its percentage for each tweet.
    *Visualize* : Lastly compare our findings and present them as part of our final project.

**Data Preparation:**

Step 1: Data Scrapping & Storage

*Raw Data Capture*
We used SNSCRAPE for capturing the tweets. We captured 20000 tweets from 1st July to 8th November (Midterm Election Day in US).
*Ingestion and Storage*
All the 20000 tweets are available in data Folder in tweets_final.csv. You can use these tweets as the main data for this project.

Note that this is a one time activity and you do not need to run this script again. However If you want to download the tweets again, use the script below to download them again.

Step 2: Data Preprocessing

In the Data Prepocessing areas , we aim to clean the collected tweets and use them at various stages to calculate sentiment accuracy. At this stage our goal is to check how Data Cleaning impacts Sentiment analysis.

This step is divided into three sub parts

a. Initial Data preperation (Current File)
    Replacing Empty Locations with Unknown
    Filtering out Non English Tweets
    Create pickle for 1st Sentiment Analysis baseline using VADER
    
b. Generic Data Cleaning
    Lowercaseing
    Removing special characters
    Removing Whitespaces
    Removing tagged Usernames
    Removing Hashtags
    Removing RT
    Removing URLs and Http tags
    Removing Punctuations
    Create pickle package for 2nd Sentiment Analysis baseline
    
c. NLP Specific Data Cleaning
    Removing Emojis
    Stopword Removal
    Lemmatization
    Create pickle package for 3rd Sentiment Analysis baseline using VADER
 
Step 3: Exploratory Analysis and Baseline Sentiment Analysis Using VADER

Valence aware dictionary for sentiment reasoning (VADER) is a popular rule-based sentiment analyzer. It uses a list of lexical features (e.g. word) which are labeled as positive or negative according to their semantic orientation to calculate the text sentiment. Vader sentiment returns the probability of a given input sentence to be postive, negative, neutral.

Vader is optimized for social media data and can yield good results when used with data from twitter, facebook, etc.

*Cleaned Dataset Columns:*

    Date 	        Date on which tweet was posted	
    ID		
    location	 Location from where tweet was posted	
    tweet	     Content of the tweet	
    num_of_likes	Number of likes on the tweet	
    num_of_retweet	Number of retweets	
    language	    language of the tweet, in our case it's english	
    cleaned_tweets	cleaned tweets by removing the punctuations	
    final_cleaned_tweets    cleaned tweets using lemmatization	

 **Data Understanding**

 1. What are the words/topics discussed:
 
 2. What are the most popular hashtags of each tweet type ?
 
 ![image](https://user-images.githubusercontent.com/109382284/206284240-af6be292-19b1-4dd7-8e3b-0fcb0df0c3f3.png)
 
 
 For scraping our tweets, we have used the words vote, voting, elections, etc. and we see those are mostly commonly used words in the tweets and all the other words  are related to US midterm elections.
 
 3. What is the overall polarity of the tweets ?
 ![image](https://user-images.githubusercontent.com/109382284/206284649-ae9d4ab4-2361-4332-bfc1-40e7f6b35605.png)

 

This bar graph shows that in the original not preprocessed data, we see that the number of positive tweets in our original not processed tweets are more than the positive number of tweets in cleaned and finally cleaned tweets. We wanted to have a fair distribution among the positive, neutral and negative tweets. 
 
 
 This is the master script for Our Project - US Midterm Elections 2022 - Twitter Sentiment Analysis.

This Jupyter Notebook is divided into Various sections as per our Project Proposal.
Broadly , these are
1) Raw Data Capture (01_Twitter_scrape.ipynb)
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

https://towardsdatascience.com/evaluate-topic-model-in-python-latent-dirichlet-allocation-lda-7d57484bb5d0


