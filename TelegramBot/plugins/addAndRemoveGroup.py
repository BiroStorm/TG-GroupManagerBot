from pyrogram import filters

from ..customClient import customClient

@customClient.on_message(filters.command('addGroup', ['/','.']) & (filters.group | filters.channel))
async def add2DB(client : customClient, m):
    #if is a channel, who can write must be admin
    if (
        (m.chat.type == 'channel' and await client.adminInChannel(m))
        or client.is_admin(m)
    ) and client.connection['chatlist'].find_one({'id': m.chat.id}) is None:
        newItem = {'id': '100' + m.chat.id, 'name': m.chat.title, 'type': m.chat.type}
        chatlist = client.connection['chatlist']
        id = chatlist.insert_one(newItem)
        if id:
            print(f'new group added!\n{newItem}')
        logchannel = chatlist.find_one({'type': 'LogChannel'})
        if logchannel:
            await client.send_message(chat_id=logchannel['id'], text=f"New group [{m.chat.title} | {m.chat.id} ] added!")
        

# TODO 
# ADD A RESPONSE IN CASE THE GROUP IS ALREADY IN DB
