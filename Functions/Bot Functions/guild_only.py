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
# Decorator that ensures the command is only run in a guild (not a private message)
@commands.guild_only()
# Command function that will be executed when the command is called
async def guildonly(ctx):
    # Accessing the guild that the command was called in
    guild = ctx.guild
    # Sending a message to the channel where the command was used, displaying the name of the guild
    await ctx.send(f"This command was sent in the server '{guild.name}'.")

# Decorator that registers an error handler for the 'server_info' command
@guildonly.error
# Error handler function to be executed when an error occurs
async def guildonly_error(ctx, error):
    # Checking if the error is a 'NoPrivateMessage' error (i.e. the command was not sent in a guild)
    if isinstance(error, commands.NoPrivateMessage):
        # Sending an error message to the channel where the command was used, informing the user that the command can only be used in a guild
        await ctx.send("This command can only be used in a server.")


# Run the bot by providing the bot token
bot.run('your_bot_token_here')
