import asyncio 
import bot


@bot.command('test')
@bot.is_admin
async def testy(self,channel,nick,msg):
    await bot.message(self,'test',channel,'hi there')



async def init(self):
   pass

