from base64 import urlsafe_b64decode
from struct import unpack
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import RPCError

from ...customClient import customClient

@customClient.on_message(filters.command("resolve", [".", "/"]))
async def resolve_invite(client: customClient, message: Message):
    if client.is_admin(message):
        link = message.command[1].split("/")[-1]
        d = urlsafe_b64decode(link + "==")
        try:
            await message.reply(
                "Invite Link: `{}`\nAdmin: `{}`\nChat: `-100{}`\nHash: `{}`".format(
                    link, *unpack(">iiq", d)
                )
            )
        except RPCError as e:
            await client.send_message(client.CREATOR_ID, "Error in resolve_invite: " + e.MESSAGE)