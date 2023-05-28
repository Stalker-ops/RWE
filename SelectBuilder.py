import disnake
from disnake.ext import commands
from ModalsBuilder import ModalsView

class SelectSets(disnake.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)
    
    @disnake.ui.select(
        custom_id='set',
        min_values=1,
        max_values=1,
        placeholder='Выберите необходимую должность',
        options=[
            disnake.SelectOption(
                label='Moderator',
                description='Подать заявку на пост Moderator',
                emoji='<a:dot:1079337710566772736>',
                value='moder'
            ),
            disnake.SelectOption(
                label='Support',
                description='Подать заявку на пост Support',
                emoji='<a:dot:1079337710566772736>',
                value='sup'
            ),
            disnake.SelectOption(
                label='TribuneMod',
                description='Подать заявку на пост TribuneMod',
                emoji='<a:dot:1079337710566772736>',
                value='tribune'
            ),
            disnake.SelectOption(
                label='Events Mod',
                description='Подать заявку на пост Events Mod',
                emoji='<a:dot:1079337710566772736>',
                value='events'
            ),
            disnake.SelectOption(
                label='Media',
                description='Подать заявку на пост Media',
                emoji='<a:dot:1079337710566772736>',
                value='media'
            ),
            disnake.SelectOption(
                label='Creative',
                description='Подать заявку на пост Creative',
                emoji='<a:dot:1079337710566772736>',
                value='creativ'
            ),
        ]
    )
    async def select_callback(self, select: disnake.ui.Select, inter):
        if inter.values[0] == 'moder':
            await inter.response.send_modal(modal=ModalsView('Moderator'))
        elif inter.values[0] == 'sup':
            await inter.response.send_modal(modal=ModalsView('Support'))
        elif inter.values[0] == 'tribune':
            await inter.response.send_modal(modal=ModalsView('TribuneMod'))
        elif inter.values[0] == 'events':
            await inter.response.send_modal(modal=ModalsView('EventsMod'))
        elif inter.values[0] == 'creativ':
            await inter.response.send_modal(modal=ModalsView('Creative'))
        elif inter.values[0] == 'media':
            await inter.response.send_modal(modal=ModalsView('Media'))
        else:
            pass