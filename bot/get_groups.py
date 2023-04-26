from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest


from config import *

api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
phone_number = YOUR_PHONE_NUMBER

async def get_groups():
    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.start(phone=phone_number)
        dialogs = await client.get_dialogs()

        groups = []

        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                group_username = dialog.entity.username if dialog.entity.username else "No username"
                group_info = f"{dialog.name} (ID: {dialog.entity.id}, Username: {group_username})"
                print(group_info)
                groups.append(dialog.entity)
        # print("You are a member of the following groups and channels:")
        # print("\n".join(groups))
        return groups


