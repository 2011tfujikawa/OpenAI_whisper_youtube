import streamlit as st
import whisper
import os
from IPython.display import HTML
from base64 import b64encode

path="./"
files = os.listdir(path)
print(files)

st.video('https://www.youtube.com/watch?v=svopKK8YoRc')
outputfile=r'./audio_file.mp3'
print(os.path.abspath(outputfile))

selected_item = st.selectbox('data model:base(74M),small(244M),medium(769M)',
     ['base', 'small','medium'])

if st.button('実行'):
    print(os.path.abspath(outputfile))
    print("----")       
    print(selected_item)

    audio_file= open(os.path.abspath(outputfile),'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/ogg')

    data_load_state = st.text('Loading data model...'+str(selected_item))
    model = whisper.load_model(selected_item)
    data_load_state.text('Loading data model...done!'+str(selected_item))

    result = model.transcribe(os.path.abspath(outputfile), verbose=True)
    print(result["text"])
# セグメントごとに表示
    for seg in result["segments"]:
        id, start, end, text = [seg[key] for key in ["id", "start", "end", "text"]]
        print(f"{id:03}: {start:5.1f} - {end:5.1f} | {text}")
        st.write(f"{id:03}: {start:5.1f} - {end:5.1f} | {text}")
        
    st.write(result["text"])

