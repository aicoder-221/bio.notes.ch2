import streamlit as st

st.set_page_config(page_title="Biology Chapter 2 Notes", layout="wide")

st.title("📘 Biology Chapter 2 Notes")

# Try reading the file from repo
FILE_NAME = "bio.ch.2"

try:
    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read()

    st.markdown(content)

except FileNotFoundError:
    st.error(f"File '{FILE_NAME}' not found in the repository.")
    st.info("Make sure 'bio.ch.2' is uploaded in the same repo folder as app.py.")
