import os  

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "7968513647:AAHhDKQ0EgxoOIGj43GIndNFPNDYaCzSAsQ")
    API_ID = int(os.getenv("API_ID", "27148454"))
    API_HASH = os.getenv("API_HASH", "f668c20d77d1a8feee31afdc810f8ac4")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1002011482617"))  # চ্যানেল আইডি দিন
