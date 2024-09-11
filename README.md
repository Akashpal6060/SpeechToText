# Speech to Text Application

This application processes audio files in `.wav` format and converts them to text. The transcribed text is saved in a PDF and text file format.

## Requirements

Before running the script, make sure to install the necessary dependencies.

### Audio Format Requirement
- The input audio files must be in `.wav` format.
- Place your `.wav` files in the `Audio_Files` folder.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Akashpal6060/SpeechToText.git

# Folder Structure

2. Folder Structure

# SpeechToText/
- │
- ├── Audio_Files/       # Folder to upload .wav audio files
- ├── AudioChunks/       # Temporary folder where audio chunks are saved (generated during processing)
- ├── Output_files/      # Output folder where transcriptions are saved
- ├── Main.py            # Main script to run the application
- ├── requirements.txt   # List of required dependencies
- └── README.md          # This file



3. Install the Required Dependencies

  ```bash
   pip install -r requirements.txt

4. Place Your Audio Files
Put all your .wav files inside the Audio_Files folder located in the project directory.

5. Running the Application
 
  ```bash
   python Main.py

6. The script will:
    - Process each .wav file in the Audio_Files directory.
    - Split the audio into chunks (for more efficient processing).
    - Convert the audio chunks into text.
    - Save the transcribed text in two formats: .txt and .pdf.

7. Output
    The transcribed text files and PDFs will be saved in the Output_files folder.
    Each audio file will have its own corresponding .txt and .pdf files, named based on the original audio file.

## Example
 - If you have a file named example.wav in the Audio_Files folder, the following files will be generated after processing:

    - Output_files/example_transcription.txt
    - Output_files/example_transcription.pdf

### Note
    The process may take a few minutes depending on the size and duration of the audio files. Please be patient while the application runs.