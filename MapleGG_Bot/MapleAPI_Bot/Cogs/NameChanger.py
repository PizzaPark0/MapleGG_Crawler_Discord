import discord
from discord.ext import commands

import time

import mapleAPI_Request
import loadConfig

settings = loadConfig.Config()

class NameChanger(commands.Cog): #커맨드로 이름 변경
    def __init__(self, bot) -> None:
        self.bot = bot
        self.viewer = mapleAPI_Request.MapleAPI_Viewer(settings.api_key)

    @commands.command(name=settings.commandName1, pass_context=True)
    async def chnick(self, ctx, search_name):
        ocid = self.viewer.getCharOcid(search_name)
        date = f"{time.localtime().tm_year}-{time.localtime().tm_mon}-{time.localtime().tm_mday-1}"
        if len(ocid) != 32:
            await ctx.send(f'존재한 적이 없거나, 현재 사용하지 않는 이름입니다.')
            return

        basic = self.viewer.getCharData(ocid, date, "basic")
        dojang = self.viewer.getCharData(ocid, date, "dojang")
        stat = self.viewer.getCharData(ocid, date, "stat")
        popularity = self.viewer.getCharData(ocid, date, "popularity")

        attribute = {
            "name" : search_name,
            "class_name" : basic.get("character_class"),
            "world_name" : basic.get("world_name"),
            "level" : str(basic.get("character_level")),
            "guild" : basic.get("character_guild_name"),
            "popularity" : str(popularity.get("popularity")),
            "combat_power" : str(stat.get("final_stat")[-2].get("stat_value")),
            "dojang_floor" : str(dojang.get("dojang_best_floor"))
        }
                
        crawledName = self.formater(attribute)
        await ctx.message.author.edit(nick=crawledName)
        await ctx.send(f'{ctx.message.author} was changed for {ctx.message.author.mention} ')

    def formater(self, attribute):
        f = settings.nameFormat.split('/')
        return "/".join((attribute.get(i) for i in f))

async def setup(bot):
    await bot.add_cog(NameChanger(bot))
