import discord
from discord.ext import commands
import random
import sys
import csv
import time

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='~', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def wtf():
    msg = "Hi guardian, I'm Kill Tracker Ghost and I'm part of your pre-order purchase!\n\n" \
          "I understand the following commands:\n\n" \
          "`~wtf` - I'm not sure what this command does...\n" \
          "`~eightball` - Ask the magic 8 ball a question.\n" \
          "`~roll` - Request a random number, chosen by fair dice roll.\n" \
          "`~catfact` - Edumacates you in the vast world of meow-meows\n" \
          "`~dadjoke` - U laff @ dad jokes\n" \
          "`~offjoke` - U cry @ offensive joke\n" \
          "`~deadbaby` - Tells really horrible joke\n" \
          "`~google` - Stupid way to find out out shit about shit you don't know\n" \
          "`~fliptable` - Fixes table\n" \
          "`~yeah` - YEAH!!!\n" \
          "`~shrug` - I dunno\n" \
          "\nIf I'm not working correctly, go fuck yourself, you aren't my boss."
    await bot.say(msg)

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll():
    await bot.say('4')

    # """Rolls a dice in NdN format."""
    # try:
    #     rolls, limit = map(int, dice.split('d'))
    # except Exception:
    #     await bot.say('Format has to be in NdN!')
    #     return

    # result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    # await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

# @bot.command()
# async def repeat(times : int, content='repeating...'):
#     """Repeats a message multiple times."""
#     for i in range(times):
#         await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

# @bot.group(pass_context=True)
# async def cool(ctx):
#     """Says if a user is cool.

#     In reality this just checks if a subcommand is being invoked.
#     """
#     if ctx.invoked_subcommand is None:
#         await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

# @cool.command(name='bot')
# async def _bot():
#     """Is the bot cool?"""
#     await bot.say('Yes, the bot is cool.')

#########################################################################################

@bot.command()
async def fliptable():
    await bot.say('┬──┬ ﾉ(° -°ﾉ) That wasn\'t nice.')

@bot.command()
async def yeah():
    # #yeah
    await bot.say(" \n( •\_•)\n( •\_•)>⌐■-■\n(⌐■\_■)")

@bot.command()
async def shrug():
    # ¯\_(ツ)_/¯
    await bot.say("¯\\_(ツ)_/¯")

bot.command()
async def google(query : str):
    await bot.say("Hey guardian, let me Google that for you: http://lmgtfy.com/?q="+query)

@bot.command()
async def catfact():
    cat_facts = open(sys.path[0] + '/cat_facts.txt').read().splitlines()
    await bot.say(random.choice(cat_facts))

@bot.command()
async def dadjoke():
    dad_joke = open(sys.path[0] + '/dadjokes.txt').read().splitlines()
    await bot.say(random.choice(dad_joke))

@bot.command()
async def offjoke():
    off_joke = open(sys.path[0] + '/offjokes.txt').read().splitlines()
    await bot.say(random.choice(off_joke))

@bot.command()
async def deadbaby():
    dead_baby = open(sys.path[0] + '/deadbaby.txt').read().splitlines()
    await bot.say(random.choice(dead_baby))

@bot.command()
async def eightball():
    phrases = [
        "As I see it, yes",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don’t count on it",
        "It is certain",
        "It is decidedly so",
        "Most likely",
        "My reply is no",
        "My sources say no",
        "Outlook good",
        "Outlook not so good",
        "Reply hazy, try again",
        "Signs point to yes",
        "Very doubtful",
        "Without a doubt",
        "Yes",
        "Yes, definitely",
        "You may rely on it.",
        "Blame Kanotu"
    ]
    #await bot.send_message(message.channel, "{user}: {phrase}".format(user=member.mention, phrase=random.choice(phrases)))
    await bot.say(random.choice(phrases))

@bot.command(pass_context=True)
async def stat(ctx):
    """Returns a CSV file of all users on the server."""
    await bot.request_offline_members(ctx.message.server)
    before = time.time()
    nicknames = [m.display_name for m in ctx.message.server.members]
    with open('temp.csv', mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        for v in nicknames:
            writer.writerow([v])
    after = time.time()
    await bot.send_file(ctx.message.author, 'temp.csv', filename='stats.csv',
                        content="Here you go! Check your PM's. Generated in {:.4}ms.".format((after - before)*1000))


bot.run('YOURTOKENHERE')