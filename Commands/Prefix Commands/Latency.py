"""Importing The Necessary Modules"""
import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):

        """Defining Intents And Stating What Intents We Need"""
        intents = discord.Intents.default()
        intents.message_content = True

        """Defining our bots prefix and passing the intents"""
        super().__init__(command_prefix=commands.when_mentioned_or('#'), intents=intents)

    async def on_ready(self):
        """Printing a message when our bot comes online"""
        print(f'Logged in as {self.user} ({self.user.id})')

bot = Bot()

"""Creating A Command"""
@bot.command()
"""Defining the command name and parameters"""
async def latency(ctx):
    """Sending the message containing the client's latency/ping"""
    await ctx.send(f"Pong! I replied to your message in {round(bot.latency * 1000)}ms")


"""After we run the file this logs into the bot, triggering the on_ready function"""
bot.run('token')
