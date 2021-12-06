from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect

def checking_language(sentence):
    if detect(sentence) == 'en':
        return 1
    else:
        return 0

def predict(sentence):
    if checking_language(sentence) == 0:
        raise Exception("The text language used must be English")
    else:
        sid_obj = SentimentIntensityAnalyzer()
        sentiment_dict = sid_obj.polarity_scores(sentence)
        print("Overall sentiment dictionary is : ", sentiment_dict)
        print("sentence was rated as ", sentiment_dict['neg'] * 100, "% Negative")
        print("sentence was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
        print("sentence was rated as ", sentiment_dict['pos'] * 100, "% Positive")
        print("Sentence Overall Rated As", end=" ")
        # decide sentiment as positive, negative and neutral
        if sentiment_dict['compound'] >= 0.05:
            return "Positive"
        elif sentiment_dict['compound'] <= - 0.05:
            return "Negative"
        else:
            return "Neutral"
