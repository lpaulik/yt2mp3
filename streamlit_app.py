import streamlit as st
import pandas as pd
import numpy as np
import yt_dlp
import os

st.title("Youtube to mp3 converter")

st.text("Drop a youtube link below and voila")

link = st.text_input("Youtube link", value=None, key="link")

def clear_link():
    st.session_state.link = ""

def download_video_as_mp3(url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192k',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if link:
        
        ytp = yt_dlp.YoutubeDL()
        info_dict = ytp.extract_info(url=link, download=False)
        video_title = info_dict.get('title', None)
        filename = f"{video_title}.mp3"
        
        st.text(filename)
        
        with st.spinner('Converting...'):
            download_video_as_mp3(link)
        st.success("File converted")

        st.download_button(
            label="Download mp3",
            data=open(filename, "rb").read(),
            file_name=filename,
            mime="audio/mpeg",
            icon=":material/download_for_offline:",
            on_click=clear_link
        )

        os.remove(filename)


#https://www.youtube.com/watch?v=ymgIkOXp6Ds