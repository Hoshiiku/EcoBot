import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True



bot = commands.Bot(command_prefix = "/", intents = intents )



@bot.event 
async def on_ready():
    print("Bot's online")




rubbish_decomposition ={
    "plastic bottle": "500 years",
    "can": "10 years",
    "plastic bag":"20 years",
    "glass": "4000 years",
    "paper": "6 weeks",
    "diaper":"500 years" ,
    "food": "2 weeks"
}

@bot.command()
async def helpme(ctx):
    await ctx.send("This bot shows how long rubbish takes to decompose, use it using /classify")
    await ctx.send(f"List of objects: {rubbish_decomposition}")




@bot.command()

async def classify(ctx, *, object: str):
    object = object.lower()
    if object in rubbish_decomposition:
        time = rubbish_decomposition[object]
        await ctx.send(f"The object {object} takes {time} to decompose")
    else:
        await ctx.send("No data was found!")











bot.run("TOKEN GOES HERE!")

