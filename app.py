import streamlit as st
import requests

# API URL (Make sure FastAPI is running)
API_URL = "http://127.0.0.1:8000/chat"

st.title("🤖 Cypher - Your AI Assistant")

# User input field
user_input = st.text_input("Enter your message:")

# When user clicks "Send"
if st.button("Send"):
    if user_input:
        response = requests.get(API_URL, params={"query": user_input})
        chatbot_response = response.json().get("response", "No response")
        st.text_area("Chatbot says:", chatbot_response, height=100)
    else:
        st.warning("Please enter a message before sending.")
