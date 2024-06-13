import tkinter as tk
from tkinter import messagebox
import assemblyai as aai

def transcribe_and_search():
    api_key = api_key_entry.get()
    audio_url = audio_url_text.get("1.0", tk.END).strip()
    search_words = search_words_entry.get().strip().split()

    aai.settings.api_key = api_key

    try:
        transcriber = aai.Transcriber()
        config = aai.TranscriptionConfig(language_detection=True)
        transcript = transcriber.transcribe(audio_url, config=config)
    except Exception as e:
        messagebox.showerror("Transcription Error", str(e))
        return


    results_text.delete("1.0", tk.END)


    normalized_search_words = [word.lower() for word in search_words]

    for word in normalized_search_words:
        found = False
        count = 0
        for word_info in transcript.words:

            if word_info.text.lower() == word:
                if not found:
                    results_text.insert(tk.END, f"Found '{word}' in the transcript:\n")
                    found = True
                count += 1
                start_seconds = word_info.start / 1000.0
                results_text.insert(tk.END, f"Occurrence of '{word_info.text}' - Start: {start_seconds:.2f}s\n")
        if not found:
            results_text.insert(tk.END, f"'{word}' not found in the transcript.\n")
        else:
            results_text.insert(tk.END, f"'{word}' found {count} times in the transcript.\n")

root = tk.Tk()
root.title("Audio Transcription and Word Search")

tk.Label(root, text="API Key:").grid(row=0, column=0, padx=10, pady=10)
api_key_entry = tk.Entry(root, width=50)
api_key_entry.grid(row=0, column=1, padx=10, pady=10)
api_key_entry.insert(0, "0703b6d8e89d434cabacd13c526d2480")

tk.Label(root, text="Audio URL:").grid(row=1, column=0, padx=10, pady=10)
audio_url_text = tk.Text(root, width=50, height=5)
audio_url_text.grid(row=1, column=1, padx=10, pady=10)
# audio_url_text.insert(tk.END, "test-audio.mp3")

tk.Label(root, text="Words to Search (space-separated):").grid(row=2, column=0, padx=10, pady=10)
search_words_entry = tk.Entry(root, width=50)
search_words_entry.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Transcribe and Search", command=transcribe_and_search)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

results_text = tk.Text(root, height=15, width=80)
results_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
