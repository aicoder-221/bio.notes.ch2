import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Biology Chapter 2", layout="wide")

st.title("📘 Biology Chapter 2")

FILE_NAME = "bio_ch_2.html"  # make sure this matches GitHub exactly

try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        html_content = file.read()

    components.html(html_content, height=800, scrolling=True)

except FileNotFoundError:
    st.error("File not found. Check filename in GitHub repo.")
