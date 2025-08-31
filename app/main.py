import streamlit as st

st.title("Email Generator")
url_input = st.text_input("Enter a URL:", value="https://devjobs.lk/dev-jobs/client/ads/257")
submit_button = st.button("Generate Email")

if submit_button:
    st.code("Hello, Hiring Manage, I am from InnovD", language="markdown")