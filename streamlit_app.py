import streamlit as st
import pandas as pd
import numpy as np
import yt_dlp

st.title("Youtube to mp3 converter")

st.text("Drop a youtube link below and voila")

link = st.text_input("Youtube link")

def download_video_as_mp3(url, bitrate='192k'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate,
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

for videoid in videoids:
    download_video_as_mp3(f'link')
