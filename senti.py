import tweepy as tp
from textblob import TextBlob
y= input("type your sentece: ")
edu =TextBlob(y)
x=edu.sentiment.polarity
if x<0:
  print("negative")
elif x==0:
    print("Neutral")
elif x>0 and x<=1:
    print("Positve")