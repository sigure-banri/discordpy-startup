import discord
import sys


from func import  diceroll

TOKEN = '任意のトークン'

client = discord.Client()

@client.event
async def on_ready():
    print('--------------')
    print('ログインしました')
    print(client.user.name)
    print(client.user.id)
    print('--------------')
    channel = client.get_channel('チャンネルID')
    await channel.send('楽しいTRPGを始めましょう！')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("!dice"):
      
        say = message.content 

       
        order = say.strip('!dice ')
        cnt, mx = list(map(int, order.split('d'))) 
        dice = diceroll(cnt, mx) 
        await message.channel.send(dice[cnt])
        del dice[cnt]

      
        await message.channel.send(dice)

client.run(TOKEN)
