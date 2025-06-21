# My Bluesky AI Posting Agent

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
