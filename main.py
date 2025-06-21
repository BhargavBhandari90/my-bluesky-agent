import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from atproto import Client

# Load environment variables
load_dotenv()

# Setup Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# Setup Bluesky
client = Client()
client.login(os.getenv("BLUESKY_HANDLE"), os.getenv("BLUESKY_PASSWORD"))

# Function to post on Bluesky
def post_to_bluesky(message):
    client.send_post(text=message)
    print("✅ Posted to Bluesky:", message)

# Agent logic
def run_agent():
    prompt = """You are a social media bot for Bluesky. Generate a clever or funny post under 300 characters with text at the last like "-- Sent via Bunty's AI Agent..." and respond in this JSON format:

{
  "function_call": {
    "name": "post_to_bluesky",
    "arguments": {
      "message": "Write your witty post here."
    }
  }
}
"""

    response = model.generate_content(prompt)

    try:
        content = response.text.strip()
        if content.startswith("```json"):
            content = content.replace("```json", "").strip()
        if content.endswith("```"):
            content = content[:-3].strip()

        tool_call = json.loads(content)
        message = tool_call["function_call"]["arguments"]["message"]
        post_to_bluesky(message)
    except Exception as e:
        print("⚠️ Error parsing or posting:", e)
        print("Raw response:\n", response.text)

if __name__ == "__main__":
    run_agent()

import schedule
import time

schedule.every().day.at("09:00").do(run_agent)

while True:
    schedule.run_pending()
    time.sleep(60)
