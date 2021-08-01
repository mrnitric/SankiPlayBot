from asyncio.queues import QueueEmpty
from SankiPlayBot.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from SankiPlayBot.function.admins import set
from SankiPlayBot.helpers.channelmusic import get_chat_id
from SankiPlayBot.helpers.decorators import authorized_users_only, errors
from SankiPlayBot.helpers.filters import command, other_filters
from SankiPlayBot.services.callsmusic import callsmusic



@Client.on_message(filters.command(["channelpause","cpause"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def pause(_, message: Message):
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is Thıs Chατ Ενεη Lıηκεd ?")
      return    
    chat_id = chid
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("❗ Νσ Aηy Sσηg ıs Playιηg Oη Vc 😼")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("▶️ Sσηg Hαs Bεεη Ραυsəd My Lord 😼")


@Client.on_message(filters.command(["channelresume","cresume"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def resume(_, message: Message):
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is Thıs Chατ Ενεη Lıηκεd ?")
      return    
    chat_id = chid
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("❗ Νσ Aηy Sσηg ıs Ραυsəd Oη Vc 😼")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("⏸ Sσηg Hαs Bεεη Rεsuməd My Lord 😼")


@Client.on_message(filters.command(["channelend","cend"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is Thıs Chατ Ενεη Lıηκεd ?")
      return    
    chat_id = chid
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Νσ Aηy Sσηg ıs Strεαmıηg Oη Vc 😼")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("❌ Sσηg Strεαmıηg Hαs Bεεη Stσρρəd My Lord 😼")


@Client.on_message(filters.command(["channelskip","cskip"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is Thıs Chατ Ενεη Lıηκεd ?")
      return    
    chat_id = chid
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("❗ Νσ Aηy Sσηg ıs Playιηg Oη Vc Tσ Sκıρ 😼")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"🔄 Sκιρρεd - **{skip[0]}**\n🔛 Nσω Playιηg - **{qeue[0][0]}**")


@Client.on_message(filters.command("channeladmincache"))
@errors
async def admincache(client, message: Message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is Thıs Chατ Ενεη Lıηκεd ?")
      return
    set(
        chid,
        [
            member.user
            for member in await conchat.linked_chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("❇️ Admıη CαcΗə Rəfrεshed.")
