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

# A command that sends a message to a specific channel
@bot.command()  # A decorator to register a command
async def channel(ctx):
    channel = bot.get_channel(123456789)  # Replace with your channel ID
    await channel.send("I'm working!")
    await ctx.send("Message sent to the specified channel.")

# Run the bot by providing the bot token
bot.run('your_bot_token_here')
