# Sentiment Analysis on Twitter

## Overview

This code is a solution for a challenge in a Youtube video [Learn Python for Data Science #2](https://www.youtube.com/watch?v=o_OZdbCzHUA&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=2) to analyse sentiment in tweets about a subject. 
The code uses the tweepy library to access the Twitter API and the TextBlob library to perform Sentiment Analysis on each Tweet. 
We'll be able to see how positive or negative each tweet is about whatever topic we choose.

The challenge is to save each Tweet to a CSV file and label each one as either 'positive' or 'negative', depending on the sentiment. 

## Dependencies

- tweepy 
- textblob 
Install missing dependencies using pip

## Usage

Once you have your dependencies installed via pip, run the script in terminal via

```python 
python twitter_sentiment.py
```

## Challenge 

I choose the topic "Macron". 
The code will analyse the 100 latest tweets about Macron and tell the sentiment of each tweet: rather neutral, positive or negative. 
The tweets and their label will be saved into a CSV file. 
Then a piechart will summarize and show the result. 

## Result 

Here is one possible result.  
![PieChart](/images/Piechart.png)




