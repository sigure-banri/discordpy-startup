from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def aabb(ctx):
    await ctx.send('1')
    
@bot.command()
async def aabb(ctx):
    await ctx.send('2')
    
    @bot.command()
async def diece(ctx):
    await ctx.send('3')
    
@bot.command()
async def pong(ctx):
    await ctx.send('ping')

@bot.command()
async def dice(ctx):
    await ctx.send('saikoro')    

bot.run(token)

