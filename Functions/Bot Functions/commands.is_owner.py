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

# Decorator that registers a command
@bot.command()
# Decorator that ensures only the bot owner can use this command
@commands.is_owner()
# Command function that will be executed when the command is called by the bot owner
async def owner(ctx):
    # Sending a message to the channel where the command was used, informing the user that they are the bot owner
    await ctx.send("You are the bot owner.")

# Decorator that registers an error handler for the 'owner' command
@owner.error
# Error handler function to be executed when an error occurs
async def owner_error(ctx, error):
    # Checking if the error is a 'NotOwner' error (i.e. the command was not sent by the bot owner)
    if isinstance(error, commands.NotOwner):
        # Sending an error message to the channel where the command was used, informing the user that they are not the bot owner
        await ctx.send("You are not the bot owner.")




# Run the bot by providing the bot token
bot.run('your_bot_token_here')
