from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from SankiPlayBot.config import SUDO_USERS

@Client.on_message(filters.command(["gcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in SUDO_USERS:
        lol = await message.reply("🔄 Sταrτιηg Glσβαlly Cαsτιηg...")
        if not message.reply_to_message:
            await lol.edit("🙄 Rερly Τσ ληy Τεχτ Μεssαgε Τσ Gcαsτ Sιr.")
            return
        msg = message.reply_to_message.text
        async for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"🔄 Gcαsτιηg.. Sεητ : {sent} Chατs. Fαιlεd : {failed} Chατs.")
            except:
                failed=failed+1
                await lol.edit(f"🔄 Gcαsτιηg.. Sεητ : {sent} Chατs. Fαιlεd : {failed} Chατs.")
            await asyncio.sleep(3)
        await message.reply_text(f"🙄 Gcαsτεd Μεssαgε Τσ {sent} Chατs. Fαιlεd {failed} Chατs.")
