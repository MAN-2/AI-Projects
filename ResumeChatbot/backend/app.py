import streamlit as st
st.set_page_config(page_title="AI Resume Chatbot", layout="centered")
import tempfile
from bot import chatbot_response
from parser import extract_text_from_pdf
import google.generativeai as genai


st.title("AI Resume Chatbot          (Powered by Gemini)")
st.subheader("Upload a resume and ask questions!")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  

if "user_query" not in st.session_state:
    st.session_state.user_query = ""

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"], key="resume_upload")
user_query = st.text_input("Enter your question", value=st.session_state.user_query, key="user_input")

# Chatbot Interaction
if uploaded_file and user_query:
    try:
        
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name

    
        reply = chatbot_response(user_query, temp_path)

        
        st.session_state.chat_history.append({"Question": user_query, "Response": reply})

        #  answer
        st.success(reply)

        
        st.session_state.user_query = ""

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Rate My Resume 
if uploaded_file and st.button("Rate My Resume", key="rate_resume"):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name
        resume_text = extract_text_from_pdf(temp_path)
        analysis_prompt = f"""
        Summarize key skills in this resume.
        Identify the strongest skill and provide a brief explanation.       
        Provide free resources to enhance career growth.
        Analyze this resume for ATS compatibility and provide an estimated score (0-100).
        Highlight missing keywords that could improve ATS ranking.
        Suggest specific skill improvements and learning resources.
        Recommend job roles aligned with this resume.

        Resume:
        {resume_text}
        """

        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        analysis_response = model.generate_content(analysis_prompt)

        st.subheader("Resume Analysis")
        st.write(analysis_response.text)

    except Exception as e:
        st.error(f"Error analyzing resume: {str(e)}")
