import disnake
from disnake.ext import commands

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('\033[1m\033[31mМодуль\033[0m {} \033[1m\033[31mзагружается\033[0m'.format(self.__class__.__name__))

    # Информация о сервере
    @commands.slash_command(description="Информация о серверре!")
    async def serverinfo(self, ctx):
        bots = len(([member for member in ctx.guild.members if member.bot]))
        embed = disnake.Embed(
            description=f'**{ctx.guild.name}**\n'
                        f'\n**Участники:**\n'
                        f':busts_in_silhouette: Всего: **{ctx.guild.member_count}**\n'
                        f':bust_in_silhouette: Людей: **{ctx.guild.member_count - bots}**\n'
                        f':robot: Ботов: **{bots}**\n'
                        f'\n**Каналы:**\n'
                        f':speech_balloon: Текствые: **{len(ctx.guild.text_channels)}**\n'
                        f':mega: Голосовые: **{len(ctx.guild.voice_channels)}**\n'
                        f':books: Категории: **{len(ctx.guild.categories)}**\n'
                        f'\n**Владелец:**\n'
                        f'{ctx.guild.owner}\n'
                        f'\n**Уровень проверки:**\n'
                        f'{ctx.guild.verification_level}\n'
                        f'**Дата создания:**\n{ctx.guild.created_at.strftime("%d.%m.%Y")}\n',
            color=0x2f3136, )
        embed.set_footer(text=f'ID: {ctx.guild.id}')
        await ctx.send(embed=embed)

    # Информация о ролях пользователя

    @commands.slash_command(description="Информация о ролях!")
    async def roles(self, ctx, member: disnake.Member = None, guild: disnake.Guild = None):
        if member == None:
            userPrefix = ctx.message.author
        else:
            userPrefix = member

        member_roles = userPrefix.roles
        member_roles.pop(0)
        member_roles.reverse()
        x = ''
        for i in member_roles:
            element = str(i.id)
            result = f'<@&{element}>'
            if len(member_roles) <= 5:
                x += f'{result}\n'
            else:
                x += f'- {result} -'

        embed = disnake.Embed(
            description=f"{userPrefix.mention} список ролей:\n\n{x}",
            color=0x2f3136, )
        await ctx.send(embed=embed)

    # Информация о пользователя

    @commands.slash_command(description="Информация о пользователе!")
    async def userinfo(self, ctx, member: disnake.Member = None, guild: disnake.Guild = None):
        if not member:
            member = ctx.message.author

        t = member.status
        if t == disnake.Status.online:
            d = ":green_circle: В сети"
        if t == disnake.Status.offline:
            d = ":black_circle: Не в сети"
        if t == disnake.Status.idle:
            d = ":crescent_moon: Не активен"
        if t == disnake.Status.dnd:
            d = ":no_entry: Не беспокоить"

        value1 = member.activity

        embed = disnake.Embed(
            description=f'**Информация о пользователе**\n'
                        f'\n**Имя: **{member.display_name}\n'
                        f'**Статус: **{d}\n'
                        f'**Роль на сервере: **{member.top_role.mention}\n'
                        f'**Дата создания: **{member.created_at.strftime("%d.%m.%Y")}\n',
            color=0x2f3136, )
        embed.set_footer(text=f'ID: {member.id}')
        await ctx.send(embed=embed)

    # Аватарка пользователя

    @commands.slash_command(description="Авторочка пользователя!")
    async def avatar(self, ctx, member: disnake.Member = None):
        if member == None:
            userPrefix = ctx.message.author
        else:
            userPrefix = member

        emb = disnake.Embed(
            title=f"Аватарка пользователя {userPrefix.display_name}", color=0x2f3136)
        await ctx.send(embed=emb)
        
def setup(bot):
    bot.add_cog(Info(bot))