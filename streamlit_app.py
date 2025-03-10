import streamlit as st
import pandas as pd
import numpy as np
import yt_dlp

st.title("Youtube to mp3 converter")

st.text("Drop a youtube link below and voila")

link = st.text_input("Youtube link")

def download_video_as_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192k',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

mp3=download_video_as_mp3(f'link')

st.download_button(
    file_name="test.mp3"
    data=mp3
)
