import discord
from discord.ext import commands
from helpers.logging_config import log_event
from helpers.utils import pick_name

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """pbot logs on"""
        log_event('INFO', 'logged in as bot user', bot_user=str(self.bot.user.name))
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands"))

    @commands.Cog.listener()
    async def on_message(self, message):
        """message is sent in a server channel."""
        channel_name = message.channel.name if hasattr(message.channel, 'name') else 'Unknown'
        channel_id = message.channel.id
        log_event('INFO', 'message received', 
                  user=str(message.author), 
                  channel_name=channel_name, 
                  channel_id=channel_id, 
                  message_content=message.content, 
                  message_id=message.id)
        await self.bot.process_commands(message)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """new member joins the server."""
        log_event('INFO', 'new member joined', user=str(member))
        
        channel = discord.utils.get(member.guild.channels, name='social')
        greeting = pick_name()
        if channel:
            await channel.send(f'welcome to the server {greeting}!')

def setup(bot):
    bot.add_cog(Events(bot))