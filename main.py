import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Привет! Меня зовут {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    memes = os.listdir('memes')
    img_name = random.choice(memes)
    with open(f'memes/{img_name}', 'rb') as f:
            picture = discord.File(f)

@bot.command()
async def gen_advice():
    advice = ["Экономьте ресурсы", "Раздяляйте мусор", "Сдавайте второсырье", "Выбирайте ECO Транспорты", "Обратите внимание на питание"]
    await random.choice(emodji)

    await ctx.send(file=picture)

bot.run("ВСТАВЬТЕ СЮДА СВОЙ ТОКЕН")
