import os  

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    API_ID = int(os.getenv("API_ID", "YOUR_API_ID_HERE"))
    API_HASH = os.getenv("API_HASH", "YOUR_API_HASH_HERE")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-100XXXXXXXXX"))  # চ্যানেল আইডি দিন
