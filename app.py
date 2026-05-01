import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Biology Chapter 2", layout="wide")

st.title("📘 Biology Chapter 2")

FILE_NAME = "bio.ch.2"

try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Render HTML inside Streamlit
    components.html(html_content, height=800, scrolling=True)

except FileNotFoundError:
    st.error(f"File '{FILE_NAME}' not found.")
    st.info("Make sure the HTML file is in the same repo as app.py.")
