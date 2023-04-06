"""Importing The Necessary Modules"""
iimport discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        """Defining Intents"""
        intents = discord.Intents().all()

        """Defining our bot's prefix and passing the intents"""
        super().__init__(command_prefix=commands.when_mentioned_or('#'), intents=intents)

    async def on_ready(self):
        """Printing a message when our bot comes online"""
        print(f'Logged in as {self.user} ({self.user.id})')

bot = Bot()

"""Syncing the command to our bot"""
@bot.command()
"""Checking if the user has kick_members permission"""
@commands.has_permissions(kick_members=True)
"""Defining command's name and parameters"""
async def ban(ctx, member: discord.Member, *, reason=None):
    """Kicks the member from the guild"""
    await member.kick(reason=reason)
    """Responds with a follow-up message containing who was kicked and why"""
    await ctx.send(f'{member.name} has been kicked from the server. Reason: {reason}')

@ban.error
async def ban_error(ctx, error):
    """Error handler for the ban command"""
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have permission to kick members.')

# Run the bot
bot.run('your_bot_token_here')
