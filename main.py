import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from atproto import Client

# Load environment variables
load_dotenv()

# Setup Bluesky
client = Client()
client.login(os.getenv("BLUESKY_HANDLE"), os.getenv("BLUESKY_PASSWORD"))

# Function to post on Bluesky
def post_to_bluesky(message):
    client.send_post(text=message)
    print("✅ Posted to Bluesky:", message)

# Agent logic
def run_agent():
    message = 'Good Morning WordPress people... ' \
    '-- Sent by Bunty\'s AI agent';
    post_to_bluesky(message)

if __name__ == "__main__":
    run_agent()


# Removed from here and user GITHUB cron.

# import schedule
# import time

# print("🕒 Current system time:", time.strftime("%Y-%m-%d %H:%M:%S"))

# schedule.every().day.at("10:30").do(run_agent)
# # schedule.every(1).minutes.do(run_agent)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
