import discord
from discord.ext import commands

class ChannelSelection(discord.ui.ChannelSelect):
    def __init__(self, guild_channels):
        super().__init__(placeholder='Pick a channel!.', max_values=1, min_values=1)
        self.guild_channels = guild_channels

    async def callback(self, interaction: discord.Interaction):
        channel_id = int(self.values[0].id)
        channel = interaction.guild.get_channel(channel_id)
        guild_id = interaction.guild.id
        await interaction.followup.send(f"You picked {channel.mention}!")



class LoggingChannelDropdownView(discord.ui.View):
    def __init__(self, guild_channels):
        super().__init__()
        self.add_item(ChannelSelection(guild_channels))

@client.command()
async def channel(ctx):
    view = LoggingChannelDropdownView(guild_channels=ctx.guild.channels)
    await ctx.send("What channel will you pick?", view=view)
