import discord
from discord import app_commands
from discord.ext import commands

class Slash(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Slash cog loaded")

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.client.tree.sync(guild=ctx.guild)
        await ctx.send(f"Synced {len(fmt)} commands.")

    @app_commands.command(name="slash", description="test slash command")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f"Pong! {bot_latency} ms.")


async def setup(client):
    await client.add_cog(Slash(client), guilds=[discord.Object(id="1255437522629169285")])