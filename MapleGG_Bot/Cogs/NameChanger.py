import discord
from discord.ext import commands
import maplegg_crawl

class NameChanger(commands.Cog): #커맨드로 이름 변경
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name='이름변경', pass_context=True)
    async def chnick(self, ctx, search_name):
        crawler = maplegg_crawl.MapleGG_Crawler()
        crawled_data = crawler.searchNickname(search_name)
        
        if crawled_data == 0:
            await ctx.send(f'존재한 적이 없는 이름입니다.')

        elif (crawled_data.get("world_rank")=="(정보없음)"): #이름 바꾼 사람은 현재 랭킹 말소됨
            await ctx.send(f'현재 사용하지 않는 이름입니다.')
        
        else:
            crawledName = f"{crawled_data.get('nickname')}/{crawled_data.get('MuLung_floor')}/{crawled_data.get('char_class')}"
            await ctx.message.author.edit(nick=crawledName)
            await ctx.send(f'{ctx.message.author} was changed for {ctx.message.author.mention} ')

async def setup(bot):
    await bot.add_cog(NameChanger(bot))
