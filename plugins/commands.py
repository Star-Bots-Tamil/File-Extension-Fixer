import random
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from database.database import db
from config import Config, Text  
  
@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message)                
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🧑🏻‍💻 Developer", callback_data='dev')
        ],[
        InlineKeyboardButton('🤖 Update Channel', url='https://t.me/Star_Bots_Tamil'),
        InlineKeyboardButton('👥 Support Group', url='https://t.me/Star_Bots_Tamil_Support')
        #],[
        #InlineKeyboardButton('⚙️ Settings', callback_data='showSettings')
        ],[
        InlineKeyboardButton('🎛️ About', callback_data='about'),
        InlineKeyboardButton('🛠️ Help', callback_data='help')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
    ]])
    if Config.PIC:
        await message.reply_photo(Config.PIC, caption=Text.START_TEXT.format(user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Text.START_TEXT.format(user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("help"))
async def help(client, message):
    user = message.from_user
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🧑🏻‍💻 Developer", callback_data='dev')
        ],[
        InlineKeyboardButton('🤖 Update Channel', url='https://t.me/Star_Bots_Tamil'),
        InlineKeyboardButton('👥 Support Group', url='https://t.me/Star_Bots_Tamil_Support')
        ],[
        InlineKeyboardButton('🎛️ About', callback_data='about'),
        InlineKeyboardButton('🏠 Home', callback_data='start')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
    ]])
    if Config.PIC:
        await message.reply_photo(Config.PIC, caption=Text.HELP_TEXT.format(user.mention), parse_mode=enums.ParseMode.MARKDOWN, reply_markup=button)       
    else:
        await message.reply_text(text=Text.HELP_TEXT.format(user.mention), reply_markup=button, parse_mode=enums.ParseMode.MARKDOWN, disable_web_page_preview=True)

@Client.on_message(filters.private & filters.command("about"))
async def about(client, message):
    user = message.from_user
    button = InlineKeyboardMarkup([[
        InlineKeyboardButton("🧑🏻‍💻 Developer", callback_data='dev')
        ],[
        InlineKeyboardButton('🤖 Update Channel', url='https://t.me/Star_Bots_Tamil'),
        InlineKeyboardButton('👥 Support Group', url='https://t.me/Star_Bots_Tamil_Support')
        ],[
        InlineKeyboardButton('🛠️ Help', callback_data='help'),
        InlineKeyboardButton('🏠 Home', callback_data='start')
        ],[
        InlineKeyboardButton('🔒 Close', callback_data='close')
    ]])
    if Config.PIC:
        await message.reply_photo(Config.PIC, caption=Text.ABOUT_TEXT.format(client.mention, user.mention), reply_markup=button)       
    else:
        await message.reply_text(text=Text.ABOUT_TEXT.format(client.mention, user.mention), reply_markup=button, disable_web_page_preview=True)

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=Text.START_TEXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup([[
                InlineKeyboardButton("🧑🏻‍💻 Developer", callback_data='dev')
                ],[
                InlineKeyboardButton('🤖 Update Channel', url='https://t.me/Star_Bots_Tamil'),
                InlineKeyboardButton('👥 Support Group', url='https://t.me/Star_Bots_Tamil_Support')
                ],[
                InlineKeyboardButton('🎛️ About', callback_data='about'),
                InlineKeyboardButton('🛠️ Help', callback_data='help')
                ],[
                InlineKeyboardButton('🔒 Close', callback_data='close')
            ]])
        )
    elif data == "help":
        await query.message.edit_text(
            text=Text.HELP_TEXT,
            parse_mode=enums.ParseMode.MARKDOWN,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("🤖 Update Channel", url="https://t.me/Star_Bots_Tamil")
                ],[
                InlineKeyboardButton("👥 Support Group", url='https://t.me/Star_Bots_Tamil_Support')
                ],[
                InlineKeyboardButton("🎛️ About", callback_data = "about"),
                InlineKeyboardButton("🏠 Home", callback_data = "start")
                ],[
                InlineKeyboardButton('🔒 Close', callback_data='close')
            ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=Text.ABOUT_TEXT.format(client.mention, query.from_user.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("🤖 Update Channel", url="https://t.me/Star_Bots_Tamil")
                ],[
                InlineKeyboardButton("👥 Support Group", url="https://t.me/Star_Bots_Tamil_Support")
                ],[
                InlineKeyboardButton("🛠️ Help", callback_data = "help"),
                InlineKeyboardButton("🏠 Home", callback_data = "start")
                ],[
                InlineKeyboardButton('🔒 Close', callback_data='close')
            ]])            
        )
    elif data == "dev":
        await query.message.edit_text(
            text=Text.DEV_TEXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("🤖 Update Channel", url="https://t.me/Star_Bots_Tamil")
                ],[
                InlineKeyboardButton("👥 Support Group", url="https://t.me/Star_Bots_Tamil_Support")
                ],[
                InlineKeyboardButton("🎛️ About", callback_data = "about"),
                InlineKeyboardButton("🏠 Home", callback_data = "start"),
                InlineKeyboardButton("🛠️ Help", callback_data = "help")
                ],[
                InlineKeyboardButton('🔒 Close', callback_data='close')
            ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

# prefix commond ✨
@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_prefix(client, message):
    if len(message.command) == 1:
        return await message.reply_text("**__Give The Prefix__\n\nExᴀᴍᴩʟᴇ:- `/set_prefix @Rkn_Bots`**")
    prefix = message.text.split(" ", 1)[1]
    RknDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    await db.set_prefix(message.from_user.id, prefix)
    await RknDev.edit("__**✅ ᴘʀᴇꜰɪx ꜱᴀᴠᴇᴅ**__")

@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):
    RknDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if not prefix:
        return await RknDev.edit("__**😔 ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴇꜰɪx**__")
    await db.set_prefix(message.from_user.id, None)
    await RknDev.edit("__**❌️ ᴘʀᴇꜰɪx ᴅᴇʟᴇᴛᴇᴅ**__")

@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_prefix(client, message):
    RknDev = await message.reply_text("Please Wait ...", reply_to_message_id=message.id)
    prefix = await db.get_prefix(message.from_user.id)
    if prefix:
        await RknDev.edit(f"**ʏᴏᴜʀ ᴘʀᴇꜰɪx:-**\n\n`{prefix}`")
    else:
        await RknDev.edit("__**😔 ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴇꜰɪx**__")
      
