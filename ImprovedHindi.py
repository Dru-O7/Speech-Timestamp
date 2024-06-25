import joblib
from nltk.tokenize import word_tokenize
import nltk

classifier = joblib.load('svm_classifier.joblib')
vectorizer = joblib.load('tfidf_vectorizer.joblib')

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalpha()]
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text

def predict_sentiment(text):
    preprocessed_text = preprocess_text(text)
    text_tfidf = vectorizer.transform([preprocessed_text])
    prediction = classifier.predict(text_tfidf)[0]
    return prediction

input_text = transcript.text
predicted_sentiment = predict_sentiment(input_text)
print(f"Predicted Sentiment: {predicted_sentiment}")
