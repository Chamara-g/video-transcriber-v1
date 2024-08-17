'''
import os
import csv
from groq import Groq

def transcribe_audio(audio_filename, output_dir,final_string,api_key):


    client = Groq(api_key=api_key) 

    #print(client) 
    # Transcribe the audio file
    print("audio_filename:",audio_filename)
    with open(audio_filename, "rb") as file:
        translation = client.audio.translations.create(
            file=(audio_filename, file.read()),
            model="whisper-large-v3",
            prompt="Specify context or spelling",  # Optional
            response_format="json",  # Optional
            temperature=0.0  # Optional
        )
        transcription_text = translation.text

    # Save transcription to a TXT file
    txt_file_path = os.path.join(output_dir, f"{final_string}_trans.txt")
    print("txt_file_path",txt_file_path)
    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(transcription_text)

    # Save transcription to a CSV file
    csv_file_path = os.path.join(output_dir, f"{final_string}_trans.csv")
    with open(csv_file_path, "w", encoding="utf-8", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Transcription"])
        csv_writer.writerow([transcription_text])

    print(f"Transcription saved to {txt_file_path}")

'''
'''
import os
import csv
from groq import Groq

def transcribe_audio(audio_file, output_dir, final_string, api_key):
    client = Groq(api_key=api_key) 

    # Transcribe the audio file
    #print("audio_filename:", audio_filename)
    translation = client.audio.translations.create(
        file=audio_file,  # Pass the filename directly
        model="whisper-large-v3",
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        temperature=0.0  # Optional
    )
    transcription_text = translation.text

    # Save transcription to a TXT file
    txt_file_path = os.path.join(output_dir, f"{final_string}_trans.txt")
    print("txt_file_path", txt_file_path)
    with open(txt_file_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(transcription_text)

    # Save transcription to a CSV file
    csv_file_path = os.path.join(output_dir, f"{final_string}_trans.csv")
    with open(csv_file_path, "w", encoding="utf-8", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Transcription"])
        csv_writer.writerow([transcription_text])

    print(f"Transcription saved to {txt_file_path}")
'''
import os
from groq import Groq

def transcribe_audio(audio_file, api_key):
    client = Groq(api_key=api_key) 
    '''
    # Transcribe the audio file
    translation = client.audio.translations.create(
        #file=open(audio_file_path, "rb"),  # Open the file in binary mode
        model="whisper-large-v3",
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        temperature=0.0  # Optional
    )
    '''
    translation = client.audio.translations.create(
        file=audio_file,  # Pass the filename directly
        model="whisper-large-v3",
        prompt="Specify context or spelling",  # Optional
        response_format="json",  # Optional
        temperature=0.0  # Optional
    )
    transcription_text = translation.text

    # Return the transcription text so it can be displayed on the UI
    return transcription_text


