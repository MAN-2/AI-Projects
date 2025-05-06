
# **AI Resume Chatbot (Powered by Gemini AI)**

## 📌 Project Overview
The **AI Resume Chatbot** is an intelligent career assistant designed to answer questions about a user's resume, analyze its strengths, provide improvement suggestions, and rate its ATS compatibility. 

## 🚀 Features
- **Smart Resume Q&A** – Answers user queries based on uploaded resumes.
- **ATS Score Evaluation** – Suggests improvements for better job application success.
- **Skill Enhancement Recommendations** – Provides resources to improve relevant skills.
- **Career Path Suggestions** – Recommends job roles aligned with resume data.

## Snapshots
![Screenshot (424)](https://github.com/user-attachments/assets/78de01ac-e8dd-416e-af13-12c4ad3b3afd)
![Screenshot (425)](https://github.com/user-attachments/assets/a8052895-59b1-4687-8e71-d370f992ea7e)
![Screenshot (423)](https://github.com/user-attachments/assets/e0a230e8-d115-4b33-80db-0e291c84618e)


## 🛠️ Installation & Usage
### **1 Clone Repository**
```bash
git clone https://github.com/MAN-2/AI-Projects.git
cd AI-Projects/ResumeChatbot
```
### **2 Install Requirements**

Ensure all required packages are installed:
```bash
pip install -r requirements.txt
```

### **3 Running the Chatbot**
```bash
streamlit run ResumeChatbot/backend/app.py
````

## 🔮 Future Scope & Enhancements
### **🔊 Voice Functionality**
Currently, the chatbot operates via text. A future upgrade could integrate **voice-based interaction**, allowing users to:
- **Ask resume-related questions via speech** instead of typing.
- **Receive spoken responses** using a text-to-speech engine.
- **Streamline accessibility** for users who prefer voice-based career assistance.

Libraries like **SpeechRecognition** and **pyttsx3** can be incorporated for voice interaction.

##Known Error :: Can sometimes run duplicate instances of Streamlit UI and present multiple dialogs on first deployment . 
 ### Administered fix: Refresh the Browser
