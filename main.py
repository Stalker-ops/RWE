import disnake
from disnake.ext import commands
import os
from config import *
from SelectBuilder import SelectSets



class SetsBot(commands.InteractionBot):
    def __init__(self):
        self.persistent_views_added = False
        super().__init__(
            intents=disnake.Intents.all()
        )
    
    async def on_ready(self):
        if not self.persistent_views_added:
            self.add_view(SelectSets())
            self.persistent_views_added = True
        print(f'Загружен: {self.user} (ID: {self.user.id})')
    
bot = SetsBot()

@bot.event
async def on_member_join(member):
    role = disnake.utils.get(member.guild.roles, id = 1106230782848139314) #unverife role
    await member.add_roles(role)

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(bot_config['token'])

