import discord
from discord.ext import commands

list = []

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    channel = bot.get_channel(message.channel.id)
    past = [i.content async for i in channel.history(limit=None)] 
    if message.author == bot.user or message.content != past[-1]:
        return 

    destination_channel_id = 1171944192390471765 
    url = f'https://discord.com/channels/1171944192390471762/{message.id}'

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

bot.run('MTE3MTk0NDYzMzUzODk3Nzg4Mg.Gj1ZNQ.jyhdG64dUEBJ3YrUxytTx4gc4UQeQIbKPTH-UI')
