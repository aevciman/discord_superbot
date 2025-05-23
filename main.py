import discord
from discord.ext import commands
from functions import sifre_olusturucu, emoji_olusturucu, yazi_tura
import requests
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']

komutlar = """
$merhaba: Bot selam verir.
$bye: Bot gitmenize tepki olarak bir emoji gönderir.
$sifre_olustur: Bot 15 karakter uzunluğunda rastgele bir şifre oluşturur.
$random_emoji: Bot rastgele bir emoji gönderir.
$yazi_tura: Bot yazı tura atar.
$yardim: Komutları listeler.
$hello: Bot tanıtım mesajı gönderir.
$heh [sayı]: Belirtilen sayıda 'he' yazar.
"""

@bot.event
async def on_ready():
    print(f'Bot giriş yaptı: {bot.user}')

@bot.command()
async def merhaba(ctx):
    await ctx.send("Selam!")

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")  # 🙂

@bot.command()
async def sifre_olustur(ctx):
    await ctx.send(sifre_olusturucu(15))

@bot.command()
async def random_emoji(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def yazi_tura(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def yardim(ctx):
    await ctx.send(komutlar)

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command('ordek')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('kopek')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('tilki')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)

@bot.command("kirlilik")
async def kirlilik(ctx):
    klasor = "kirlilik_bilgileri"
    secilen = random.choice(os.listdir(klasor))
    tam_yol = os.path.join(klasor, secilen)

    with open(tam_yol, "r", encoding="utf-8") as dosya:
        icerik = dosya.read()
        await ctx.send(icerik)


bot.run("TOKEN")
