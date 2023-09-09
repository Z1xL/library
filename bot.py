import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(command_prefix='$', intents=intents)

@bot.commands
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.commands
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startwith('forzabbl'):
        await message.channel.send("Lets Go BBL")
    else:
        await message.channel.send(message.content)

@bot.commands
async def bbl(ctx, count_bbl = 11):
    await ctx.send("FORZA BBL" * count_bbl)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
bot.run("MTE0NTAzMzY0MjczMzc0MDIxNA.G-7fSA.bv4Oh4xCjS0bpsgRXxqYH9w67ve-ryx-8jSGVM")
