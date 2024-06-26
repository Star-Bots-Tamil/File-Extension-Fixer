from pyrogram import Client, filters
from database.database import db

@Client.on_message(filters.text & filters.private & ~filters.command(['start','help','about','set_prefix','see_prefix','del_prefix','ban','unban','banned','get_mode','stats','restart','broadcast',]))
async def file_extension_fixer(client, message):
    user_text = message.text
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        user_text = f"{prefix} - {user_text}"
    else:
        user_text = f"{user_text}"
    first_60_letters = user_text[:60]
    await client.send_message(message.chat.id, f"`{first_60_letters}.mkv`")
