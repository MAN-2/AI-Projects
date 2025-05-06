from bot import chatbot_response

resume_path = "data/test_resumes/sample.pdf"
user_question = "What is my strongest skill?"

response = chatbot_response(user_question, resume_path)
print("Chatbot Response:", response)
