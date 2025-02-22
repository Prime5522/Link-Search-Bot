from pyrogram import Client, filters  
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton  
from config import Config  
from helpers import search_messages, correct_spelling  

bot = Client("search_bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

# 🎬 Start Command  
@bot.on_message(filters.command("start"))
async def start(client, message):
    buttons = [
        [InlineKeyboardButton("〆 ʜᴇʟᴘ 〆", callback_data="help"),
         InlineKeyboardButton("〆 ᴀʙᴏᴜᴛ 〆", callback_data="about")],
        [InlineKeyboardButton("✧ ᴄʀᴇᴀᴛᴏʀ ✧", url="https://t.me/prime_Nayem")]
    ]
    await message.reply_photo(
        "https://envs.sh/XX.jpg",  # এখানে তোমার স্টার্ট ইমেজ লিংক দাও
        caption="👋 **Welcome!**\n🔍 Just send me a movie name, and I'll fetch it from the channel!",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

# 📜 About Command  
@bot.on_callback_query(filters.regex("about"))
async def about(client, callback_query):
    about_text = """<b>╔════❰ <a href='https://t.me/Prime_Botz'>ʜᴇʀᴇ ɪꜱ ᴍʏ ᴀʙᴏᴜᴛ 🔥</a> ❱═══════❍
║╭━━━━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : @Link_Search_Prime_Bot
║┣⪼👦ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/Prime_Nayem'>ᴍʀ.ᴘʀɪᴍᴇ</a>
║┣⪼❣️ᴜᴘᴅᴀᴛᴇ : <a href=https://t.me/Prime_Botz>ᴘʀɪᴍᴇ ʙᴏᴛᴢ</a>
║┣⪼📡Hᴏsᴛᴇᴅ ᴏɴ : ᴀᴅᴠᴀɴᴄᴇ sᴇʀᴠᴇʀ
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : v2.0 [ᴍᴏsᴛ sᴛᴀʙʟᴇ]
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ </b>"""
    await callback_query.message.edit_text(about_text, disable_web_page_preview=True)

# 🔍 Search System  
@bot.on_message(filters.text & filters.private)
async def search(client, message):
    query = message.text
    words_list = ["example", "movie1", "series"]  # এখানে চ্যানেলের কন্টেন্ট অনুযায়ী শব্দ যোগ করা যাবে  

    corrected_query = correct_spelling(query, words_list)
    if corrected_query != query:
        await message.reply(f"🔎 **Did you mean:** `{corrected_query}` ?", quote=True)

    result = await search_messages(client, corrected_query, Config.CHANNEL_ID)
    if result:
        await result.copy(message.chat.id)
    else:
        await message.reply("❌ **No results found!**", quote=True)

# বট চালু  
bot.run()
