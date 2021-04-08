from discord.ext import commands
import os
import traceback
import random
import discord

client = discord.Client()


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


    
guraindo1 = '', '中吉だ', '吉だ。', '半吉だ。', '半中吉だ。', '半大吉だ。', '凶だ。', '中凶だ。', '大凶だ。', '半凶だ。', '半中凶だ。', '半大凶だ。', '不明だ……。', '超絶大吉だ！'
@bot.command(name="運勢", pass_context=True)
async def kyouun(ctx):
    ran1 = random.choice(guraindo1)
    # await ctx.send("{}へ：今日の運勢だ。".format(ctx.message.author.name))
    await ctx.send(f"{ctx.message.author.name}へ：今日の運勢だ。\n{ran1}")
    
guraindo2 =  '5000万円', '１億円', '２億円', '３億円'
@bot.command(name="貧乏神チャンス", pass_context=True)
async def kyouun(ctx):
    ran2 = random.choice(guraindo2)
    # await ctx.send("{}へ：貧乏神ポイントは".format(ctx.message.author.name))
    await ctx.send(f"{ctx.message.author.name}へ：貧乏神ポイントは\n{ran2}")
    
guraindo3 =  '1000万円', '５０００万円', '１億円', '２億円'
@bot.command(name="ラッキーチャンスA", pass_context=True)
async def kyouun(ctx):
    ran3 = random.choice(guraindo3)
    # await ctx.send("{}へ：おそろポイントは。".format(ctx.message.author.name))
    await ctx.send(f"{ctx.message.author.name}へ：おそろポイントは\n{ran3}")
    

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
        
@bot.command()
async def pong(ctx):
    await ctx.send('ping')

@bot.command()
async def dice(ctx):
    await ctx.send('saikoro')    

bot.run(token)

