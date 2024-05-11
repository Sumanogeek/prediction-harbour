from textblob import TextBlob

def predict_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity
    
    # Determine sentiment label based on polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

if __name__ == "__main__":
    # Example text for sentiment analysis
    text = "I love this product, it's amazing!"

    # Predict sentiment
    sentiment = predict_sentiment(text)
    print("Sentiment:", sentiment)
