from textblob import TextBlob

text = input("Enter a sentence: ")
if not text.strip():
    text = "Artificial Intelligence is great and very helpful"

analysis = TextBlob(text)
score = analysis.sentiment.polarity

print("Sentiment Polarity Score:", score)
if score > 0:
    print("Sentiment: Positive")
elif score < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
