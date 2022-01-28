import discord 
from discord.ext import commands 

bot = commands.Bot(command_prefix="w!", case_insensitive=True)

@bot.event
async def on_ready():
    print('Bot is Online')

@bot.command()
async def test(ctx):
    embed = discord.Embed(
        description = f"I am online {ctx.author.mention}!",
        colour = discord.Colour.green()  
    )
    await ctx.send(embed=embed)
 
bot.run("...")
