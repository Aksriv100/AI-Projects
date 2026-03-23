import streamlit as st
from openai import OpenAI
import os
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Resume Analyzer")

resume_text = st.text_area("Paste your resume here")

if st.button("Analyze"):
    prompt = f"""
    Analyze this resume and provide:
    - Strengths
    - Weaknesses
    - Suggestions
    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert HR."},
            {"role": "user", "content": prompt}
        ]
    )

    st.write(response.choices[0].message.content)
