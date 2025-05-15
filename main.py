import discord
from discord.ext import commands
from functions import sifre_olusturucu
from functions import emoji_olusturucu
from functions import yazi_tura

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

komutlar="""$merhaba: Bot selam verir.
$bye: Bot gitmenize tepki olarak bir emoji gönderir.
$sifre_olustur: Bot 15 karakter uzunluğunda rastgele bir şifre oluşturur.
$random_emoji: Bot rastgele bir emoji gönderir.
$yazi_tura: Bot yazı tura atar.
"""


@client.event
async def on_ready():
    print(f'We logined as {client.user}')

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
    elif message.content.startswith("$yardim"):
        await message.channel.send(komutlar)
    else:
        await message.channel.send(message.content)

client.run("TOKEN")
