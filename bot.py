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

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from helpers.logging_config import logger

# ENV
_ = load_dotenv()
auth_token = os.environ['discord_token']

# INTENTS
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# COGS
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# RUN
bot.run(auth_token)