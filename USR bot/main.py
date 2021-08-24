import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import utils
import asyncio

t='TOKEN'

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='>', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='DM for any query'))
    client.load_extension("cogs.onMessage")
    print('Bot is on')

@client.command(aliases=['dm'])
@commands.has_permissions(administrator=True)
async def dm_all(ctx,*,ann):
    members = ctx.guild.members
    embed=discord.Embed(title=' ', discription= ' ', color=0xff0000)
    embed.add_field(name='**New Announcement**', value=ann)
    for member in members:
      try:
        await member.send(embed=embed)
        await ctx.send(f'sent to {member.name}')
        await asyncio.sleep(15)
      except:
        await ctx.send(f'couldnt send to {member.mention}')

@client.event
async def on_member_join(member):
    guild= client.get_guild(GuildID)
    channel=guild.get_channel(ChannelID)

    
    embed=discord.Embed(title=f'Welcome to Raka\'s Association of Members',colour=0xff0000, description= f'Hey {member.mention}, welcome to **RAM**\'s official server!\nCheck <#868299595871035414> for any further updates!!')
    #embed.set_thumbnail(url=member.avatar_url)
    embed.set_image(url='https://cdn.discordapp.com/attachments/826509090054340628/868481070260191272/20210724_184324.gif')
                         
    await channel.send(member.mention,embed=embed)

@client.command()
#@commands.has_permissions(administrator= True)
async def close(ctx):
  if ctx.channel.category.name == "Modmail tickets":
    await ctx.send("Deleting the channel in 10 seconds!")
    embed=discord.Embed(title='Modmail Ticket deleted',description=f'{ctx.channel} was closed by {ctx.author.name}',color=0xff0000)
    chl=client.get_channel(ChannelID)
    await chl.send(embed=embed)
    await asyncio.sleep(10)
    await ctx.channel.delete()

@client.command(aliases=['a'])
@commands.has_permissions(kick_members= True)
async def av(ctx,member:discord.Member = None):
    member=ctx.author if not member else member
    embed=discord.Embed(title=f'Avatar for {member.name}', discription= member.mention, color=discord.Color.red())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(aliases=['ann1'])
@commands.has_permissions(manage_messages=True)
async def ann(ctx,a='ff0000',*,ann):
    guild= client.get_guild(GuildID)
    channel1=guild.get_channel(ChannelID)
    col = int(a, 16)
    embed=discord.Embed(title=' ', discription= ' ', color=col)
    embed.add_field(name='**New Announcement**', value=ann)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/826137383271399445/859857071100133436/USR_LOGO.png')
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'By {ctx.author.name}')
    
    await channel1.send(embed=embed)

@client.command(aliases=['ann2'])
@commands.has_permissions(manage_messages=True)
async def ann_ev(ctx,a='ff0000',*,ann):
    guild= client.get_guild(GuildID)
    channel1=guild.get_channel(ChannelID)
    col = int(a, 16)
    embed=discord.Embed(title=' ', discription= ' ', color=col)
    embed.add_field(name='**New Announcement**', value=ann)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/826137383271399445/859857071100133436/USR_LOGO.png')
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'By {ctx.author.name}')
    
    pin='@everyone <@&778614439360069652> <@&778616908706349058> <@&826132734023565322> <@&778677970134237194> <@&778677621332508682>'
    await channel1.send(pin,embed=embed)

@client.command(aliases=['ann3'])
@commands.has_permissions(manage_messages=True)
async def ann_here(ctx,a='ff0000',*,ann):
    guild= client.get_guild(GuildID)
    channel1=guild.get_channel(ChannelID)
    col = int(a, 16)
    embed=discord.Embed(title=' ', discription= ' ', color=col)
    embed.add_field(name='**New Announcement**', value=ann)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/826137383271399445/859857071100133436/USR_LOGO.png')
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'By {ctx.author.name}')
    
    await channel1.send('@here')
    await channel1.send(embed=embed)

@client.command(aliases=['ann4'])
@commands.has_permissions(manage_messages=True)
async def ann_test(ctx,a='ff0000',*,ann):
    guild= client.get_guild(GuildID)
    channel1=guild.get_channel(ChannelID)
    col = int(a, 16)
    embed=discord.Embed(title=' ', discription= ' ', color=col)
    embed.add_field(name='**New Announcement**', value=ann)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/826137383271399445/859857071100133436/USR_LOGO.png')
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'By {ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(aliases=['t'])
@commands.has_permissions(manage_messages=True)
async def test(ctx,ch,*,ann):
    embed=discord.Embed(title=' ',color=discord.Color.red(),description=ann)
    print(ann)
    chl=client.get_channel(int(ch[2:-1]))
    await chl.send(embed=embed)

@client.command(aliases=['im'])
@commands.has_permissions(manage_messages=True)
async def image(ctx,a,*,pic):
    col = int(a, 16)
    embed=discord.Embed(title=' ', discription= ' ', color=col)
    embed.set_image(url=pic)
    await ctx.send(embed=embed)

@client.command(aliases=['emb'])
@commands.has_permissions(manage_messages=True)
async def embed(ctx,a,ch,*,ann):
    col = int(a, 16)
    embed=discord.Embed(title=' ',color=col,description=ann)
    chl=client.get_channel(int(ch[2:-1]))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/826137383271399445/859857071100133436/USR_LOGO.png')
    await chl.send(embed=embed)

@client.command(aliases=['com'])
async def commands(ctx):
    await ctx.send('>ann [Hex Code] [Message]\n>ann_test [Hex Code] [Message]\n>ann_ev [Hex Code] [Message]\n>ann_here [Hex Code] [Message]\n>image [Hex Code] [Image Link]\n>av [mention person]\n>dm_all [announcement]\n>embed [hex code] [channel] [message]')

client.run(t)
