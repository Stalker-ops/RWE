import disnake
from disnake.ext import commands

options = [
    disnake.SelectOption(label="Dota 2", description="", emoji="<:118:1079332729998544979>"),
    disnake.SelectOption(label="Genshin impact", description="", emoji="<:113:1079332714135699556>"),
    disnake.SelectOption(label="Osu", description="", emoji="<:119:1079332732867461130> "),
    disnake.SelectOption(label="Valorant", description="", emoji="<:112:1079332712365686844>"),
    disnake.SelectOption(label="CS:GO", description="", emoji="<:114:1079332718074138685>"),
    disnake.SelectOption(label="Очистить все роли", description=""),
]

class Role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('\033[1m\033[31mМодуль\033[0m {} \033загружается\033'.format(self.__class__.__name__))

def setup(bot):
    bot.add_cog(Role(bot))

class RoleView(disnake.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @disnake.ui.select(
        min_values=1,
        max_values=1,
        placeholder="Выберите нужное",
        options=options,
    )
    async def select_callback(self, select, interaction):
        user = interaction.user
        guild = interaction.guild
        if select.values[0] == "Dota 2":
            role = guild.get_role(1104827603841458278)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1104827603841458278>!", ephemeral = True)
        elif select.values[0] == "Genshin impact":
            role = guild.get_role(1104827598774739044)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1104827598774739044>!", ephemeral = True)
        elif select.values[0] == "CS:GO":
            role = guild.get_role(1104827597520642169)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1104827597520642169>!", ephemeral = True)
        elif select.values[0] == "Valorant":
            role = guild.get_role(1104827600934817924)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1104827600934817924>!", ephemeral = True)
        elif select.values[0] == "Osu":
            role = guild.get_role(1104827605200425030)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1104827605200425030>!", ephemeral = True)
        elif select.values[0] == "Очистить все роли":
            role1 = guild.get_role(1104827603841458278)
            role2 = guild.get_role(1104827598774739044)
            role3 = guild.get_role(1104827597520642169)
            role4 = guild.get_role(1104827600934817924)
            role5 = guild.get_role(1104827605200425030)
            await user.remove_roles(role1)
            await user.remove_roles(role2)
            await user.remove_roles(role3)
            await user.remove_roles(role4)
            await user.remove_roles(role5)
            await interaction.response.send_message(f"У вас были сняты все роли!", ephemeral = True)