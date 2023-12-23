import discord
from discord.ext import commands

import os
import sys
sys.path.insert(1, f"{os.path.abspath(os.path.dirname(__file__))}/Cogs/crawlModule")
import loadConfig

token = os.getenv('TOKEN')
bot = commands.Bot(command_prefix=loadConfig.Config().c_prefix, intents=discord.Intents().all())  # 봇의 접두사 설정
# cogs 폴더의 절대 경로 얻기
# Pycharm에서 바로 상대 경로를 사용하면 오류가 발생하기 때문에 따로 절대경로를 얻어야한다.
abs_cogs_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "Cogs")

# cogs 폴더에 존재하는 cogs(.py파일) 로드
async def load():
  for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        await bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():  # 봇 준비 시 1회 동작하는 부분
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("반갑습니다 :D")) # 봇 이름 하단에 나오는 상태 메시지 설정
    await load()
    print("Bot is ready")

bot.run(loadConfig.Config().bot_token)