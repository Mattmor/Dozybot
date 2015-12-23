import discord
from random import randint
from botconfig import *

client = discord.Client()
client.login(botEmail, botPassword)

@client.event
def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        client.send_message(message.channel, """You can use these commands:
!bigkappa = the big version
!coin = flip a coin
!kappa
!liu = da best
!hello = replies a greeting and your name
!help = list the commands
!roll = roll a random number between 0 and 100
!ts = teamspeak IP address
!whats up = obvious
        """)

    if message.content.startswith('!coin'):
        roll = randint(0, 1)
        if (roll == 0):
            coin = "heads"
        elif (roll == 1):
            coin = "tails"
        client.send_message(message.channel, '{} flipped a coin and it landed on '.format(message.author.mention()) + coin)

    if message.content.startswith('!kappa'):
        client.send_file(message.channel, './images/Kappa.png')

    if message.content.startswith('!bigkappa'):
        client.send_file(message.channel, './images/Kappahd.png')

    if message.content.startswith('!roll'):
        roll = randint(0, 100)
        client.send_message(message.channel, '{} rolled a '.format(message.author.mention()) + str(roll))

    if message.content.startswith('!hello'):
        client.send_message(message.channel, 'Hello {}!'.format(message.author.mention()))

    if message.content.startswith('!liu'):
        liu = discord.utils.find(lambda m: m.id == '105714564930260992', message.channel.server.members)
        if (liu == None):
            client.send_message(message.channel, 'Liu is not on this server, but if he was he\'d be the best person in this server.')
        else:
            client.send_message(message.channel, '{} is the greatest person in the universe. Kappa.'.format(liu.mention()) , mentions=True)

    if message.content.startswith('!whats up'):
        client.send_message(message.channel, 'The sky.')

    if message.content.startswith('!ts'):
        client.send_message(message.channel, 'Teamspeak IP: 88.202.226.151:7297')

@client.event
def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

client.run()