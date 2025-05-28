import streamlit as st

st.title("🚀 Hello Streamlit App")

name = st.text_input("What's your name?")
if name:
    st.write(f"Welcome, {name}!")
