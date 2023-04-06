import discord
from discord.ext import commands

class ColorDropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Red', description='Red!', emoji='🟥'),
            discord.SelectOption(label='Green', description='Green!', emoji='🟩'),
            discord.SelectOption(label='Blue', description='Blue', emoji='🟦'),
        ]


        super().__init__(placeholder='Choose a color.', min_values=1, max_values=1, options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'You selected the color {self.values[0]}')


class ColorDropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(ColorDropdown())



@bot.command()
async def colour(ctx):
    view = ColorDropdownView()
    await ctx.send('Pick a colour:', view=view)
