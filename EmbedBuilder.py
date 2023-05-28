import disnake
from disnake.ext import commands
import datetime
from disnake import ui

class SetsEmbed(disnake.Embed):
    def __init__(self, interaction, two):
        self.interaction = interaction
        self.two = two
        super().__init__(
            title=f'Пользователь подал заявку на роль {two}',
            description=f'ID: **{interaction.author.id}**\nПользователь: **{interaction.author.name}**\n',
            color=disnake.Color.from_rgb(47, 49, 54),
        )
        self.add_field(name='Имя, Возраст', value=f'{interaction.text_values["nameage"]}')
        self.add_field(name='Сколько вы времени можете уделять серверу?', value=f'{interaction.text_values["primetime"]}', inline=False)
        self.add_field(name=f'Почему именно ты должен стать {two}?', value=f'{interaction.text_values["pochemu"]}', inline=False)
        self.add_field(name='Работали ли ранее в данной сфере?', value=f'{interaction.text_values["workbefore"]}', inline=False)
        self.add_field(name='Расскажи о своих хороших чертах характера', value=f'{interaction.text_values["characterfield"]}', inline=False)


class SetsAnnounce(disnake.Embed):
    def __init__(self):
        super().__init__(
            description=(
                ''
            ),
            color=disnake.Color.from_rgb(47, 49, 54),
        )
        self.set_image(url='https://media.discordapp.net/attachments/1027264051459395666/1088555785027588176/Group_348.png?width=470&height=221')
        
class SetsAnnounce1(disnake.Embed):
    def __init__(self):
        super().__init__(
            description=(
                ''
            ),
            color=disnake.Color.from_rgb(47, 49, 54),
        )
        self.set_image(url='https://media.discordapp.net/attachments/1027264051459395666/1088555784729796718/Group_347.png?width=470&height=221')

class SetsRole(disnake.Embed):
    def __init__(self):
        super().__init__(
            title='Игровые роли',
            description=(
            ' Ты можешь получить **игровые роли**, чтобы быстрее найти себе **тиммейтов**. Для этого **выбери роли** из списка ниже.'
            ),
            color=disnake.Color.from_rgb(47, 49, 54),
        )
        self.set_image(url='')


class SetsLink(disnake.Embed):
    def __init__(self):
        super().__init__(
            title='Уведомления',
            description=(
            ' **Получи роли** уведомлений о событиях, которые **ты бы не хотел** пропускать. Для этого **выбери роли** из списка ниже.'
            ),
            color=disnake.Color.from_rgb(47, 49, 54),
        )
        self.set_image(url='')