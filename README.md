# My Bluesky AI Posting Agent

[![Run Daily AI Agent](https://github.com/BhargavBhandari90/my-bluesky-agent/actions/workflows/daily-agent.yml/badge.svg?branch=main)](https://github.com/BhargavBhandari90/my-bluesky-agent/actions/workflows/daily-agent.yml)

This agent uses Google's Gemini to generate posts and publishes them to Bluesky.

## Setup

1. Create a `.env` file: and add following details

```
GEMINI_API_KEY=your_gemini_key
BLUESKY_HANDLE=your_handle.bsky.social
BLUESKY_PASSWORD=your_app_password
```

2. Install dependencies:

    `pip install -r requirements.txt`

3. Run the agent:

    `python main.py`
