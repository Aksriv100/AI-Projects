
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")
py
st.title("AI Chatbot")

user_input = st.text_input("You:")

if st.button("Send"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    st.write("Bot:", response.choices[0].message.content)
