import streamlit as st
from deep_translator import GoogleTranslator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import assemblyai as aai

# Initialize AssemblyAI API key
aai.settings.api_key = ""

def transcribe_audio(file):
    config = aai.TranscriptionConfig(speaker_labels=True, language_code='hi')
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(file, config)
    transcript_text = ' '.join([word.text for word in transcript.words])
    return transcript, transcript_text

def analyze_sentiment(text):
    translated_text = GoogleTranslator(source='auto', target='en').translate(text)
    analyzer = SentimentIntensityAnalyzer()
    return analyzer.polarity_scores(translated_text)

def display_transcript_and_timestamps(transcript, search_words):
    st.subheader("Transcript")
    st.write(' '.join([word.text for word in transcript.words]))
    st.divider()
    st.subheader("Timestamps")
    
    word_positions = {word.lower(): [] for word in search_words}
    for word_info in transcript.words:
        word_info_text = word_info.text.lower()
        if word_info_text in word_positions:
            start_seconds = word_info.start / 1000.0
            word_positions[word_info_text].append(start_seconds)
    
    for word, positions in word_positions.items():
        if positions:
            st.write(f"Found '{word}' {len(positions)} times in the transcript.")
            for position in positions:
                st.write(f"Occurrence of '{word}' - Start: {position:.2f}s")
        else:
            st.write(f"'{word}' not found.")

def display_sentiment_analysis(sentiment_dict):
    st.subheader("Sentiment Analysis")
    if sentiment_dict['compound'] >= 0.05:
        st.write("## :green[POSITIVE]")
    elif sentiment_dict['compound'] <= -0.05:
        st.write("## :red[NEGATIVE]")
    else:
        st.write("## :grey[NEUTRAL]")

# Streamlit UI setup
st.header('**:blue[Sentiment Analysis] and :red[Timestamps]**')
st.subheader('Upload an Audio file')
file_address = st.file_uploader('Upload your audio file', label_visibility='collapsed')
st.divider()
st.subheader('Enter the Keywords (space separated)', help="Always clear the input field before transcripting a new audio file.")
search_words = st.text_input("Enter keywords", label_visibility='collapsed').split()

if file_address and search_words:
    try:
        transcript, transcript_text = transcribe_audio(file_address)
        display_transcript_and_timestamps(transcript, search_words)
        
        sentiment_dict = analyze_sentiment(transcript_text)
        display_sentiment_analysis(sentiment_dict)
        
        st.toast('Transcription and Timestamping Done!', icon='🥳')
    
    except Exception as e:
        st.error(f"An error occurred: {e}")

# 990 243
