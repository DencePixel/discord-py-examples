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

# Decorator that registers a new command with the bot
@bot.command()
# Decorator that ensures the command can only be run in a NSFW channel
@commands.is_nsfw()
# Command function that will be executed when the command is called
async def nsfw_command(ctx):
    # Sending a message to the channel where the command was used, indicating that the command was run in an NSFW channel
    await ctx.send("I was run in an NSFW channel.")

# Decorator that registers an error handler for the 'nsfw_command' command
@nsfw_command.error
# Error handler function to be executed when an error occurs
async def nsfw_command_error(ctx, error):
    # Checking if the error is a 'NSFWChannelRequired' error (i.e. the command was not run in an NSFW channel)
    if isinstance(error, commands.NSFWChannelRequired):
        # Sending an error message to the channel where the command was used, informing the user that the command can only be used in an NSFW channel
        await ctx.send("NSFW CHANNELS ONLY")





# Run the bot by providing the bot token
bot.run('your_bot_token_here')
