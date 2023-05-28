import disnake
from disnake.ext import commands
from cogs.role import RoleView
from cogs.link import LinkView
from SelectBuilder import SelectSets
from EmbedBuilder import SetsAnnounce
from EmbedBuilder import SetsAnnounce1
from EmbedBuilder import SetsRole
from EmbedBuilder import SetsLink

class SetsCommand(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Отправить ембед с наборами')
    async def send_sets(inter, channelid: disnake.TextChannel):
        channel = disnake.utils.get(inter.guild.text_channels, id=int(channelid.id))
        await channel.send(embed=SetsAnnounce())
        await channel.send(embed=SetsAnnounce1(), view=SelectSets())

    @commands.slash_command(description='Отправить ембед с ролями')
    async def send_role(inter, channelid: disnake.TextChannel):
        channel = disnake.utils.get(inter.guild.text_channels, id=int(channelid.id))
        await channel.send(embed=SetsRole(), view=RoleView())

    @commands.slash_command(description='Отправить ембед с ролями уведомлений')
    async def send_link(inter, channelid: disnake.TextChannel):
        channel = disnake.utils.get(inter.guild.text_channels, id=int(channelid.id))
        await channel.send(embed=SetsLink(), view=LinkView())
    
    @commands.slash_command(description='Назначить всем участникам роль unverify')
    async def unverof(self, ctx, role_id: int):
        unverify_role = disnake.utils.get(ctx.guild.roles, id=role_id)

        if unverify_role is None:
            # Создаем новую роль, если ее еще нет
            unverify_role = await ctx.guild.create_role(id=role_id, name='unverify', reason='Роль для неверифицированных участников')

        member_count = 0

        # Получаем список всех участников на сервере
        members = ctx.guild.members

        # Проверяем, есть ли роль unverify у участника
        for member in members:
            if unverify_role not in member.roles:
                # Если у участника нет роли unverify, добавляем ее
                await member.add_roles(unverify_role)
                member_count += 1

        await ctx.send(f'Роль "{unverify_role.name}" была назначена {member_count} участникам на сервере.')
def setup(bot):
    bot.add_cog(SetsCommand(bot))