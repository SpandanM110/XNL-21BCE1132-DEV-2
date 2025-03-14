import os
import google.generativeai as genai

# Configure Gemini AI
genai.configure(api_key=os.environ["AIzaSyDQzZQFNUjYgxTBtWluA23sOzw_BgfyXY0"])

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-8b",
    system_instruction="Optimize SQL queries for performance."
)

def optimize_query(sql_query):
    """
    Sends an SQL query to Gemini AI for optimization suggestions.
    """
    chat_session = model.start_chat()
    response = chat_session.send_message(f"Optimize this SQL query: {sql_query}")
    
    return response.text

if __name__ == "__main__":
    sample_query = "SELECT * FROM users WHERE created_at > NOW() - INTERVAL '7 days'"
    optimized_query = optimize_query(sample_query)
    print("Optimized Query:", optimized_query)
