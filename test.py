import os
from pydub import AudioSegment
import speech_recognition as sr
from fpdf import FPDF

# List of audio files
audio_files = [
    "/home/ninad/Akash/Audios/06_Aug.wav",
    "/home/ninad/Akash/Audios/13_Aug.wav",
    "/home/ninad/Akash/Audios/16_Aug.wav",
    "/home/ninad/Akash/Audios/23_Aug.wav"
]

# Initialize recognizer
recognizer = sr.Recognizer()

# Iterate over each audio file
for audio_file in audio_files:
    # Extract file name without extension for folder and PDF naming
    file_name = os.path.splitext(os.path.basename(audio_file))[0]

    # Create an output folder for the audio chunks
    output_folder = f"/home/ninad/Akash/Audios/{file_name}_chunks"
    os.makedirs(output_folder, exist_ok=True)

    # Initialize PDF for each audio file
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Load the audio file
    audio = AudioSegment.from_wav(audio_file)

    # Split audio into 1 minute chunks
    chunk_length_ms = 60000  # 1 minute in milliseconds
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]

    full_text = ""
    for i, chunk in enumerate(chunks):
        chunk_name = os.path.join(output_folder, f"chunk{i}.wav")
        chunk.export(chunk_name, format="wav")

        # Transcribe each chunk
        with sr.AudioFile(chunk_name) as source:
            audio_data = recognizer.record(source)
            try:
                # Use Google Web API for transcription
                text = recognizer.recognize_google(audio_data)
                print(f"Chunk {i} of {file_name} transcribed successfully.")
            except sr.UnknownValueError:
                text = "[Unintelligible]"
                print(f"Chunk {i} of {file_name} could not be transcribed.")
            except sr.RequestError as e:
                text = f"[API request error: {e}]"
                print(f"API request error for chunk {i} of {file_name}: {e}")

            # Append the transcribed text
            full_text += text + "\n"

            # Add transcribed text to PDF
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text)

    # Save full text to a text file
    with open(f"/home/ninad/Akash/Audios/{file_name}_transcription.txt", "w") as text_file:
        text_file.write(full_text)

    # Save the transcribed text as a PDF file
    pdf_output_path = f"/home/ninad/Akash/Audios/{file_name}_transcription.pdf"
    pdf.output(pdf_output_path)

    print(f"Transcription of {file_name} completed and saved to {pdf_output_path}")
