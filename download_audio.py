import os
import yt_dlp
from config import cfg  # Import the entire config object
import time

def extract_user_id(video_url):
        
    from urllib.parse import urlparse

    parsed_url = urlparse(video_url)
    start = video_url.find("www.") + len("www.")
    end = video_url.find(".", start)
    substring_1 = video_url[start:end]
    substring_2 = video_url[-5:]

    if substring_1 == "tiktok":
        path = parsed_url.path
        substring_2 = path[-5:] if len(path) >= 5 else ''
    final_string = f"{substring_1}_{substring_2}"
    return final_string

def download_audio(url, output_dir,final_string):
    try:
        start_time = time.time()

        # Ensure the output directory exists
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print("final_string",final_string)

        output_path = os.path.join(output_dir, f"{final_string}.mp3")

        print("output_path",output_path)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        download_time = time.time() - start_time
        print(f"Audio downloaded and saved to {output_path}")
        print(f"Downloading time: {download_time:.2f} seconds")
        return output_path
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None

