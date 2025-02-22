from pyrogram.errors import MessageNotModified
import difflib  

# স্পেল চেক ফাংশন  
def correct_spelling(query, words_list):
    matches = difflib.get_close_matches(query, words_list, n=1, cutoff=0.7)
    return matches[0] if matches else query  

# চ্যানেল থেকে পোস্ট খোঁজা  
async def search_messages(client, query, channel_id):
    async for message in client.search_messages(channel_id, query):
        if message.text or message.caption:
            return message  
    return None
