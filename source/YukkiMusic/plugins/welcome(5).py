import asyncio
from pyrogram import Client, filters
from datetime import datetime

@app.on_message(filters.member_joined)
async def get_chat_info(chat, already=False):
    if not already:
        chat = await app.get_chat(chat)
    chat_id = chat.id
    members = chat.members_count
	await message.reply_text(f"""
● نورت يحلو ♥♡
{message.from_user.first_name}
●  يجب احترام الادمنية
●  الالتزام بالقوانين في الوصف
●  الاعضاء  {members} 
""")


@app.on_message(filters.member_left)
async def leftmem(chat):
    await message.reply_text(f"""
    ★انت مو حبي يا «{ message.from_user.first_name}» 
★ وين اكو مثل هذا الكروب وتريد تطلع
★ احلى جمعة هنا  حبايب واصدقاء 
★ توكل يلا الله وياك
√""")