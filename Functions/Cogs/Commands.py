import discord
from discord.ext import commands

class CogCommand(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(name="test1")
    async def test(self, ctx):
        await ctx.send(f"I am inside a cog! {ctx.author.mention}")
    
        
async def setup(client: commands.Bot) -> None:
    await client.add_cog(CogCommand(client)) # Registering The Command # 
    
"""All commands must take a self parameter to allow usage of instance attributes that can be used to maintain state."""
