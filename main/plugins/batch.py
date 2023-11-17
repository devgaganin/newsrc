"""
Plugin for both public & private channels!
"""

import time
import os
import asyncio
from telethon import events, Button
from telethon.errors import FloodWait
from .. import bot as Drone
from .. import userbot, Bot, AUTH
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_bulk_msg
from main.plugins.helpers import get_link
from pyrogram import Client 
from pyrogram.errors import FloodWait

ft = f"To use this bot, you've to join @{fs}."

batch = []

@Drone.on(events.NewMessage(incoming=True, pattern='/cancel'))
async def cancel(event):
    if event.sender_id not in batch:
        return await event.reply("No batch active.")
    batch.clear()
    await event.reply("Done.")

@Drone.on(events.NewMessage(incoming=True, pattern='/batch'))
async def _batch(event):
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if not s:
        await event.reply(r)
        return       
    if event.sender_id in batch:
        return await event.reply("You've already started one batch, wait for it to complete, you dumbfuck owner!")
    
    async with Drone.conversation(event.chat_id) as conv: 
        await conv.send_message("Send me the message link you want to start saving from, as a reply to this message.", buttons=Button.force_reply())
        try:
            link = (await conv.get_reply()).text
            try:
                _link = get_link(link)
            except Exception:
                await conv.send_message("No link found.")
                return conv.cancel()
        except Exception as e:
            print(e)
            await conv.send_message("Cannot wait longer for your response!")
            return conv.cancel()
        
        await conv.send_message("Send me the number of files/range you want to save from the given message, as a reply to this message.", buttons=Button.force_reply())
        try:
            _range = (await conv.get_reply()).text
        except Exception as e:
            print(e)
            await conv.send_message("Cannot wait longer for your response!")
            return conv.cancel()
        
        try:
            value = int(_range)
            if value > 100:
                await conv.send_message("You can only get up to 100 files in a single batch.")
                return conv.cancel()
        except ValueError:
            await conv.send_message("Range must be an integer!")
            return conv.cancel()
        
        batch.append(event.sender_id)
        await run_batch(userbot, Bot, event.sender_id, _link, value) 
        conv.cancel()
        batch.clear()

async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 5
        elif 25 <= i < 50:
            timer = 10
        elif 50 <= i < 100:
            timer = 15
        if not 't.me/c/' in link:
            timer = 2 if i < 25 else 3
        try: 
            if sender not in batch:
                await client.send_message(sender, "Batch completed.")
                break
        except Exception as e:
            print(e)
            await client.send_message(sender, "Batch completed.")
            break
        try:
            await get_bulk_msg(userbot, client, sender, link, i) 
        except FloodWait as fw:
            if int(fw.x) > 299:
                await client.send_message(sender, "Cancelling batch since you have floodwait more than 5 minutes.")
                break
            await asyncio.sleep(fw.x + 5)
            await get_bulk_msg(userbot, client, sender, link, i)
        protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and protect the account!")
        await asyncio.sleep(timer)
        await protection.delete()
