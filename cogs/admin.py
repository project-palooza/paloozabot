import discord
from discord.ext import commands
from helpers.logging_config import log_event

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """pb says hello when prompted"""
        log_event('INFO','bot command invoked by user', user=str(ctx.author), command='hello')
        await ctx.send('hellooo there!')

    @hello.error
    async def hello_error(self, ctx, error):
        log_event('ERROR', 'error in hello command', command='hello', error=str(error))
        await ctx.send('an error occurred :/')

def setup(bot):
    bot.add_cog(Admin(bot))