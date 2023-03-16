import discord
from discord import app_commands
from discord.ext import commands

from lib.config import config

class Util(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "new_order",
        description = "Create a new group order",
    )
    async def new_order(self, interaction: discord.Interaction, website: str = None):
        role = get(interaction.guild.roles, name = 'RotorJacket')
        if role not in interaction.user.roles:
            await interaction.response.send_message('You must be a RotorJacket to create a group order')
        else:
            channel = get(interaction.guild.text_channels, name = "shipping-sharing")
            if website == None:
                await channel.create_thread(name = f"{interaction.user} is ordering goods", type = ChannelType.public_thread)
            else:
                await channel.create_thread(name=f"{interaction.user} is ordering goods from {website}",
                                            type=ChannelType.public_thread)
            await interaction.response.send_message(f'Group order created in {channel}')


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Util(bot))