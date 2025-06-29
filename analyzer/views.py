from django.shortcuts import render
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_sentiment(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        sia = SentimentIntensityAnalyzer()
        sentiment_scores = sia.polarity_scores(text)
        
        if sentiment_scores['compound'] >= 0.05:
            sentiment = 'Positive'
        elif sentiment_scores['compound'] <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        
        context = {
            'text': text,
            'sentiment': sentiment,
            'scores': sentiment_scores
        }
        return render(request, 'analyzer/result.html', context)
    
    return render(request, 'analyzer/analyze.html')