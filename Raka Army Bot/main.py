import discord
from discord.ext import commands



client = commands.Bot(command_prefix='>')


@client.event 
async def on_ready():
    await client.change_presence(activity=discord.Game(name='2 Rs ki pepsi Raka vai seksi'))
    print('Bot is ready')


@client.event
async def on_message(msg):
    try:
        if ':'==msg.content[0] and ':'==msg.content[-1]:
            en=msg.content[1:-1]
            for emoji in msg.guild.emojis:
                if en==emoji.name:
                    await msg.channel.send(str(emoji))
                    await msg.delete()
                    break
    except:
        print('no')

    await client.process_commands(msg)



@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send('You dont have permission to do that...!')
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Please enter all the required arguments.')
    '''if isinstance(commands.BotMissingAnyRole):
        await ctx.send('I dont have permission to do that.')
    if isinstance(commands.BotMissingPermissions):
        await ctx.send('I dont have permission to do that.')'''

@client.command(aliases=['c'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send('Successfully cleared '+str(amount)+' messages.')

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason='No reason provided'):
    try:
        await member.send('We have decided to kick you out from Raka.Army! Reason: '+reason)
    except:
        print('Cant send message')
    await ctx.send(member.name+' was kicked from the server. Reason : '+reason)
    await member.kick(reason=reason)

@client.command(aliases=['w'])
@commands.has_permissions(kick_members = True)
async def warn(ctx,member : discord.Member,*,reason):
    try:
        await member.send('You were warned in Raka.Army! Reason: '+reason)
    except:
        print('Cant send message')
    await ctx.send(member.name+' was warned! Reason : '+reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason='No reason provided'):
    try:
        await member.send('We have decided to ban you from Raka.Army! Reason: '+reason)
    except:
        print('Cant send message')
    await ctx.send(member.name+' was banned from the server. Reason : '+reason)
    await member.ban(reason=reason)

'''@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    buser = await ctx.guild.bans()
    memname,memdisc=member.split('#')

    for banned_entry in buser:
        user=banned_entry.user

        if (user.name, user.discriminator)==(memname,memdisc):
            await ctx.guild.unban(user)
            await ctx.send(memname+' is unbanned!')
            return

    await ctx.send(member+' was not found')'''
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.send(f"{user.mention} has been unbanned")

@client.command(aliases=['m'])
@commands.has_permissions(kick_members = True)
async def mute(ctx,member : discord.Member,*,reason='No reason provided'):
    muted_role= ctx.guild.get_role(RoleID)
    try:
        await member.send('You are muted in Raka.Army! Reason: '+reason)
    except:
        print('Cant send message')
    await member.add_roles(muted_role)
    await ctx.send(member.mention+' is muted. Reason : '+reason)
    
@client.command(aliases=['um'])
@commands.has_permissions(kick_members = True)
async def unmute(ctx,member : discord.Member):
    muted_role= ctx.guild.get_role(RoleID)
    try:
        await member.send('You are unmuted in Raka.Army!')
    except:
        print('Cant send message')
    await member.remove_roles(muted_role)
    await ctx.send(member.mention+' is unmuted.')

@client.command(aliases=['user','info'])
@commands.has_permissions(kick_members= True)
async def whois(ctx,member:discord.Member = None):
    member=ctx.author if not member else member
    embed=discord.Embed(title=member.name, discription= member.mention, color=discord.Color.red())
    embed.add_field(name = 'ID', value=member.id, inline=True)
    embed.add_field(name="Top Role", value=member.top_role.mention, inline=True)
    embed.add_field(name='Name on server',value=member.display_name,inline=False)
    embed.add_field(name='Created at',value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=True)
    embed.add_field(name='Joined at',value=member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'), inline=True)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)

@client.command(aliases=['a'])
@commands.has_permissions(kick_members= True)
async def avatar(ctx,member:discord.Member = None):
    member=ctx.author if not member else member
    embed=discord.Embed(title=member.name, discription= member.mention, color=discord.Color.red())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}')
    await ctx.send(embed=embed)


keep_alive()

client.run('TOKEN')
