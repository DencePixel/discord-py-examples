import discord
from discord.ext import commands


class RoleSelection(discord.ui.RoleSelect):
    def __init__(self, guild_Roles):
        super().__init__(placeholder='Select a role!', max_values=1, min_values=1)
        self.guild_roles = guild_Roles

    async def callback(self, interaction: discord.Interaction):
        role_id = int(self.values[0].id)
        role = interaction.guild.get_role(role_id)
        guild_id = interaction.guild.id
        await interaction.response.send_message(f"Looks like you picked {role.mention}!")


class RoleSelectionView(discord.ui.View):
    def __init__(self, guild_Roles):
        super().__init__(placeholder='Select a role!', max_values=1, min_values=1)
        self.add_item(RoleSelection(guild_Roles))


@client.command(name="role")
async def role(ctx):
    view = RoleSelectionView(guild_Roles=ctx.guild.roles)
    await ctx.send(f"What role will you pick?", view=view)
