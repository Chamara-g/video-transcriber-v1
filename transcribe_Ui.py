import streamlit as st
import pandas as pd
from main_transcribe import main
from transcribe_audio import transcribe_audio  # Import your modified function
import os

# Function to load CSS from a file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file
css_file_path = 'styles.css'  # Adjust this path if you placed the file in a different location
load_css(css_file_path)

# Header
#st.markdown("<div class='header'><h2>Transcribing-Ai</h2></div>", unsafe_allow_html=True)


# Layout with two columns
st.markdown("""
    <div class='container'>
        <div class='left-column'>
            <h3>Model Details</h2>
            <li>Model ID: whisper-large-v3</li>
            <li>Developer: OpenAI</li>
            <li>File Size: 25 MB</li>
        </div>
    </div>
""", unsafe_allow_html=True)

# Streamlit interface
transcription_option = st.radio("Choose your input method:", ("URL", "Upload a file"))

video_url = None
uploaded_file = None

if transcription_option == "URL":
    video_url = st.text_input("Enter the video URL:", '', key="video_url")
elif transcription_option == "Upload a file":
    uploaded_file = st.file_uploader("Upload a local file", type=["mp4", "mp3", "wav", "m4a"])

def transcribing():
    transcription_result = None
    
    if video_url:
        transcription_result = main(video_url, is_url=True)
        st.success('Successfully transcript your file from the URL !')
    elif uploaded_file:
        # Save the uploaded file to a temporary location
        temp_file_path = f"./temp_{uploaded_file.name}"
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.getvalue())
        transcription_result = main(temp_file_path, is_url=False)
        st.success('Successfully transcript your file ,from the uploaded file!')
    else:
        st.error('Please provide a valid URL or upload a file.')

    # Display transcription result in UI
    if transcription_result:
        st.markdown("### Transcription Result:")
        st.text_area("Transcription:", transcription_result, height=200)

        # Option to download as text file
        st.download_button(
            label="Download as Text",
            data=transcription_result,
            file_name="transcription.txt",
            mime="text/plain"
        )

        # Option to download as CSV file
        df = pd.DataFrame([{"Transcription": transcription_result}])
        st.download_button(
            label="Download as CSV",
            data=df.to_csv(index=False),
            file_name="transcription.csv",
            mime="text/csv"
        )

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.button('Start Transcription', on_click=transcribing)
st.markdown("</div>", unsafe_allow_html=True)
