# imports
import logging
import os
import discord
from discord.ext import commands
from utils import pick_name
from dotenv import load_dotenv
# env
_ = load_dotenv()
auth_token = os.environ['discord_token']
# logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(module)s:%(lineno)d:%(funcName)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    handlers=[
                        logging.FileHandler('paloozabot.log'),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('discord')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# COMMANDS

@bot.command()
async def hello(ctx):
    """pb says hello when prompted"""
    logger.info(f'{ctx.author} invoked hello command')
    await ctx.send('hellooo there!')

# EVENTS

@bot.event
async def on_ready():
    """pbot logs on"""
    logger.info(f'logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands"))

@bot.event
async def on_message(message):
    """message is sent in a server channel."""
    channel_name = message.channel.name if hasattr(message.channel, 'name') else 'Unknown'
    channel_id = message.channel.id
    logger.info(f'Message from {message.author} in #{channel_name} (ID: {channel_id}): {message.content}, Message ID: {message.id}')

    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    """new member joins the server."""
    logger.info(f'{member} joined the server')
    
    channel = discord.utils.get(member.guild.channels, name='social')
    greeting = pick_name()
    if channel:
        await channel.send(f'welcome to the server {greeting}!')

@bot.event
async def on_reaction_add(reaction, user):
    """reaction is added to a message."""
    logger.info(f'{user} added {reaction.emoji} to message ID {reaction.message.id}: {reaction.message.content}')

# ERRORS

@hello.error
async def hello_error(ctx, error):
    logger.error(f'error in hello command: {error}')
    await ctx.send('an error occurred :/')


# RUN

bot.run(auth_token)
