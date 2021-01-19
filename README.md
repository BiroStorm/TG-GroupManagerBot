
# [Telegram Bot] Group Manager

A simple telegram bot the can manage a group, it was created for an "Italian Community Group".

I published it on github so everyone can see how it was made and if someone have any suggestion can help implement it.

  
  

## :star2: How is made :star2:

It's written in python using [Pyrogram](https://github.com/pyrogram/pyrogram), it use MongoDB as main database to store data.

  

## Requirements & environment variables in  `config.ini` 

* Mongo Database
* Python 3+

After copying this project, create a `config.ini` file inside `TelegramBot` directory with:
```
[pyrogram]
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN

[plugins]
root = plugins

[database]
link = URL_TO_MONGODB
dbname = NAMEOFYOURDB

[creator]
id = YOUR_TELEGRAM_ACCOUNT_ID
```


-----
### Run in console
Run the following command outside the `TelegramBot` directory:
```
python -m TelegramBot
```
----
### Run with Docker
Create an image with docker:
```
docker build -t botimg .
```
Run the image:
```
docker run --name TGgroupmanager botimg 
```


## Disclamer
This was a project I made a lot of time ago (mid 2020) but right now I haven't much time to continue it or update it. This project was not intended to be used with other groups other than the one is made for it should work for other groups too.
This project is not complete, but it should work, I have updated it to the new version of Pyrogram (1.0.7), and it should keep working until a new big update of Pyrogram.

If you have some problem with this project contact me on telegram @BrioStoCazz