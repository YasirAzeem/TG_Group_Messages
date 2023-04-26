from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from asyncio import sleep
from bot.get_groups import get_groups
from config import *


async def send_message_with_delay(client, entity, message, delay):
    await sleep(delay)
    await client.send_message(entity, message)



async def main():

        

    groups = await get_groups()
    allowed_groups = [x.replace('@','').strip() for x in GROUPS.split('\n')]
    sent_count = 0
    message = MESSAGE
    delay = 3600/len(allowed_groups)
    async with TelegramClient('anon', YOUR_API_ID, YOUR_API_HASH) as client:
        await client.start(phone=YOUR_PHONE_NUMBER)
        for group in groups:
            if group.username.strip() in allowed_groups:
                # print(f"Sending message to {group.title} (ID: {group.id}) (Username: {group.username})")
                await send_message_with_delay(client, group, message, delay)
                sent_count+=1
                print(f"{sent_count} | Message sent to {group.title} (ID: {group.id}) (Username: {group.username})")
            else:
                print(f"Group {group.title} (ID: {group.id}) (Username: {group.username}) is not in allowed groups list.")