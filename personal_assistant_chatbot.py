import requests
import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
HUGGINGFACE_API_KEY = "your_api_key"

# Hugging Face Model
MODEL = "mistralai/Mistral-7B-Instruct-v0.3" 
#"mistralai/Mistral-7B-Instruct-v0.2"
#"HuggingFaceH4/zephyr-7b-alpha"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

# Initialize FastAPI app
app = FastAPI()

def get_ai_response(user_input: str) -> str:
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
    
    payload = {
        "inputs": f"User: {user_input}\n Cypher - an AI Assistant (Respond in one sentence):",
        "parameters": {
            "max_new_tokens": 200,  # Limits response length
            "temperature": 0.2,  # Reduces randomness
            "top_p": 0.8,  # Ensures focus on relevant words
            "do_sample": False,  # Prevents unnecessary creativity
            "repetition_penalty": 1.2,  # Reduces repetition
            "return_full_text": False,  # Only return AI response
        }
        
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"Error: {response.text}"


CHATBOT_NAME = "Cypher"

@app.get("/chat")
def chat(query: str):
    """API endpoint to get chatbot response."""
    ai_response = get_ai_response(query)
    return {"chatbot_name": CHATBOT_NAME, "response": ai_response}

# Run the server using: uvicorn personal_assistant_chatbot:app --reload