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
            "<b>😼 Hεllσ, Add Mε λs λdmιη Οf Υσυr Grσυρ Fιrsτ.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "SankiAssistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤗🧡 ΗεΥ, Αm Jσιηεd Ηεrε λs Υσυ Rεqυεsτεd.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>🤗🧡 Hεlρεr λlrεαdγ Ιη Υσυr Chατ.</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>⚠ Flσσd Wαιτ Errσr ⚠ \n Usεr {user.first_name} Cσυldη'τ Jσιη Υσυr Grσυρ Dυε Τσ ΗεανΥ Jσιη Rεqυεsτs Fσr Usεrβστ ! Mακε Sυrε Usεr Ιs Νστ βαηηεd Ιη Grσυp."
            "\n\nOr Mαηυαlly λdd @SankiRobot Τσ Υσυr Grσυρ ληd Τry Αgαιη.</b>",
        )
        return
    await message.reply_text(
        "<b>🤗🧡 Hεlρεr Usεrβστ Jσιηεd Υσυr Chατ.</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>🙄 Usεr Cσυldη'τ Lεανε Υσυr Grσυρ ! MαΥ βε Flσσdωαιτs."
            "\n\nOr Mαηυαlly Κιcκ Με Frσm Τσ Υσυr Grσυρ.</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("🤫 Assιsταητ Lεανιηg λll Chατs...")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assιsταητ Lεανιηg... Lεfτ : {left} Chατs. Fαιlεd : {failed} Chατs.")
            except:
                failed=failed+1
                await lol.edit(f"Assιsταητ Lεανιηg... Lεfτ : {left} Chατs. Fαιlεd : {failed} Chατs.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Lεfτ {left} Chατs. Fαιlεd {failed} Chατs.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is Chατ Ενεη Lιηκεd ??")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>😼 Hεllσ, Add Mε λs λdmιη Οf Υσυr Grσυρ Fιrsτ.</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "SankiAssistant"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤗🧡 ΗεΥ, Αm Jσιηεd Ηεrε λs Υσυ Rεqυεsτεd.")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>🤗🧡 Hεlρεr λlrεαdγ Ιη Υσυr Chατ.</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>⚠ Flσσd Wαιτ Errσr ⚠ \n Usεr {user.first_name} Cσυldη'τ Jσιη Υσυr Grσυρ Dυε Τσ ΗεανΥ Jσιη Rεqυεsτs Fσr Usεrβστ ! Mακε Sυrε Usεr Ιs Νστ βαηηεd Ιη Grσυp."
            "\n\nOr Mαηυαlly λdd @SankiRobot Τσ Υσυr Grσυρ ληd Τry Αgαιη.</b>",
        )
        return
    await message.reply_text(
        "<b>🤗🧡 Hεlρεr Usεrβστ Jσιηεd Υσυr Chατ.</b>",
    )
    