from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from asyncio import sleep
from bot.get_groups import get_groups
from config import *


async def send_message_with_delay(client, entity, message, delay):
    await sleep(delay)
    await client.send_message(entity, message)



async def main():
    async with TelegramClient('anon', YOUR_API_ID, YOUR_API_HASH) as client:
        await client.start(phone=YOUR_PHONE_NUMBER)
        

        groups = await get_groups()

    

        message = MESSAGE
        delay = DELAY

        for group in groups:
            print(f"Sending message to {group.title} (ID: {group.id})")
            await send_message_with_delay(client, group, message, delay)
            print(f"Message sent to {group.title} (ID: {group.id})")