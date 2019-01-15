# Twitter Sentiment Analysis Tutorial
# https://www.youtube.com/watch?v=o_OZdbCzHUA&list=PL2-dafEMk2A6QKz1mrk1uIGfHkC1zZ6UU&index=2

# create a Twitter API

# install dependencies:
# pip install tweepy  --> library for accessing our Twitter API
# pip install textblob --> perform sentiment analysis
# python -m texblob.download_corpora

# textblob demo on python terminal

import tweepy
from textblob import TextBlob
import csv
import numpy as np
import matplotlib.pyplot as plt


# STEP 1 - AUTHENTICATE

# create 4 variables to authenticate to Twitter
# copy the value from the part "Keys and token" from the app

consumer_key = '0OGhjX0XySXnMh8T6YJTpj832'
consumer_secret = 'IMJri1jwVTPih13OcanSSUZ37BX6R0KR7cYvhef9P9f5fuwEGM'

access_token = '1187586672-f8rta6yTNm1QUh4ckPt8RTlt0QzmdJLX2bgJuwf'
access_token_secret = '7uYIVhsmHTsemWEO5wrjlyTYm5BUQvAs4HJHKVNUAmtJw'


# STEP 2 - LOGIN

# variable to login
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set the access token method
auth.set_access_token(access_token, access_token_secret)

# create main variable to do Twitter magic
api = tweepy.API(auth)  # to perform Twitter tasks (Create Tweets, delete Tweets, find Twitter Users ...)


# STEP 3 - RETRIEVE TWEETS

# collect Tweets that contains certain keywords
public_tweets = api.search('Macron', count=100)    # collect a list of Tweets that contain a word
nb_tweet = 100

# polarity : how negative or positive the text is
# subjectivity : how much is it an opinion versus how factual

"""
CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
and label each one as either 'positive' or 'negative', depending on the sentiment 
You can decide the sentiment polarity threshold yourself
"""


# array where the polarity of each tweet will be stored
array_polarity = np.zeros((1, nb_tweet))
i = 0
nb_neutral = 0
nb_pos = 0
nb_neg = 0

# STEP 4 - ANALYSE THE TWEETS AND LABELED THEM IN A FILE

# create the csv file
with open('tweet_sentiment.csv', mode='w') as csv_file:
    # create the headers
    fieldnames = ['tweet', 'sentiment polarity', 'sentiment subjectivity', 'analysis']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()

    # loop for each tweet
    for tweet in public_tweets:
        print(tweet.text.encode("utf-8"))  # print each tweet in string version
        # calculate sentiment of the tweet (-1 < sentiment < 1)
        analysis = TextBlob(tweet.text)     # store sentiment analysis
        print(analysis.sentiment)           # print the analysis attribute

        # calculate if it's neutral, positive or negative
        if analysis.polarity < 0:
            analysis_word = 'negative'
            nb_neg = nb_neg+1
        elif analysis.polarity == 0:
            analysis_word = 'neutral'
            nb_neutral = nb_neutral + 1
        else:
            analysis_word = 'positive'
            nb_pos = nb_pos + 1

        # store the polarity in the array
        array_polarity[0][i] = analysis.polarity
        i = i+1

        print(analysis_word)
        writer.writerow({'tweet': tweet.text.encode("utf-8"), 'sentiment polarity': analysis.polarity, 'sentiment subjectivity': analysis.subjectivity, 'analysis': analysis_word})
        print("")

    writer.writerow({'tweet': ' ', 'sentiment polarity': ' ', 'sentiment subjectivity': ' ', 'analysis': ' '})

    print(array_polarity)
    mean_array = np.mean(array_polarity)
    writer.writerow({'tweet': ' POPULARITY = ', 'sentiment polarity': mean_array, 'sentiment subjectivity': ' ', 'analysis': ' '})


    # STEP 5 - SUMMARIZE THE RESULT IN A PIECHART

    # Data to plot
    labels = 'Neutral', 'Positive', 'Negative'
    sizes = [nb_neutral, nb_pos, nb_neg]
    colors = ['lightskyblue', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)  # explode 1st slice

    # Plot
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title('Popularity of Macron over 100 tweets')
    plt.show()
    plt.savefig('Result.png')

