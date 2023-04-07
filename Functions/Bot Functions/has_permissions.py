# Importing The Necessary Modules
import discord
from discord.ext import commands

# Defining a subclass of commands.Bot
class Bot(commands.Bot):
    def __init__(self):
        # Defining Intents
        intents = discord.Intents().all()

        # Defining our bot's prefix and passing the intents
        super().__init__(command_prefix=commands.when_mentioned_or('#'), intents=intents)

    # An event handler that is called when the bot is ready
    async def on_ready(self):
        # Printing a message when our bot comes online
        print(f'Logged in as {self.user} ({self.user.id})')

# Creating an instance of our bot
bot = Bot()

@bot.command()
@commands.has_permissions(manage_channels=True)
async def permissions(ctx):
    await ctx.send("You have manage_channels permissions")
    
@permissions.error
async def channel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have manage_channels permissions")


# Run the bot by providing the bot token
bot.run('your_bot_token_here')
