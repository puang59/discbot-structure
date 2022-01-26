import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix="w!", case_insensitive=True)

@bot.event
async def status_task():
    while True:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('Use w!help'))
        await asyncio.sleep(50)
        await bot.change_presence(status=discord.Status.online, activity=discord.Game('WeenPoint Admins'))
        await asyncio.sleep(50)

@bot.event
async def on_ready():
    print('Bot is Online')
    bot.loop.create_task(status_task())

@bot.command()
async def test(ctx):
    embed = discord.Embed(
        description = f"I am online {ctx.author.mention}!",
        colour = discord.Colour.green()  
    )
    await ctx.send(embed=embed)
 
bot.run("...")
