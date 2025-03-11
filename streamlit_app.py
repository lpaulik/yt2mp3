import streamlit as st
import pandas as pd
import numpy as np
import yt_dlp
import os
from pathlib import Path

st.title("Youtube to mp3 converter")

st.text("Drop a youtube link below and voila")

link = st.text_input("Youtube link")

def download_video_as_mp3(url):
    # Get the path to the user's Downloads folder
    downloads_path = str(Path.home() / "Downloads")

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': os.path.join(downloads_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192k',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if link:
    if st.button("Download as MP3"):
        download_video_as_mp3(link)
        st.success("Download started!")


#https://www.youtube.com/watch?v=VEfMAsFBMC8