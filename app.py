# Work with Python 3.6
import discord

TOKEN = 'NTIyNDMzNDU2NDE2NzUxNjM1.DvK5-A.e8mWyS48_6ytPPrvpUsZfmD_DcU'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!comment va ?'):
        msg = ' {0.author.mention} Super merci bien ! et toi ?:)'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!salut'):
        msg = 'Yoooo{0.author.mention} '.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!Salut'):
        msg = 'Yoooo {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('!help'):
        msg = ' {0.author.mention} Here is the command list:\n -hello \n -salut \n -comment va ?'.format(message)
        await client.send_message(message.channel, msg)

    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)