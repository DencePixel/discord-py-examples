import discord
from discord.ext import commands
from discord import app_commands
import discord.ext
from discord import Color


class Lock(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
        self.locked_emoji = '🔒'  # store the locked emoji for later use
        self.unlocked_emoji = '🔓'  # store the unlocked emoji for later use
        self.locked_message = None  # initialize locked message to None

    @app_commands.command(name="lock", description="Lock a channel")
    async def lock(self, interaction: discord.Interaction, *, reason: str = None):
        channel = interaction.channel
        if interaction.guild.get_member(interaction.user.id).guild_permissions.manage_channels:
            await interaction.response.send_message(f"Succesfully locked {channel.mention}", ephemeral=True)
            self.locked_message = await interaction.followup.send(self.locked_emoji)
            await channel.set_permissions(interaction.guild.default_role, send_messages=False)
        else:
            await interaction.response.send_message("You do not have permission to lock channels.", ephemeral=True)

    @app_commands.command(name="unlock", description="Unlock a channel")
    async def unlock(self, interaction: discord.Interaction, *, reason: str = None):
        channel = interaction.channel
        if interaction.guild.get_member(interaction.user.id).guild_permissions.manage_channels:
            if self.locked_message is not None:  # check if locked message exists
                await interaction.response.send_message(f"Succesfully unlocked {channel.mention}", ephemeral=True)
                await self.locked_message.edit(content=self.unlocked_emoji)  # replace locked emoji with unlocked emoji
                await channel.set_permissions(interaction.guild.default_role, send_messages=True)
            else:
                await interaction.response.send_message("Channel is not locked.", ephemeral=True)
        else:
            await interaction.response.send_message("You do not have permission to unlock channels.", ephemeral=True)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Lock(client))
