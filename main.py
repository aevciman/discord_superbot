import discord
from functions import sifre_olusturucu
from functions import emoji_olusturucu
from functions import yazi_tura

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("$sifre_olustur"):
        await message.channel.send(sifre_olusturucu(15))
    elif message.content.startswith("$random_emoji"):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith("$yazi_tura"):
        await message.channel.send(yazi_tura())
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
