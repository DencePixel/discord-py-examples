import discord
from discord.ext import commands

class RoleSelection(discord.ui.RoleSelect):
    def __init__(self, guild_Roles):
        super().__init__(placeholder='Select a role!', max_values=1, min_values=1)# Contains the placeholder text which appears on top of the dropdown when not selected, min_values means the minimum amount of roles they need to select, man_values is the maximum amount of roles they can select.
        self.guild_roles = guild_Roles

    async def callback(self, interaction: discord.Interaction):
        role_id = int(self.values[0].id)
        role = interaction.guild.get_role(role_id)
        guild_id = interaction.guild.id
        await interaction.response.send_message(f"Looks like you picked {role.mention}!")

@client.command(name="role")
async def role(ctx):
    RoleSelection_Dropdown = RoleSelection(ctx.guild.channels)
    RoleSelection_View = discord.ui.View()
    RoleSelection_View.add_item(RoleSelection_Dropdown)
    await ctx.send(f"What role will you pick?", view=RoleSelection_View)

# How To Use In A Cog #
import discord
from discord.ext import commands

class RoleSelection(discord.ui.RoleSelect):
    def __init__(self, guild_Roles):
        super().__init__(placeholder='Select a role!', max_values=1, min_values=1)# Contains the placeholder text which appears on top of the dropdown when not selected, min_values means the minimum amount of roles they need to select, man_values is the maximum amount of roles they can select.
        self.guild_roles = guild_Roles

    async def callback(self, interaction: discord.Interaction):
        role_id = int(self.values[0].id)
        role = interaction.guild.get_role(role_id)
        guild_id = interaction.guild.id
        await interaction.response.send_message(f"Looks like you picked {role.mention}!")


class RoleSelection(discord.ui.RoleSelect):
    def __init__(self, guild_Roles):
        super().__init__(placeholder='Select a role!', max_values=1, min_values=1)
        self.guild_roles = guild_Roles

    async def callback(self, interaction: discord.Interaction):
        role_id = int(self.values[0].id)
        role = interaction.guild.get_role(role_id)
        guild_id = interaction.guild.id
        await interaction.response.send_message(f"You selected the {role.mention}")

class Role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="role")
    async def role(self, ctx):
        RoleSelection_Dropdown = RoleSelection(ctx.guild.channels)
        RoleSelection_View = discord.ui.View()
        RoleSelection_View.add_item(RoleSelection_Dropdown)
        await ctx.send(f"What role will you pick?", view=RoleSelection_View)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(Role(client))
