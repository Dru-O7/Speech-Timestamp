import assemblyai as aai

aai.settings.api_key = "Enter Your API KEY Here"
audio_url = "test-audio.mp3"
transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_url)
print(transcript)

search_words =[]
nums=int(input("Enter the Number of Words to Search: "))
for i in range(nums):
    a=input()
    search_words.append(a)

if hasattr(transcript, 'words') and transcript.words:
    matches = transcript.word_search(search_words)
    for match in matches:
        print(f"Found '{match.text}' {match.count} times in the transcript.")
        for word_info in transcript.words:
            if word_info.text == match.text:
                start_seconds = word_info.start / 1000.0
                print(f"Occurrence of '{word_info.text}' - Start: {start_seconds:.2f}s")
else:
    print("Transcription failed or no words found in the transcript.")
