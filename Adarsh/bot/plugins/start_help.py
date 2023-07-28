import random
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲** \n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]
                        ]
                    )
                    
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    
                    disable_web_page_preview=True)
                return
        await m.reply_photo(
            photo="https://graph.org/file/f20d1210495df4bd7b4c8.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪ,ᴀᴍ ᴀ ᴩʀᴏ✨️ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ. A sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴡɪᴛʜ ʙᴇꜱᴛ ꜰᴇᴀᴛᴜʀᴇꜱ⚡️.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴠɪᴅᴇᴏ / ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀ...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("✲ UᴩᴅΔᴛᴇꜱ ✲", url="https://t.me/Bot_cracker"), InlineKeyboardButton("☆ MᴏVɪᴇꜱ ☆", url="https://t.me/Mod_MoviezX")],
                    [InlineKeyboardButton("♚ Oᴡɴᴇʀ ♚", user_id=1733124290), InlineKeyboardButton ("⌬ Bᴀᴄᴋ-Uᴩ ⌬", url="https://t.me/+7TYOxeNL37I5MWRl"), InlineKeyboardButton("⚘ Bᴏᴛꜱ ➾", url="https://t.me/Bot_Cracker/17")],
                    [InlineKeyboardButton("✫ Mᴏᴠɪᴇꜱ Gʀᴏᴜᴩ ✫", url="https://t.me/+d7djWG_VLfcwMzg9")]
                ]
            ),
            
        )
    else:
        if Var.UPDATES_CHANNEL is not None:
            try:
                user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await b.send_message(
                        chat_id=m.chat.id,
                        text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                        
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲** \n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                            ]                           
                        ]
                    )
                    
                )
                return
            except Exception:
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                    disable_web_page_preview=True)
                return

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**Yᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\nꜱᴩᴇᴄɪᴀʟ ᴛʜᴀɴᴋꜱ ᴛᴏ..... <a href='http://t.me/Mod_MoviezX'>𐂮 ᴍᴏᴅ ᴍᴏᴠɪᴇᴢ ˹x˼™</a>**"
        await m.reply_photo(
            photo=random.choice(Var.PICS),
            caption=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⚡ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ⚡", url=stream_link)]])
        )


@StreamBot.on_message(filters.command('help') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲** \n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                
                disable_web_page_preview=True)
            return
    await message.reply_photo(
            photo=random.choice(Var.PICS),
            caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ , ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴀ ʏᴏᴜ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ɪᴛ...\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴀʟꜱᴏ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ.\n\n┣⪼ ᴛʜɪs ʙᴏᴛ ɪs ᴀʟsᴏ sᴜᴘᴘᴏʀᴛ ɪɴ ᴄʜᴀɴɴᴇʟ [ᴩʀᴏ✨️]. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴛᴏ ɢᴇᴛ ʀᴇᴀʟᴛɪᴍᴇ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ғᴏʀ ᴇᴠᴇʀʏ ғɪʟᴇs/ᴠɪᴅᴇᴏs ᴘᴏsᴛ../\n\n ┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /about\n\n\n⚠Cᴜᴀᴛɪᴏɴ ᴀʜᴇᴀᴅ ;\n✧ sᴘᴀᴍ = ʙᴀɴ \n✧ ᴅᴏɴᴛ ᴜꜱᴇ ᴀᴅᴜʟᴛ ᴠɪᴅᴇᴏꜱ, ɪꜰ yᴏᴜ ᴡᴀɴᴛ yᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜᴇ ꜱɪᴛᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ɢᴏᴏɢʟᴇ ᴏʀ ᴅᴏᴡɴʟᴏᴀᴅ ꜰɪʟᴇꜱ, ᴅᴏɴᴛ ᴜꜱᴇ ᴏᴜʀ ʙᴏᴛ ꜰᴏʀ ᴛʜᴀᴛ [ʙᴇ ᴀ ɢᴏᴏᴅ ᴏɴᴇ😇 #yᴏᴜᴡɪʟʟɢᴇᴛᴄʜᴀɴᴄᴇᴀʟꜱᴏ] \nᴘʟᴇᴀsᴇ sʜᴀʀᴇ ᴀɴᴅ sᴜᴩᴩᴏʀᴛ ᴜꜱ!!!**", 
  
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 ⚡", url="https://t.me/kwicbotupdates"), InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/kwicbotupdates")],
                [InlineKeyboardButton("📺 24/7 𝙼𝙾𝚅𝙸𝙴𝚂 📺", url="https://t.me/MoviesNowV2"), InlineKeyboardButton("💎𝙾𝚃𝚃 𝙼𝙾𝚅𝙸𝙴𝚂💎", url="https://t.me/MoviesNowOTT2")],
                [InlineKeyboardButton("💌 𝙼𝙾𝚅𝙸𝙴 𝙱𝙾𝚃 💌", url="https://t.me/KWICVER2bot")]
            ]
        )
    )

@StreamBot.on_message(filters.command('about') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    if Var.UPDATES_CHANNEL is not None:
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == enums.ChatMemberStatus.BANNED:
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ../**",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ  ᴍᴇ..🥹🥹**\n\n**ᴛʜᴇʀᴇ ᴍᴀɴy ᴜꜱᴇʀꜱ ᴀɴᴅ ᴡᴇ ᴀʀᴇ ɢɪᴠɪɴɢ ᴛʜɪꜱ ꜱᴇʀᴠɪᴄᴇ ꜰᴏʀ ꜰʀᴇᴇ🥲** \n\n**Sᴏ ᴩʟᴇᴀꜱᴇ ꜱᴜᴩᴩᴏʀᴛ ᴜꜱ ..!😔😔**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⍟ ᴊᴏɪɴ ᴍʏ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ⍟", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**𝙰𝙳𝙳 𝙵𝙾𝚁𝙲𝙴 𝚂𝚄𝙱 𝚃𝙾 𝙰𝙽𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻**",
                
                disable_web_page_preview=True)
            return
    await message.reply_photo(
            photo="https://graph.org/file/bee17850e842b8ecaad3c.jpg",
            caption="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs😜</b>

<b>╭━━━━━━━⦍ ⸢ʙᴏᴛ-ᴅᴇᴛᴀɪʟꜱ⸥ ⦐</b>
┃
┣⪼<b>Bᴏᴛ ɴΔᴍᴇ : <a href='https://t.me/Ms_FiLe2LINk_bOt'>˹ᴍꜱ˼ ˾ꜰɪʟᴇ 2 ʟɪɴᴋ˺ ʙoᴛ𐂴</a></b>
┣⪼<b>Oᴡɴᴇʀ : <a href='http://t.me/Syd_Xyz'>мґ 𝕾𝖄𝕯 ️✨️️</a></b>
┣⪼<b>Uᴘᴅᴀᴛᴇꜱ : <a href='https://t.me/Bot_cracker'>𝗞𝗪𝗜𝗖𝗕𝗢𝗧 𝗨𝗣𝗗𝗔𝗧𝗘𝗦</a></b>
┣⪼<b>Sᴜᴘᴘᴏʀᴛ : <a href='https://t.me/kwic2002'>𝗞𝗪𝗜𝗖</a></b>
┣⪼<b>sᴇʀᴠᴇʀ : 
┣⪼<b>ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
┣⪼<b>ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ 3</b>
┣⪼<b>sᴏᴜʀᴄᴇ-ᴄᴏᴅᴇ : <a href='https://github.com/kwicfletolinkbot'>𝗞𝗪𝗜𝗖𝗕𝗢𝗧𝗦</a></b>
┣⪼<b>𝙼𝚘𝚟𝚒𝚎-𝙶𝚛𝚘𝚞𝚙 : <a href='https://t.me/MoviesNowV2'>𝙼𝚘𝚟𝚒𝚎𝚜𝙽𝚘𝚠𝚅2</a></b>
┃
<b>╰━━━━━━━〔ᴘʟᴇᴀsʀ sᴜᴘᴘᴏʀᴛ〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ⚡", url="https://t.me/kwicbotupdates"), InlineKeyboardButton("📺 24/7 𝙼𝙾𝚅𝙸𝙴𝚂 📺", url="https://t.me/MoviesNowV2")],
                [InlineKeyboardButton("💌 𝙼𝙾𝚅𝙸𝙴𝙱𝙾𝚃 💌 ", url="https://t.me/KWICVER2bot")]
            ]
        )
    )
