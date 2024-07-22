
# 🎧 Speech Timestamp and Sentiment Analysis with Streamlit

This project leverages Streamlit to provide an easy-to-use web interface for transcribing audio files, analyzing the sentiment of the transcript, and displaying timestamps for specified keywords. 

## 🛠️ Features

- **Transcription:** Converts speech to text using AssemblyAI.
- **Sentiment Analysis:** Analyzes the sentiment of the transcript using VADER Sentiment Analysis.
- **Timestamps:** Displays timestamps for specified keywords in the transcript.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Dru-O7/Speech-Timestamp.git 
   ```
   ```
   cd Speech-Timestamp 
   ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Set your AssemblyAI API key in index.py:

```python
aai.settings.api_key = "YOUR_API_KEY_HERE"
```

## 🚀 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```
2. Upload an audio file and enter keywords:

    - Upload your audio file through the web interface.

    - Enter the keywords (space separated) for which you want to see timestamps.

3. View the results:

    - The transcript of the audio file will be displayed.

    - Sentiment analysis of the transcript will be shown.

    - Timestamps for the specified keywords will be listed.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

Enjoy using the app! 🎉
