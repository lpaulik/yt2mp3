import streamlit as st
import pandas as pd
import numpy as np
import yt_dlp
import os

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

if link:
    if st.button("Convert to mp3"):
        with st.spinner('Converting...'):
            download_video_as_mp3(link)
        st.success("File converted")

        info_dict = yt_dlp.YoutubeDL.extract_info(link, download=False)
        video_title = info_dict.get('title', None)
        filename = f"{video_title}.mp3"
        os.rename(f"{link.split('=')[-1]}.mp3", filename)

        st.download_button(
            label="Download mp3",
            data=open(filename, "rb").read(),
            file_name=filename,
            mime="audio/mpeg"
        )

        os.remove(f"{link.split('=')[-1]}.mp3")


#https://www.youtube.com/watch?v=VEfMAsFBMC8