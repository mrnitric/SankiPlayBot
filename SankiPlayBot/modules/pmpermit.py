from pyrogram import Client
import asyncio
from SankiPlayBot.config import SUDO_USERS, PMPERMIT
from pyrogram import filters
from pyrogram.types import Message
from SankiPlayBot.services.callsmusic.callsmusic import client as USER

PMSET =True
pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    if PMPERMIT == "ENABLE":
        if PMSET:
            chat_id = message.chat.id
            if chat_id in pchats:
                return
            await USER.send_message(
                message.chat.id,
                "Hεllö, тнıs ıs α мυsıc αssısтαηт sєяѵıcє.\n\n ❗️ Rυłєs:\n   - Nσ cнαттıηg αłłσωєd\n   - Nσ sραм αłłσωєd \n\n 👉 **Sєηd yσυя gяσυρ ıηѵıтє łıηk σя υsєяηαмє нєяє @BrandSanki ıf υsєявσт cαη'т jσıη yσυя gяσυρ.**\n\n ⚠️ Dıscłαмєя: ıf yσυ ηєєd αηy нєłρ тнєη jσıη sυρρσят gяσυρ :- @BrandSanki\n    - Dση'т αdd тнıs υsєя тσ sєcяєт gяσυρs.\n   - Dση'т sнαяє ρяıѵαтє ıηfσ нєяє\n\n",
            )
            return

    

@Client.on_message(filters.command(["/pmpermit"]))
async def bye(client: Client, message: Message):
    if message.from_user.id in SUDO_USERS:
        global PMSET
        text = message.text.split(" ", 1)
        queryy = text[1]
        if queryy == "on":
            PMSET = True
            await message.reply_text("Pмρєямıт тυяηєd ση 🧡")
            return
        if queryy == "off":
            PMSET = None
            await message.reply_text("Pмρєямıт тυяηєd σff 🧡")
            return

@USER.on_message(filters.text & filters.private & filters.me)        
async def autopmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("~ Aρρяσσѵєd тσ ρм dυє тσ συтgσıηg мєssαgєs.")
        return
    message.continue_propagation()    
    
@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)
async def pmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if not chat_id in pchats:
        pchats.append(chat_id)
        await message.reply_text("~ Aρρяσσѵєd тσ PM")
        return
    message.continue_propagation()    
    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)
async def rmpmPermiat(client: USER, message: Message):
    chat_id = message.chat.id
    if chat_id in pchats:
        pchats.remove(chat_id)
        await message.reply_text("~ DιsAρρяσσѵєd тσ PM")
        return
    message.continue_propagation()    
