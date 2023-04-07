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

@bot.command()  # defines a new command
@commands.cooldown(1, 60, commands.BucketType.user)  # sets a 60-second cooldown for each user
async def cooldown(ctx):  # coroutine function that represents the cooldown command
    await ctx.send("This command has a 60 second cooldown.")  # sends a message to the channel

@cooldown.error  # error handler for the cooldown command
async def cooldown_error(ctx, error):  # coroutine function that handles errors for the cooldown command
    if isinstance(error, commands.CommandOnCooldown):  # checks if the error is due to a cooldown
        seconds = round(error.retry_after)  # calculates the remaining seconds until the command can be used again
        await ctx.send(f"You must wait {seconds} seconds before using this command again.")  # sends an error message to the channel


# Run the bot by providing the bot token
bot.run('your_bot_token_here')
