import os
import discord
from discord.ext import commands
from helpers.utils import pick_name
from helpers.logging_config import logger, log_event
from dotenv import load_dotenv

# ENV
_ = load_dotenv()
auth_token = os.environ['discord_token']

# INTENTS
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# COMMANDS
@bot.command()
async def hello(ctx):
    """pb says hello when prompted"""
    log_event('INFO','bot command invoked by user', user=str(ctx.author), command='hello')
    await ctx.send('hellooo there!')

# EVENTS
@bot.event
async def on_ready():
    """pbot logs on"""
    log_event('INFO', 'logged in as bot user', bot_user=str(bot.user.name))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands"))

@bot.event
async def on_message(message):
    """message is sent in a server channel."""
    channel_name = message.channel.name if hasattr(message.channel, 'name') else 'Unknown'
    channel_id = message.channel.id
    log_event('INFO', 'message received', 
              user=str(message.author), 
              channel_name=channel_name, 
              channel_id=channel_id, 
              message_content=message.content, 
              message_id=message.id)
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    """new member joins the server."""
    log_event('INFO', 'new member joined', user=str(member))
    
    channel = discord.utils.get(member.guild.channels, name='social')
    greeting = pick_name()
    if channel:
        await channel.send(f'welcome to the server {greeting}!')

@bot.event
async def on_reaction_add(reaction, user):
    """reaction is added to a message."""
    log_event('INFO', 'reaction added', 
              user=str(user), 
              reaction=str(reaction.emoji), 
              message_id=reaction.message.id)
# ERRORS
@hello.error
async def hello_error(ctx, error):
    log_event('ERROR', 'error in hello command', command='hello', error=str(error))
    await ctx.send('an error occurred :/')

# RUN
bot.run(auth_token)
