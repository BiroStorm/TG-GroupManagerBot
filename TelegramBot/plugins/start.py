from pyrogram import filters

from ..customClient import customClient

@customClient.on_message(filters.command('start', ['/','.']) & filters.private)
async def startcmd(client : customClient, m):
    #start cmd check if bot is online
    await m.reply("Hello there! I'm Online!")