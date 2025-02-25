import streamlit as st
import openai
import os

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI Assistant")

user_input = st.text_input("Enter your prompt:")

if user_input:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message.content.strip())
