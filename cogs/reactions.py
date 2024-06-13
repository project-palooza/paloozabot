import discord
from discord.ext import commands
from helpers.logging_config import log_event

class Reactions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        """reaction is added to a message."""
        log_event('INFO', 'reaction added', 
                  user=str(user), 
                  reaction=str(reaction.emoji), 
                  message_id=reaction.message.id)
        # Additional logic for handling reactions in #open-issues
        channel = reaction.message.channel
        if str(channel) == "open-issues":
            first_reaction = reaction.message.reactions[0]
            if first_reaction.count == 1:
                thread = await reaction.message.create_thread(name="Issue Discussion")
                await thread.send(f"@{user.display_name} claims this issue!")
                log_event('INFO', 'issue claimed', 
                          user=str(user), 
                          message_id=reaction.message.id)

def setup(bot):
    bot.add_cog(Reactions(bot))