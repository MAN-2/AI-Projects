import google.generativeai as genai

API_KEY = "AIzaSyA6eeED-xGp49mivzb1v22qOMxzfIG07fU"
genai.configure(api_key=API_KEY)

def query_gemini(question, resume_text):
    """Generates responses intelligently based on resume content."""
    prompt = f"""
    Act as a professional AI career assistant. Here is a candidate's resume:

    {resume_text}

    Answer the following question in a way that reflects the candidate’s skills, experience, and aspirations:

    {question}
    """

    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    truncated_response = response.text[:350]
    if " " in truncated_response:
     truncated_response = truncated_response.rsplit(' ', 1)[0]  

    
    return truncated_response
