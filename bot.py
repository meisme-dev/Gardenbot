import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

client = commands.Bot(command_prefix="./", help_command=None)
load_dotenv()

greetings = [
    "Hello!", "Hallo!", "Bonjour!", "Ciao!", "¡Hola!",
    "Hej!", "Ahoj!", "Aloha!", "Привет!", "Χαίρετε!",
    "你好!", "こんにちは!", "여보세요!", "!مرحبا", "हैलो!"
]

predictions = [
    "Yeah, sure.", "What about no?", "Yes, totally.", "Are you kidding me? Of course, no!", "Of course!",
    "I guess, no.", "Probably yes." , "Nah. Not at all.", "Obviously, yes!"
]

death_scenarios = [
    "A snake bit you.", "You met a vampire and he sucked all your blood.", \
    "You drank a glass of juice, but there was poison inside.", \
    "You were thrown out into space by a giant gorilla.", "You ate too many mushrooms.", \
    "A heavy hammer fell onto your head.", "A zombie strangled you to death.", \
    "A maniac cut your throat while you were sleeping.", "You became too old.", \
    "You decided that you had to eat 20 bags of chips.", \
    "You wanted to take a vacation in Chernobyl.", \
    "Voldemort came to you and said \'Avada Kedavra!\'", \
    "You were trying to install Arch Linux, but failed."
]

scary_things = ["😈", "💀", "👻", "🎃", "🧛‍♂️", "🦇", "🧟"]

distro_list = [
    "Arch Linux", \
    "Ubuntu", \
    "Gentoo", \
    "Mageia", \
    "Debian", \
    "Endeavour OS", \
    "Zorin OS", \
    "Pop_OS!", \
    "Fedora", \
    "Cent OS", \
    "Manjaro", \
    "OpenSUSE", \
    "Kali", \
    "Blackarch", \
    "LFS", \
    "Artix", \
    "Arco", \
    "Knoppix", \
    "Alpine", \
    "FreeBSD", \
    "OpenBSD", \
    "DragonflyBSD", \
    "Hyperbola", \
    "Parabola", \
    "DragonflyBSD", \
    "Qubes OS", \
    "Void Linux", \
    "Venom Linux", \
    "Elementary OS", \
    "Slackware" 


]

ubuntu_versions = [
    "Ubuntu 4.10 (Warty Warthog)", \
    "Ubuntu 5.04 (Hoary Hedgehog)", \
	"Ubuntu 5.10 (Breezy Badger)", \
    "Ubuntu 6.06 LTS (Dapper Drake)", \
	"Ubuntu 6.10 (Edgy Eft)", \
	"Ubuntu 7.04 (Feisty Fawn)", \
	"Ubuntu 7.10 (Gutsy Gibbon)", \
	"Ubuntu 8.04 LTS (Hardy Heron)", \
	"Ubuntu 8.10 (Intrepid Ibex)", \
	"Ubuntu 9.04 (Jaunty Jackalope)", \
	"Ubuntu 9.10 (Karmic Koala)",  \
	"Ubuntu 10.04 LTS (Lucid Lynx)",  \
	"Ubuntu 10.10 (Maverick Meerkat)",  \
	"Ubuntu 11.04 (Natty Narwhal)",  \
	"Ubuntu 11.10 (Oneiric Ocelot)",  \
	"Ubuntu 12.04 LTS (Precise Pangolin)",  \
	"Ubuntu 12.10 (Quantal Quetzal)",  \
	"Ubuntu 13.04 (Raring Ringtail)",  \
	"Ubuntu 13.10 (Saucy Salamander)",  \
	"Ubuntu 14.04 LTS (Trusty Tahr)",  \
	"Ubuntu 14.10 (Utopic Unicorn)",  \
	"Ubuntu 15.04 (Vivid Vervet)",  \
	"Ubuntu 15.10 (Wily Werewolf)",  \
	"Ubuntu 16.04 LTS (Xenial Xerus)",  \
	"Ubuntu 16.10 (Yakkety Yak)",  \
	"Ubuntu 17.04 (Zesty Zapus)",  \
	"Ubuntu 17.10 (Artful Aardvark)",  \
	"Ubuntu 18.04 LTS (Bionic Beaver)",  \
	"Ubuntu 18.10 (Cosmic Cuttlefish)",  \
	"Ubuntu 19.04 (Disco Dingo)",  \
	"Ubuntu 19.10 (Eoan Ermine)",  \
	"Ubuntu 20.04 LTS (Focal Fossa)",  \
	"Ubuntu 20.10 (Groovy Gorilla)",  \
    "Ubuntu 21.04 (Hirsute H...)"
]

vowels = ["a","e","i","o","u","y"]

consonants = [
    "b","c","d","f","g","h","j","k","l","m", \
    "n","p","q","r","s","t","v","w","x","z"
]

@client.event
async def on_connect():
    print("Connecting to Discord.....")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
    activity=discord.Game(f"Type \'./help\' for the commands. On {len(client.guilds)} servers"))
    print("Gardenbot has connected to Discord")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Client-side ping took {round(client.latency * 1000)}ms')

@client.command()
async def about(ctx):
    await ctx.send(f'Gardenbot is a Discord by me is me forked from PurpleBot (https://github.com/PurpleSci/PurpleBot).')

@client.command()
async def license(ctx):
    await ctx.send(f'Gardenbot is licensed under MIT. That means it\'s open-source and you are free to redistribute your own modifications of the bot. This is not the full license, it is just summarized. Please read the full license here: https://raw.githubusercontent.com/meisme-dev/Gardenbot/master/LICENSE')

@client.command()
async def github(ctx):
    await ctx.send(f'Gardenbot\'s source code is avalaible on GitHub: https://github.com/meisme-dev/Gardenbot')

@client.command()
async def invite(ctx):
    await ctx.send(f'If you want to add Gardeonbot to your server, use this link: https://discord.com/api/oauth2/authorize?client_id=769606923091181569&permissions=8&scope=bot')

@client.command()
async def distro(ctx):
    await ctx.send(random.choice(distro_list))

@client.command()
async def hello(ctx):
    await ctx.send(random.choice(greetings))

@client.command()
async def randnum(ctx):
    await ctx.send(random.randint(0, 10000))

@client.command()
async def predict(ctx):
    await ctx.send(random.choice(predictions))

@client.command()
async def die(ctx):
    await ctx.send(random.choice(death_scenarios))

@client.command()
async def boo(ctx):
    await ctx.send(random.choice(scary_things))

@client.command()
async def pogchamp(ctx):
    await ctx.send('''
░░░░░▒░░▄██▄░▒░░░░░░
░░░▄██████████▄▒▒░░░
░▒▄████████████▓▓▒░░
▓███▓▓█████▀▀████▒░░
▄███████▀▀▒░░░░▀█▒░░
████████▄░░░░░░░▀▄░░
▀██████▀░░▄▀▀▄░░▄█▒░
░█████▀░░░░▄▄░░▒▄▀░░
░█▒▒██░░░░▀▄█░░▒▄█░░
░█░▓▒█▄░░░░░░░░░▒▓░░
░▀▄░░▀▀░▒░░░░░▄▄░▒░░
░░█▒▒▒▒▒▒▒▒▒░░░░▒░░░
░░░▓▒▒▒▒▒░▒▒▄██▀░░░░
░░░░▓▒▒▒░▒▒░▓▀▀▒░░░░
░░░░░▓▓▒▒░▒░░▓▓░░░░░
░░░░░░░▒▒▒▒▒▒▒░░░░░░
''')

@client.command()
async def ubuntu(ctx):
    await ctx.send(random.choice(ubuntu_versions))

@client.command()
async def groovy(ctx):
    await ctx.send(f'https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,w_500,h_776/https://assets.ubuntu.com/v1/fe951eda-20.10_Groovy+Gorilla_RPi_Sketch.svg')

@client.command()
async def pi(ctx):
    await ctx.send(f'Here is π calculated to the first 1000000 digits: http://newton.ex.ac.uk/research/qsystems/collabs/pi/pi6.txt')

@client.command()
async def ptable(ctx):
    await ctx.send(f'Ptable is an interactive online version of the Periodic Table of Elements: https://ptable.com/')

@client.command()
async def rubbish(ctx):
    sentence = ""
    for i in range(random.randrange(3,7)):
        word = str()
        for j in range(random.randrange(1,5)):
            word = word + random.choice(consonants) + random.choice(vowels)
        sentence = sentence + word + " "
    await ctx.send(sentence.capitalize().rstrip() + random.choice(["!","?","."]))

@client.command()
async def echo(ctx,*,arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{arg}")

@client.command()
async def help(ctx,arg):
    author = ctx.message.author
    await author.create_dm()
    if arg == "moderation":
        embedVar = discord.Embed(title="Moderation Commands", description="Shows a list of commands for moderators \n \u200B", color=0x3388FF)
        embedVar.add_field(name="Kick", value="```Kicks a member. Usage: ./kick @member``` \n \u200B", inline=True)
        embedVar.add_field(name="Mute", value="```Mutes a member. Usage: ./mute @member``` \n \u200B", inline=True)
        embedVar.add_field(name="Ban", value="```Bans a member. Usage: ./ban @member``` \n \u200B", inline=True)
   
    await ctx.send(embed=embedVar)

@help.error
async def help_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        embedVar = discord.Embed(title="Help", description="Shows a list of commands \n \u200B", color=0x3388FF)
        embedVar.add_field(name="Utility", value="```help \nping about \nlicense github \ninvite pi \nptable``` \n \u200B", inline=True)
        embedVar.add_field(name="Fun", value="```hello distro \nrandnum predict \ndie boo \npogchamp ubuntu \ngroovy rubbish``` \n \u200B", inline=True)
        embedVar.add_field(name="Moderation", value="```ban \nmute \nkick \npurge  \nMore coming soon!```", inline=True)
        await ctx.send(embed=embedVar)

@client.event
async def on_disconnect():
    print("GardenBot disconnected.")


# Let's make the Discord.py module understand that there is a folder for additional commands (cogs).

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('DISCORD_TOKEN'))
