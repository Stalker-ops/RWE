import disnake
from disnake.ext import commands

options = [
    disnake.SelectOption(label="Доступ в немодерируемый чат", description="", emoji="<:117:1079332727192563772>"),
    disnake.SelectOption(label="Уведомление об ивентах", description="", emoji="<:116:1079332723803566172>"),
    disnake.SelectOption(label="Уведомление о трансляциях", description="", emoji="<:115:1079332721903542292>"),
    disnake.SelectOption(label="Очистить все роли", description=""),
]

class Link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('\033[1m\033[31mМодуль\033[0m {} \033[1m\033[31mзагружается\033[0m'.format(self.__class__.__name__))

def setup(bot):
    bot.add_cog(Link(bot))

class LinkView(disnake.ui.View):
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
        if select.values[0] == "Доступ в немодерируемый чат":
            role = guild.get_role(1088565914254966875)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1107953392531292160>!", ephemeral = True)
        elif select.values[0] == "Уведомление об ивентах":
            role = guild.get_role(1107953392531292160)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1088565942155481149>!", ephemeral = True)
        elif select.values[0] == "Уведомление о трансляциях":
            role = guild.get_role(1088565859653533826)
            await user.add_roles(role)
            await interaction.response.send_message(f"Вам выдана роль <@&1088565859653533826>!", ephemeral = True)
        elif select.values[0] == "Очистить все роли":
            role1 = guild.get_role(1088565914254966875)
            role2 = guild.get_role(1088565942155481149)
            role3 = guild.get_role(1088565859653533826)
            await user.remove_roles(role1)
            await user.remove_roles(role2)
            await user.remove_roles(role3)
            await interaction.response.send_message(f"У вас были сняты все роли!", ephemeral = True)