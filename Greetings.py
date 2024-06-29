from discord.ext import commands

class Greetings(commands.Cog, name="Greeting Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="greet", help="Sends a greeting message.")
    async def greet(self, ctx):
        await ctx.send("Hello!")

def setup(bot):
    bot.add_cog(Greetings(bot))