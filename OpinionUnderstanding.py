from textblob import TextBlob

def Analyze(text):
    analyze = TextBlob(text)
    if analyze.sentiment.polarity > 0.00001:
        return 1
    if analyze.sentiment.polarity < -0.00001:
        return -1
    else:
        return 0