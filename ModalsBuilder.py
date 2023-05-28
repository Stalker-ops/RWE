import disnake
from disnake.ext import commands
from EmbedBuilder import SetsEmbed
from config import channels_config

class ModalsView(disnake.ui.Modal):
    def __init__(self, one):
        self.one = one
        components = [
            disnake.ui.TextInput(
                label="ИМЯ, ВОЗРАСТ (15+)", 
                placeholder="Например: Максим, 15 лет", 
                custom_id="nameage", 
                max_length=20,
            ),
            disnake.ui.TextInput(
                label="СКОЛЬКО ВЫ МОЖЕТЕ УДЕЛЯТЬ ВРЕМЕНИ", 
                placeholder="Например: с 14:00 до 18:00", 
                custom_id="primetime", 
                max_length=20,
            ),
            disnake.ui.TextInput(
                label=f"ПОЧЕМУ ИМЕННО ТЫ ДОЛЖЕН СТАТЬ {one}?", 
                placeholder="Например: Я активно сижу в дискорде", 
                custom_id="pochemu", 
                style=disnake.TextInputStyle.paragraph,
                max_length=100,
            ),
            disnake.ui.TextInput(
                label="РАБОТАЛИ ЛИ РАНЕЕ В ДАННОЙ СФЕРЕ?", 
                placeholder="Например: Ещё нет", 
                custom_id="workbefore", 
                max_length=20,
            ),
            disnake.ui.TextInput(
                label="РАССКАЖИ О СВОИХ ХОРОШИХ ЧЕРТАХ ХАРАКТЕРА", 
                placeholder="Например: Я добрый, честный)", 
                custom_id="characterfield", 
                style=disnake.TextInputStyle.paragraph,
                max_length=100,
            ),
        ]
        super().__init__(title=f"Заявка на {one}", components=components)

    async def callback(self, interaction) -> None:
        if self.one == 'Moderator':
            channel_id = channels_config.get('moder', None)
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one))
                await interaction.response.send_message('Заявка отправлена!', ephemeral=True)
            else:
                await interaction.response.send_message('Канал не найден.', ephemeral=True)
                
        if self.one == 'Support':
            channel_id = channels_config.get('supp', None)
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one))
                await interaction.response.send_message('Заявка отправлена!', ephemeral=True)
            else:
                await interaction.response.send_message('Канал не найден.', ephemeral=True)
                
        if self.one == 'TribuneMod':
            channel_id = channels_config.get('tribun', None)
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one))
                await interaction.response.send_message('Заявка отправлена!', ephemeral=True)
            else:
                await interaction.response.send_message('Канал не найден.', ephemeral=True)
                
        if self.one == 'EventsMod':
            channel_id = channels_config.get('events', None)
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one))
                await interaction.response.send_message('Заявка отправлена!', ephemeral=True)
            else:
                await interaction.response.send_message('Канал не найден.', ephemeral=True)
                
        if self.one == 'Creative':
            channel_id = channels_config.get('creativ', None)
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one))
                await interaction.response.send_message('Заявка отправлена!', ephemeral=True)
            else:
                await interaction.response.send_message('Канал не найден.', ephemeral=True)
                
        if self.one == 'Media':
            channel_id = channels_config.get('media', None)
            channel = None
            if channel_id is not None:
                channel = disnake.utils.get(interaction.guild.text_channels, id=channel_id)
            if channel is not None:
                await channel.send(f'<@{interaction.author.id}>', embed=SetsEmbed(interaction,self.one))
                await interaction.response.send_message('Заявка отправлена!', ephemeral=True)
            else:
                await interaction.response.send_message('Канал не найден.', ephemeral=True)