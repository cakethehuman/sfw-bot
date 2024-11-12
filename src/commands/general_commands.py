import datetime
import discord
from discord.ext import commands
import discord.ext.commands
from constants import cache, developers, get_server_name
import discord.ext

server_names = ["eggzellent", "vanilla", "yummy"]
# Eggzellent -> 72117
# Vanilla -> 72115
# Yummy -> 72116

def format_server_toembed(id: int, client: commands.Bot):
    server = cache.get(id)
    embed = discord.Embed()
    embed.set_author("this is what cake said", client.user.avatar.url)
    embed.description = (
        f"*{get_server_name(id)}({id})*\n" +
        "Country: *Singapore*\n" +
        f"Game Version: *{server.version}" +
        f"Players Count: *{server.players}"
        )
    embed.timestamp = datetime.timezone.utc
    return embed

class GeneralCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_group(fallback="all")
    async def server(self, ctx: discord.ext.commands.Context):
        description_text = []
        embed = discord.Embed (
            color=discord.Color.blurple()
        )

        for id, server in cache.items():
            description_text.append(
                f"*{get_server_name(id)}({id})*\n" +
                "Country: *Singapore*\n" +
                f"Game Version: *{server.version}*\n" +
                f"Players Count: *{server.players}*"
            )

        embed.set_author("this is what cake said", self.client.user.avatar.url)
        embed.description = "\n".join(description_text)
        embed.timestamp = datetime.timezone.utc

        ctx.reply(None, embeds=[embed])

    @server.command(name='vanilla')
    async def vanilla(self, ctx: discord.ext.commands.Context):
        ctx.reply(embed=format_server_toembed(72115, self.client))

    @server.command(name='yummy')
    async def yummy(self, ctx: discord.ext.commands.Context):
        ctx.reply(embed=format_server_toembed(72116, self.client))

    @server.command(name='eggz')
    async def eggz(self, ctx: discord.ext.commands.Context):
        ctx.reply(embed=format_server_toembed(72117, self.client))

    @commands.hybrid_command(name='restart')
    async def restart(self, ctx: discord.ext.commands.Context):
        if (ctx.author.id in developers) != True:
            return
        
        exit(1) # hehe
        # not a real restart
        # but ptero handles it

def setup(client: discord.ext.commands.Bot):
    client.add_cog(GeneralCommands(client))

print("Hello")