# Discord Forum Notification Bot

This bot, once added to a Discord server, gives you the ability to create and delete connections between a forum channel and a text channel. Using one of the connections the bot will read any new thread posted in the listed forum and then send its data to the respective text channel.

# Adding the Bot to you Server

To add this bot to your server, go to your web browser and enter the following link (this has to be done as an administrator of the server):  
<https://discord.com/api/oauth2/authorize?client_id=1171944633538977882&permissions=8&scope=bot>

When you open the link it will prompt you to add the bot to your server.

# Bot Commands

All the following commands are prefixed with "!".

Create a new connection:

Command: !create {forum} {text channel}
Description: Create a new connection between a forum and a text channel.
Delete a connection:

Command: !delete {forum} {text channel}
Description: Delete an existing connection between a forum and a text channel.
Remove connections that contain nonexistent channels:

Command: !update
Description: Remove connections that contain nonexistent channels.
View all commands:

Command: !h
Description: View all available commands.
