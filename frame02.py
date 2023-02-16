import streamlit as st
import whisper
import os
import youtube_dl
from IPython.display import HTML
from base64 import b64encode

source="https://www.youtube.com/watch?v=svopKK8YoRc"
outputfile=r'./audio_file.mp3'

youtube_url = st.text_input("Youtube video or playlist URL",source)
selected_item = st.selectbox('data model:base(74M),small(244M),medium(769M)',
     ['base', 'small','medium'])

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  "audio_file" + '.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

if st.button('YouTubeからのダウンロード'):
    st.video(youtube_url)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        data_load_state = st.text('Downloading...'+str(youtube_url))
        info = ydl.extract_info(youtube_url, download=True)
        filename = ydl.prepare_filename(info)

        try:
          outputfile=filename.replace('webm', 'mp3')
        except FileNotFoundError as FNF:
          outputfile=filename.replace('m4a', 'mp3')
        except Exception as e:
          print("正しく動画がダウンロードできなかったようです。")
        data_load_state = st.text('Downloag DONE...'+str(youtube_url))

    audio_file= open(os.path.abspath(outputfile),'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

if st.button('文字書き起こし'):
    st.audio(audio_bytes, format='audio/ogg') 
    data_load_state = st.text('Loading data model...'+str(selected_item))
    model = whisper.load_model(selected_item)
    data_load_state.text('Loading data model...done!'+str(selected_item))

    result = model.transcribe(os.path.abspath(outputfile), verbose=True)

# セグメントごとに表示
    for seg in result["segments"]:
        id, start, end, text = [seg[key] for key in ["id", "start", "end", "text"]]
        print(f"{id:03}: {start:5.1f} - {end:5.1f} | {text}")
        st.write(f"{id:03}: {start:5.1f} - {end:5.1f} | {text}")
        
    st.write(result["text"])

