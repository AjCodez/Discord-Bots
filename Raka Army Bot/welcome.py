import discord
from keep_alive import keep_alive
t='TOKEN'

intents = discord.Intents.default()
intents.members = True
client= discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Welcome bot is ready')

@client.event
async def on_member_join(member):
    guild= client.get_guild(GuildID)
    channel=guild.get_channel(ChannelID)

    embed=discord.Embed(title=f'Welcome to Raka.Army {member.name}!',colour=0xffd300, description= f'Hey {member.mention}, welcome to **Raka.Army**\'s official server!\nEnjoy your stay here :)')
    '''embed.add_field(name=f'Hey {member.name}!',value=f'Welcome to **Raka.Army**\'s official server {member.mention}!\nEnjoy your stay here :)')'''
    embed.set_thumbnail(url=Thumbnail URL)
    
    
    
    await channel.send(embed=embed)

@client.event
async def on_message(msg):
    if msg.content == 'hi':
        await msg.channel.send('Hello')

keep_alive()
client.run(t)
