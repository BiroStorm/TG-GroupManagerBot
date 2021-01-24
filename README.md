
  

# [Telegram Bot] Group Manager

  

A simple telegram bot the can manage a group, it was created for an "Italian Community Group".

  

I published it on github so everyone can see how it was made and if someone have any suggestion can help implement it.

  

  

## :star2: How is made :star2:

  

It's written in python using [Pyrogram](https://github.com/pyrogram/pyrogram), it use MongoDB as main database to store data.

  

  

## :books: Commands :books:

#### Staff Management

Command | Args | Where | Comment 
------- | ----------| ------- | --------
/Staff  | None		| Private | See list of staffs
/addStaff | [username \| id]| Private | Make a user a staffer
/rmStaff | [username \| id]| Private | Remove a staffer
  
  
#### Groups Management

Command | Arguments | Where | Comment 
------- | ----------| ------- | --------
/addGroup | None | Group | Add a group into DB
/rmGroup | None | Group | remove a group from the db
/getLink | None | Group | Retrive or generate a private link to the group
/revokelink | None | Group | Revoke a link from a specific group
/revokeAll | None | Any | Revoke all generated links from all groups
/setLog | None | Channel | Set a channel as log channel
/unLog | None | Channel | Remove the log channel
/globalban | [Reply \| id \| username]| Any | Ban a user from all groups and channels
/globalunban | [Reply \| id \| username]| Any | Unban a user from all groups and channels

#### Others

Command | Arguments | Where | Comment 
------- | ----------| ------- | --------
/permissions | [Reply] | Group | Change a member special permission (work only if who use this command has the permission "can_promote_members"
/pin | [Reply] | Group | Pin a message (only who has the permission to use this command, to give or take this permission use /permission)
/broadcast | [Reply] | Private | Send a message or photo with caption to all groups. *for now all buttons is in italians, I need to change it*

## Requirements & environment variables in `config.ini`

  

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