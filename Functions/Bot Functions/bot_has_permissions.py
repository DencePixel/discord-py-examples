import discord  # Importing the discord module
from discord.ext import commands  # Importing the commands submodule from the discord.ext module

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

@bot.command()  # Decorator to register a new command with the bot
@commands.bot_has_permissions(manage_channels=True)  # Decorator that restricts the usage of the command to bots with the 'manage_channels' permission
async def permissions(ctx):  # Command function to be executed when the command is called
    await ctx.send("The bot has manage_channels permissions")  # Sending a message to the channel where the command was used

@permissions.error  # Decorator to register an error handler for the 'permissions' command
async def channel_error(ctx, error):  # Error handler function to be executed when an error occurs
    if isinstance(error, commands.BotMissingPermissions):  # Checking if the error is a BotMissingPermissions error
        await ctx.send("The bot does not have manage_channels permissions")  # Sending an error message to the channel where the command was used

# Run the bot by providing the bot token
bot.run('your_bot_token_here')
