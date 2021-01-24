from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton
from pyrogram import __version__
from pyrogram.raw.all import layer
import configparser

from pymongo import MongoClient
from pymongo.database import Database

import configparser

class customClient(Client):
    CREATOR_ID = 510456529

    def __init__(self):
        name = self.__class__.__name__.lower()
        print(name)
        super().__init__(
            name,
            config_file="TelegramBot/config.ini",
            plugins=dict(
                root="TelegramBot/plugins"
            ))
        self.admins = []
        self.connection : Database

    async def start(self):
        await super().start()

        print('Connecting the DB...')
        config = configparser.ConfigParser()
        config.read('TelegramBot/config.ini')
        if 'database' in config.sections() and 'link' in config['database'] and 'dbname' in config['database']:
            client = MongoClient(config['database']['link'])
            self.connection = client[config['database']['dbname']]
            self.mainID = int(config['creator']['id'])
        else:
            print("config.ini wrong, need [database] section with under link and collection values.")
            exit(0)
        print('Database connected!')

        self.loadAdmin()

        me = await self.get_me()
        print(f"Custom Bot v{__version__} (Layer {layer}) started on @{me.username}. Hi.")

    async def stop(self, *args):
        await super().stop()
        print("Custom Bot stopped!")

    def loadAdmin(self):
        staffdb = self.connection["stafflist"]
        cursor = staffdb.find({})
        self.admins = [self.CREATOR_ID, self.mainID]
        for document in cursor:
            if document['id'] not in self.admins:
                self.admins.append(document['id'])

    def is_admin(self, message) -> bool:
        return message.from_user.id in self.admins
        
    #check if there is an admin inside a channel
    async def adminInChannel(self, m):
        channelStaff = await self.get_chat_members(m.chat.id, filter="administrators")
        staffId = [x.user.id for x in channelStaff if x.user.id in self.admins]
        return len(staffId) > 0
    
    def invertCBQBool(self, inlineKeyboardButton):
        if inlineKeyboardButton.callback_data.split(' ')[-1] == "false":
            newcallback = inlineKeyboardButton.callback_data.rsplit(' ', 1)[
                0] + " true"
            newbutton = inlineKeyboardButton.text.rsplit(' ', 1)[0] + " ✅"
        else:
            newcallback = inlineKeyboardButton.callback_data.rsplit(' ', 1)[
                0] + " false"
            newbutton = inlineKeyboardButton.text.rsplit(' ', 1)[0] + " ❌"

        return InlineKeyboardButton(newbutton, newcallback)

    @staticmethod
    def CBFilter(data):
        return filters.create(
            lambda flt, query: flt.data.lower() == query.data.split(' ', 1)[0].lower() and query.message.from_user.is_self,
            data=data  # "data" kwarg is accessed with "flt.data" above
    )
