import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 

    destination_channel_id = 1171944192390471765 
    url = f'https://discord.com/channels/1171944192390471762/{message.id}'

    embed = discord.Embed(
        title=message.channel.name,
        url=url,
        color=0x3498db 
    )
    embed.add_field(name="", value=message.author.mention, inline=False)
    for i in bot.get_channel(message.channel.id).applied_tags:
        embed.add_field(name='', value=f'`{i.name}`', inline=True)

    destination_channel = bot.get_channel(destination_channel_id)
    await destination_channel.send(embed=embed)

bot.run('MTE3MTk0NDYzMzUzODk3Nzg4Mg.GQhYSi.36pDEfk8RCso6ycgPnC4mMFxoMm84bRthCtE1c')
