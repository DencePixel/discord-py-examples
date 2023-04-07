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

@bot.event
async def on_message(message):
    # Check if the message was sent by the bot itself
    if message.author == bot.user:
        return

    # Check if the message content contains a specific keyword
    if "hello" in message.content.lower():
        # Send a reply to the channel where the message was sent
        await message.channel.send("Hello, there!")


# Run the bot
bot.run('your_bot_token_here')
