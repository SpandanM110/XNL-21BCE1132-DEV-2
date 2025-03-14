import os
import google.generativeai as genai
import json
import requests

# Configure Gemini AI
genai.configure(api_key=os.environ["AIzaSyDQzZQFNUjYgxTBtWluA23sOzw_BgfyXY0"])

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    system_instruction="Detect unusual API usage patterns and flag potential threats."
)

def detect_anomalies(api_logs):
    """
    Sends API logs to Gemini AI for anomaly detection.
    """
    chat_session = model.start_chat()
    response = chat_session.send_message(f"Analyze the following API logs for anomalies: {json.dumps(api_logs)}")
    
    return response.text

if __name__ == "__main__":
    # Example log data
    sample_logs = [
        {"user": "user123", "endpoint": "/login", "requests": 5000, "status_code": 200},
        {"user": "user456", "endpoint": "/data", "requests": 3, "status_code": 403},
    ]
    
    result = detect_anomalies(sample_logs)
    print("Anomaly Detection Result:", result)
