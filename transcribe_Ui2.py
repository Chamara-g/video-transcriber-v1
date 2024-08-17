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
st.title('Video-Transcribing-Ai')

# Layout with two columns
st.markdown("""
    <div class='container'>
        <div class='left-column'>
            <h3 style='margin: 60px 0 1px 0;'>Model Details</h3>
            <ul>
                <li>Model ID: whisper-large-v3</li>
                <li>Developer: OpenAI</li>
                <li>File Size: 25 MB(Max)</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

# Initialize transcription result and selected option in session state if not already present
if 'transcription_result' not in st.session_state:
    st.session_state.transcription_result = None
if 'last_option' not in st.session_state:
    st.session_state.last_option = None

# Radio button for choosing input method
transcription_option = st.radio("Choose your input method:", ("URL", "Upload a file"))

# Reset transcription result if the selected radio option changes
if transcription_option != st.session_state.last_option:
    st.session_state.transcription_result = None
    st.session_state.last_option = transcription_option

video_url = None
uploaded_file = None

if transcription_option == "URL":
    video_url = st.text_input("Enter the video URL:", '', key="video_url")
elif transcription_option == "Upload a file":
    uploaded_file = st.file_uploader("Upload a local file", type=["mp4", "mp3", "wav", "m4a"])

def transcribing():
    if video_url:
        st.session_state.transcription_result = main(video_url, is_url=True)
        st.success('Successfully transcribed your file from the URL!')
    elif uploaded_file:
        
        # Save the uploaded file to a temporary location
        temp_file_path = f"./temp_{uploaded_file.name}"
        
        with open(temp_file_path, "wb") as temp_file:
            temp_file.write(uploaded_file.getvalue())
        
        st.session_state.transcription_result = main(temp_file_path, is_url=False)
        st.success('Successfully transcribed your file from the uploaded file!')
    else:
        st.error('Please provide a valid URL or upload a file.')

# Button to start transcription
if st.button('Start Transcription'):
    transcribing()

# Display transcription result if available
if st.session_state.transcription_result:
    st.markdown("### Transcription Result:")
    st.text_area("Transcription:", st.session_state.transcription_result, height=200)

    # Option to download as text file
    st.download_button(
        label="Download as Text",
        data=st.session_state.transcription_result,
        file_name="transcription.txt",
        mime="text/plain"
    )

    # Option to download as CSV file
    df = pd.DataFrame([{"Transcription": st.session_state.transcription_result}])
    st.download_button(
        label="Download as CSV",
        data=df.to_csv(index=False),
        file_name="transcription.csv",
        mime="text/csv"
    )

st.markdown("</div></div>", unsafe_allow_html=True)
