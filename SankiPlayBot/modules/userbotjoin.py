from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from SankiPlayBot.helpers.decorators import authorized_users_only, errors
from SankiPlayBot.services.callsmusic.callsmusic import client as USER
from SankiPlayBot.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b> dd M s Adm f Yr Gr Frs.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "SankiAssistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "   Jd hs Gr Fr lyg sc  Vc.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b> lr Usr lrdy Addd Yr Gr.</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b> Fld W Errr  \nUsr {user.first_name} Cld' J ur Chal D  y Rqs  Fr Usr ! M Sr Usr Is  d  Gr."
            "\n\nr Mlly Add @SankiRobot  r Gr d TrY Ag.</b>",
        )
        return
    await message.reply_text(
        "<b> lr Usr Jd Yr Gr.</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Us cd'  y g! y  fds."
            "\n\nO y kck  f y g</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Asss g  cs...")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Asss g... Lf : {left} Chs. Fld : {failed} Chs.")
            except:
                failed=failed+1
                await lol.edit(f"Asss g... Lf: {left} Chs. Fld : {failed} Chs.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Lf {left} Chs. Fld {failed} Chs.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply(" Ch s cctd r N ?")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b> dd M s Adm f Yr Gr Frs.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "SankiAssistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b> lr Usr lrdy Addd Yr Gr.</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b> Fld W Errr  \nUsr {user.first_name} Cld' J ur Chal D  y Rqs  Fr Usr ! M Sr Usr Is  d  Gr."
            "\n\nr Mlly Add @SankiRobot  r Gr d TrY Ag.</b>",
        )
        return
    await message.reply_text(
        "<b> lr Usr Jd Yr Gr.</b>",
    )
    
