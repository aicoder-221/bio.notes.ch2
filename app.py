import streamlit as st
import streamlit.components.v1 as components
import os

st.title("📘 Biology Chapter 2")

st.write("Files in repo:", os.listdir())

FILE_NAME = "bio_ch_2.html"

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        html_content = file.read()

    components.html(html_content, height=800, scrolling=True)
else:
    st.error("File not found!")
