#
# Copyright (C) 2023-2024 by TeamScary@Github, < https://github.com/TeamScary >.
#
# This file is part of < https://github.com/TeamScary/Ai-UserBot > project,
#
# All rights reserved.

from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from os import getenv
import re
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", None)
MONGO_URL = getenv("MONGO_URL", None)

client = Client(SESSION_NAME, API_ID, API_HASH)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in client.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

@client.on_message(
    filters.command("repo", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.delete()
    scaryai = await message.reply("๐")
    await asyncio.sleep(1)
    await scaryai.edit("**สแดแดแด แดแด แดสษชแด แดแดแด สแด สแดแดแดสแด ๐๐๐**")
    await asyncio.sleep(1)
    await scaryai.edit("**แดสแดสแด แดส แดษชssษช แดแด ๐๐ฅฐ**")
    await scaryai.delete()
    await asyncio.sleep(2)
    umm = await message.reply_sticker("CAACAgEAAxkBAAICOGPkoH1fKzKpaISh7XgNeisx3UVVAAK1AwACKWtwRmr9H9xzpEZDLgQ")
    await asyncio.sleep(2)
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/861af4bf86acce53e0544.jpg",
        caption=f"""**โโโโโโโโโโโโโโโโโโโโโโ
๐ฅ แด แดแดแดกแดสาแดสส แดษช สแดแด แดา [Pสแดแดแดษช](https://t.me/NomorePreeti) ๐บ๐
โโโโโโโโโโโโโโโโโโโ
แดแดแดแดสแดsแด สแดแดแดแดษดแด สแดแด าแดส แดษข..
โโโโโโโโโโโโโโโโโโโ
โฃร แดแดกษดแดส โ [Mสs.Mแดสแดsสแดกแดสษช](https://t.me/NomorePreeti)
โฃร sแดสsแดสษชสแด แดษด โ [สแดแดแดแดสแด](https://youtube.com/@caringlover)
โฃร sแดแดแดแดสแด โ [sแดแดแดแดสแด](https://t.me/ScaryNetwork)
โฃร แดแดแดแดแดแดs โ [แดแดแดแดแดแดs](https://t.me/ScaryServer)
โฃร sแดแดสแดแด แดแดแดแด โ [สแดสแด](https://github.com/TheTeamScary/MissCutie-Bot)
โฃร แดสแดแดแดแดส โ [Mส.Mแดสแดsสแดกแดสษช](https://t.me/NomoreLakshya)
โโโโโโโโโโโโโโโโโโโ
๐ฅ  ษชา สแดแด สแดแด แด แดษดส วซแดแดsแดษชแดษด แดสแดษด ษขแด แดแด sแดแดแดแดสแด ษขสแดแดแด [Hแดสแด](https://t.me/chat_ixz)**""",
    ) 


@client.on_message(
    filters.command("alive", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**แดแดแดษชแด แดsแดสสแดแด ษชs สแดแดแดส าแดส แดสแดแดแดษชษดษข**")

@client.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    scarydb = MongoClient(MONGO_URL)    
    scary = scarydb["ScaryDb"]["Scary"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                ""
            )
    is_scary = scary.find_one({"chat_id": message.chat.id})
    if not is_scary:
        scary.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"**แดสแดแดสษชแด ษชs แดษชsแดสสแดแด สส {message.from_user.mention()} าแดส แดsแดสs ษชษด {message.chat.title}**")
    if is_scary:
        await message.reply_text(f"**แดสแดแดสษชแด ษชs แดสสแดแดแดส แดษชsแดสสแดแด**")
    

@client.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    scarydb = MongoClient(MONGO_URL)    
    scary = scarydb["ScaryDb"]["Scary"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "สแดแด แดสแด ษดแดแด แดแดแดษชษด"
            )
    is_scary = scary.find_one({"chat_id": message.chat.id})
    if not is_scary:           
        await message.reply_text(f"**แดสแดแดสษชแด ษชs แดสสแดแดแดส แดษดแดสสแดแด**")
    if is_scary:
        scary.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"**แดสแดแดสษชแด ษชs แดษดแดสสแดแด สส {message.from_user.mention()} าแดส แดsแดสs ษชษด {message.chat.title}**")
    

@client.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**แดsแดแดษขแด:**\n/chatbot [on|off] แดษดสส ษขสแดแดแด**")

    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scaryai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})
       if not is_scary:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_scary:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scarystickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})
       if not is_scary:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       scarydb = MongoClient(MONGO_URL)
       scary = scarydb["ScaryDb"]["Scary"] 
       is_scary = scary.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_scary:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scaryprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def scaryprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
