from parser import extract_text_from_pdf
from api import query_gemini

def chatbot_response(user_query, resume_path):
    """Uses resume data to generate a chatbot answer."""
    resume_text = extract_text_from_pdf(resume_path)
    reply = query_gemini(user_query, resume_text)
    return reply
import streamlit as st
import tempfile
from bot import chatbot_response

st.title("AI Resume Chatbot (Powered by Gemini)")
st.subheader("Ask questions about your resume!")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
user_query = st.text_input("Enter your question")

if uploaded_file and user_query:
    
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_path = temp_file.name

   
    reply = chatbot_response(user_query, temp_path)

    
    st.success(reply)
