from pyrogram import Client, filters

@Client.on_message(filters.text & filters.private & ~filters.command(['start','help','about','showthumbnail','deletethumbnail','set_caption','get_caption','del_caption','change_mode','get_mode','stats','restart','broadcast',]))
def send_text(client, message):
    user = message.text
    first_60_letters = user[:60]
    client.send_message(message.chat.id, f"`{first_60_letters}.mkv`")
    
