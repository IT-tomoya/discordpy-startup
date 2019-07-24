from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send(ctx.content)
    
    
@client.event
async def on_ready():
    print('wake up')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

   


client.run("token")
#bot.run(token)
