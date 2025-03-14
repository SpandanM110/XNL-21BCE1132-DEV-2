import os
import google.generativeai as genai
import json

# Configure Gemini AI
genai.configure(api_key=os.environ["AIzaSyDQzZQFNUjYgxTBtWluA23sOzw_BgfyXY0"])

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    system_instruction="Adjust load balancing rules based on traffic patterns."
)

def tune_load_balancer(traffic_data):
    """
    AI-powered analysis of real-time traffic for auto-scaling.
    """
    chat_session = model.start_chat()
    response = chat_session.send_message(f"Analyze and auto-tune load balancer: {json.dumps(traffic_data)}")
    
    return response.text

if __name__ == "__main__":
    sample_traffic = [
        {"region": "US-East", "requests": 250000, "latency": "45ms"},
        {"region": "Europe", "requests": 150000, "latency": "40ms"},
    ]
    
    scaling_decision = tune_load_balancer(sample_traffic)
    print("Scaling Decision:", scaling_decision)
