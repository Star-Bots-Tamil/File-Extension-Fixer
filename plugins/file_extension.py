from pyrogram import Client, filters
from database.database import db

@Client.on_message(filters.text & filters.private & ~filters.command(['start','help','about','set_prefix','see_prefix','del_prefix','ban','unban','banned','get_mode','stats','restart','broadcast',]))
def file_extension_fixer(client, message):
    prefix = await db.get_prefix(message.from_user.id)
    user = message.text
    first_60_letters = user[:60]
    client.send_message(message.chat.id, f"`{first_60_letters}.mkv`")
    
