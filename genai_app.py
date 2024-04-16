from openai import OpenAI
import streamlit as st
f = open("keys\open_ai.txt")
key = f.read()
client = OpenAI(api_key=key)
st.title("Gen App->AI Code Reviewer 🤖")
prompt = st.text_area("Enter code here:")
if st.button("Generate 👨‍💻")==True:
    st.balloons()
    response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                {"role": "system", "content": """You are a code debugging assistant. Your task is to help developers identify and fix errors in the prompt. Given a code snippet,
                                                     provide a helpful message about the error and suggest the corrected code. 🛠️"""}, 
                {"role": "user", "content": prompt}
                ]
    )
    st.write("Results:")
    st.write(response.choices[0].message.content)