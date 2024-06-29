import discord

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

bot.load_extension('cogs.Greetings')

@bot.slash_command(guild_ids=[1255437522629169285])
async def sync(ctx): 
    await bot.sync_commands()
    await ctx.send(f"succesfully synced commands")

@bot.slash_command(guild_ids=[1255437522629169285])
async def hello(ctx):
    await ctx.respond("Hello!")

bot.run('secrettokenhere!')