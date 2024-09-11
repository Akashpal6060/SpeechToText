import os
from pydub import AudioSegment

# Folder path containing the audio files
folder_path = "D:/git_tutorial/SpeechToText/Audio_Files"

# Extract all .wav files from the folder
audio_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".wav")]

# Iterate over each audio file
for audio_file in audio_files:
    # Extract file name without extension for folder naming
    file_name = os.path.splitext(os.path.basename(audio_file))[0]

    # Create an output folder for the audio chunks
    output_folder = f"D:/git_tutorial/SpeechToText/AudioChunks/{file_name}_chunks"
    os.makedirs(output_folder, exist_ok=True)

    # Load the audio file
    audio = AudioSegment.from_wav(audio_file)

    # Split audio into 1-minute chunks
    chunk_length_ms = 600000  # 10 minute in milliseconds
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]


    # Export each chunk
    for i, chunk in enumerate(chunks):
        chunk_name = os.path.join(output_folder, f"chunk{i}.wav")
        chunk.export(chunk_name, format="wav")

    print(f"Chunks for {file_name} created successfully in {output_folder}")
