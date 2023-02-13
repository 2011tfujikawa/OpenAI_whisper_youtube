import streamlit as st
import datetime
import whisper
import youtube_dl
import os
from IPython.display import HTML
from base64 import b64encode

# https://www.youtube.com/watch?v=9zuMSYjxUlk
# youtube_url="https://www.youtube.com/watch?v=svopKK8YoRc"
outputfile=r'/a.mp3'
dir_path = os.path.dirname(os.path.realpath(__file__))+outputfile
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


youtube_url = st.text_input("Youtube video or playlist URL")

if st.button('実行'):
    source = youtube_url
    print(source)

#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        info = ydl.extract_info(source, download=True)
#        filename = ydl.prepare_filename(info)
#        print(info)
#        print("----")        
#        print(filename) 
#        outputfile=filename.split(".")[0]+str(".mp3")

    print(dir_path+outputfile)
#    audio_file= open(r"H:\マイドライブ\python\streamlit\whisper_simple\a.mp3",'rb')
    audio_file= open(dir_path+outputfile,'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

    st.write('再実行')
#else:
#    st.write('むむむ')
    


#H:\マイドライブ\python\streamlit\whisper_simple