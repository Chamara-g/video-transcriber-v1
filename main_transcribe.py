import os
import time
from config import cfg
from transcribe_audio import transcribe_audio
from download_audio import download_audio, extract_user_id

def main(input_source, is_url):
    start_time = time.time()  # Record start time
    output_dir = cfg.app.output_path
    
    #print("is_url=True:",is_url)
    # Handle URL input
    if is_url:
        print("Video URL:", input_source)
        final_string = extract_user_id(input_source)
        audio_filename = download_audio(input_source, output_dir, final_string)
        
    # Handle file upload input
    else:
        # Assume input_source is the file path
        audio_filename = input_source
        print("audio_filename:", audio_filename)
        final_string = os.path.splitext(os.path.basename(audio_filename))[0]  # Use the filename without extension as ID
    '''  
    # Step 2: Check if the audio file exists
    if not os.path.exists(audio_filename):
        print(f"Error: The file {audio_filename} does not exist.")
        return None  # Return None if the file doesn't exist
    '''
    # Step 3: Transcribe the downloaded or uploaded audio
    api_key = cfg.groq_api_key
    audio_file=open(audio_filename, "rb")

    transcription_text = transcribe_audio(audio_file, api_key)

    end_time = time.time()  # Record end time
    print(f"Total execution time: {end_time - start_time:.2f} seconds")  # Print total execution time

    return transcription_text  # Return the transcription result

if __name__ == "__main__":
    main()
