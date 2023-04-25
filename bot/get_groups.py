from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetAllChatsRequest

from config import *

api_id = YOUR_API_ID
api_hash = YOUR_API_HASH
phone_number = YOUR_PHONE_NUMBER

async def get_groups():
    async with TelegramClient('anon', api_id, api_hash) as client:
        await client.start(phone=phone_number)
        all_chats = await client(GetAllChatsRequest([]))

        groups = []

        for chat in all_chats.chats:
            if chat.megagroup or chat.broadcast:
                try:
                    full_chat = await client(GetFullChannelRequest(chat.id))
                    participants_count = full_chat.full_chat.participants_count
                except Exception as e:
                    participants_count = 0

                group_info = f"{chat.title} (ID: {chat.id}) - {participants_count} members"
                groups.append(group_info)
        print("You are a member of the following groups and channels:")
        print("\n".join(groups))
        return groups


