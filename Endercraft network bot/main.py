import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import utils
import asyncio


token = 'TOKEN'

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='>', intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='DM for support'))
    client.load_extension("cogs.onMessage")
    print('Eliga Network is on')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send('You dont have permission to do that...!')
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Please enter all the required arguments.')

@client.command()
@commands.has_permissions(administrator= True)
async def close(ctx):
  if ctx.channel.category.name == "Modmail tickets":
    await ctx.send("Deleting the channel in 10 seconds!")
    embed=discord.Embed(title='Modmail Ticket deleted',description=f'{ctx.channel} was closed by {ctx.author.name}',color=0xff0000)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)
    await asyncio.sleep(10)
    await ctx.channel.delete()

@client.event
async def on_member_join(member):
    guild= client.get_guild(833592682625630208)
    channel=guild.get_channel(840893291926257664)

    
    embed=discord.Embed(title=f'Welcome to The EnderCraft Network {member.name}',colour=0x0000ff, description= f'**Hey {member.mention} !**\n<a:welcome1:840904329070247957><a:welcome2:840904404584628236> to the **EnderCraft Network**\'s official server!\n<a:Arrow:840904044028887080> Please verify yourself in <#833592682625630213>\nEnjoy the Mining <:pepeMinecraft:840512848412278784>')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/835402284149375028/c088196619cbfb3e839152840b33fc53.webp?size=1024')
                            
    await channel.send(member.mention,embed=embed)

@client.command(aliases=['a'])
@commands.has_permissions(kick_members= True)
async def av(ctx,member:discord.Member = None):
    member=ctx.author if not member else member
    embed=discord.Embed(title=f'Avatar for {member.name}', discription= member.mention, color=0x1adb70)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send('Successfully cleared '+str(amount)+' messages.')
    embed=discord.Embed(title='Clear command used',description=f'{ctx.author.mention} cleared {amount} messages from {ctx.channel}',color=0xff00ff)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason='No reason provided'):
    try:
        await member.send('We have decided to kick you out from Eliga Network! Reason: '+reason)
    except:
        print('Cant send message')
    await ctx.send(f'**{member.name}** was kicked from the server. Reason : {reason}')
    await member.kick(reason=reason)
    embed=discord.Embed(title='Kick command used',description=f'{member.name} was kicked from server by {ctx.author.mention} for {reason}',color=0x000000)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)

@client.command(aliases=['w'])
@commands.has_permissions(kick_members = True)
async def warn(ctx,member : discord.Member,*,reason='No reason'):
    try:
        await member.send('You were warned in Eliga Network! Reason: '+reason)
    except:
        print('Cant send message')
    await ctx.send(f'**{member.name}** was warned for {reason}')
    embed=discord.Embed(title='Warn command used',description=f'{member.mention} was warned by {ctx.author.mention} for {reason}',color=0x808080)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason='No reason provided'):
    try:
        await member.send('We have decided to ban you from Raka.Army! Reason: '+reason)
    except:
        print('Cant send message')
    await ctx.send(member.name+' was banned from the server. Reason : '+reason)
    await member.ban(reason=reason)
    embed=discord.Embed(title='Ban command used',description=f'{member.name} was banned from server by {ctx.author.mention} for {reason}',color=0x000000)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f"{user.mention} has been unbanned")
    embed=discord.Embed(title='Unban command used',description=f'{user.name} was unbanned from server by {ctx.author.mention}',color=0xffffff)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)

@client.command(aliases=['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx,member : discord.Member,*,reason='No reason provided'):
    muted_role= ctx.guild.get_role(840899547877212230)
    try:
        await member.send('You are muted in Raka.Army! Reason: '+reason)
    except:
        print('Cant send message')
    await member.add_roles(muted_role)
    await ctx.send(member.mention+' is muted. Reason : '+reason)
    embed=discord.Embed(title='Mute command used',description=f'{member.mention} was muted from server by {ctx.author.mention} for {reason}',color=0x000000)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)
    
@client.command(aliases=['um'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx,member : discord.Member):
    muted_role= ctx.guild.get_role(840899547877212230)
    try:
        await member.send('You are unmuted in Raka.Army!')
    except:
        print('Cant send message')
    await member.remove_roles(muted_role)
    await ctx.send(member.mention+' is unmuted.')
    embed=discord.Embed(title='Unmute command used',description=f'{member.name} was unmuted from server by {ctx.author.mention}',color=0xffffff)
    chl=client.get_channel(840893858410004481)
    await chl.send(embed=embed)

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members= True)
async def whois(ctx,member:discord.Member = None):
    member=ctx.author if not member else member
    embed=discord.Embed(title=member.name, discription= member.mention, color=0xbfff00)
    embed.add_field(name = 'ID', value=member.id, inline=True)
    embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
    embed.add_field(name='Name on server',value=member.display_name,inline=False)
    embed.add_field(name='Created at',value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=True)
    embed.add_field(name='Joined at',value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(aliases=['emb'])
@commands.has_permissions(manage_messages=True)
async def embed(ctx,a,ch,*,ann):
    col = int(a, 16)
    embed=discord.Embed(title=' ',color=col,description=ann)
    chl=client.get_channel(int(ch[2:-1]))
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/835402284149375028/c088196619cbfb3e839152840b33fc53.webp?size=1024')
    await chl.send(embed=embed)

@client.command(aliases=['emb2'])
@commands.has_permissions(manage_messages=True)
async def embed2(ctx,a,ch,*,ann):
    col = int(a, 16)
    embed=discord.Embed(title=' ',color=col,description=ann)
    chl=client.get_channel(int(ch[2:-1]))
    await chl.send(embed=embed)

@client.command(aliases=['h'])
@commands.has_permissions(manage_messages=True)
async def here(ctx,a,ch,*,ann):
    col = int(a, 16)
    embed=discord.Embed(title='New Announcement',color=col,description=ann)
    chl=client.get_channel(int(ch[2:-1]))
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/835402284149375028/c088196619cbfb3e839152840b33fc53.webp?size=1024')
    await chl.send('@here',embed=embed)

@client.command(aliases=['ev'])
@commands.has_permissions(manage_messages=True)
async def everyone(ctx,a,ch,*,ann):
    col = int(a, 16)
    embed=discord.Embed(title='New Announcement',color=col,description=ann)
    chl=client.get_channel(int(ch[2:-1]))
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/835402284149375028/c088196619cbfb3e839152840b33fc53.webp?size=1024')
    await chl.send('@everyone',embed=embed)

@client.command(aliases=['t'])
@commands.has_permissions(manage_messages=True)
async def test(ctx,ch,*,ann):
    embed=discord.Embed(title=' ',color=discord.Color.red(),description=ann)
    print(ann)
    chl=client.get_channel(int(ch[2:-1]))
    await chl.send(embed=embed)

client.run(token)
