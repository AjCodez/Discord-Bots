from discord.ext import commands
from discord import utils
import discord
import asyncio

class onMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if isinstance(message.channel, discord.DMChannel):
            guild = self.bot.get_guild(GuildID)
            categ = utils.get(guild.categories, name = "Modmail tickets")
            channel = utils.get(categ.channels, topic = str(message.author.id))
            if not channel:
                channel = await categ.create_text_channel(name = f"{message.author.name}#{message.author.discriminator}", topic = str(message.author.id))
                await channel.send(f"New modmail created by {message.author.mention}")
                await message.author.send('Thanks for contacting! Please wait for response!')
                embed1=discord.Embed(title='Modmail Ticket created',description=f'{message.author.mention} created a ticket with first message:\n {message.content}',color=0x00ff00)
                chl=self.bot.get_channel(ChannelID)
                await chl.send(embed=embed1)

            embed = discord.Embed(description = message.content, colour = 0x696969)
            embed.set_author(name = message.author, icon_url = message.author.avatar_url)
            await channel.send(embed = embed)
            if message.attachments != []:
                files = message.attachments
                for file in files:
                    await channel.send(file.url)

        elif isinstance(message.channel, discord.TextChannel):
            if message.content.startswith(self.bot.command_prefix):
                pass
            else:
                topic = message.channel.topic
                if topic:
                    try:
                        member = message.guild.get_member(int(topic))
                    except:
                        pass
                    if member:
                        embed=discord.Embed(description= message.content)
                        await member.send(embed=embed)
                        if message.attachments != []:
                            files = message.attachments
                            for file in files:
                                await member.send(file.url)

def setup(bot):
    bot.add_cog(onMessage(bot))
