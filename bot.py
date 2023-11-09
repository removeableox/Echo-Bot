import discord
from discord.ext import commands
import sqlite3

list = []

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

connection = sqlite3.connect("main.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS connections (source INTEGER, destination INTEGER, UNIQUE(source, destination))")
connection.commit()

@bot.command()
async def create(ctx, arg1, arg2):
    try:
        source = [channel for channel in ctx.guild.channels if channel.name == arg1][0].id
        destination = [channel for channel in ctx.guild.channels if channel.name == arg2][0].id
        print(bot.get_channel(source).type , bot.get_channel(destination).type)
        if bot.get_channel(source).type != discord.ChannelType.forum or bot.get_channel(destination).type != discord.ChannelType.text:
            await ctx.send('Invalid sequence.')
            return
        cursor.execute("INSERT OR IGNORE INTO connections (source, destination) VALUES (?, ?)", (source, destination))
        connection.commit()

        await ctx.send('Connection established!!!')
    except Exception as e:
        print(e)
        await ctx.send('Connection error!!!')

@bot.command()
async def delete(ctx, arg1, arg2):
    source = [channel for channel in ctx.guild.channels if channel.name == arg1][0].id
    destination = [channel for channel in ctx.guild.channels if channel.name == arg2][0].id
    cursor.execute("DELETE FROM connections WHERE source = ? AND destination = ?", (source, destination))
    connection.commit()

    await ctx.send('Connection terminated!!!')

@bot.command()
async def update(ctx):
    rows = cursor.execute("SELECT * FROM connections").fetchall()
    for row in rows:
        if not bot.get_channel(row[0]) or not bot.get_channel(row[1]):
            cursor.execute("DELETE FROM connections WHERE source = ?", (row[0],))
            connection.commit()

@bot.command()
async def h(ctx):
    embed = discord.Embed(
        title="COMMANDS",
        color=0x3498db 
    )
    embed.add_field(name="Create a new connection:", value="!create {forum} {text channel}", inline=False)
    embed.add_field(name="Delete a connection:", value="!delete {forum} {text channel} ", inline=False)
    embed.add_field(name="Remove connections that contain nonexistent channels:", value="!update", inline=False)
    embed.add_field(name="View all commands:", value="!h", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def view(ctx):
    rows = cursor.execute("SELECT * FROM connections").fetchall()
    for i in rows:
        await ctx.send(bot.get_channel(i[0]).name + ' to ' + bot.get_channel(i[1]).name)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    past = [i.content async for i in bot.get_channel(message.channel.id).history(limit=None)] 
    if message.author == bot.user or message.content != past[-1]:
        return 

    destination_channel_id = cursor.execute("SELECT destination FROM connections WHERE source = ?", (int(message.channel.parent.id),)).fetchall()[0][0]
    print(destination_channel_id)
    url = f'https://discord.com/channels/{message.guild.id}/{message.id}'

    embed = discord.Embed(
        title=message.channel.name,
        description=message.content,
        url=url,
        color=0x3498db 
    )
    embed.add_field(name="", value=message.author.mention, inline=False)
    for i in bot.get_channel(message.channel.id).applied_tags:
        embed.add_field(name='', value=f'`{i.name}`', inline=True)

    destination_channel = bot.get_channel(destination_channel_id)
    await destination_channel.send(embed=embed)

def main(token):
    bot.run('token')
