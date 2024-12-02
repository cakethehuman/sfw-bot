from discord.ext import commands
from constants import format_server_info, cache
from discord import Color, Embed
import discord
from discord.ext import commands
from discord import app_commands

def create_embed_response(description_text: list[str], client: commands.Bot, color: Color = Color.pink()):
    embed = Embed()
    embed.color = color
    embed.description = "\n\n".join(description_text)
    embed.set_author(name='this is what cake said', icon_url=client.user.avatar.url)
    embed.set_footer(text="api might be little slow")

    return embed

class ServerCommands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.hybrid_group('server', fallback='all')
    @commands.guild_only()
    async def show_all_servers(self, ctx: commands.Context):
        description_text = []

        for id in cache.keys():
            description_text.append(format_server_info(id))
            
        embed = create_embed_response(description_text, self.client)

        await ctx.reply(embeds=[embed])
        return
    
    @show_all_servers.command(name='vanilla')
    async def show_vanilla_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72115)], self.client, Color.green()) ])
    
    @show_all_servers.command(name='yummy')
    async def show_yummy_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72116)], self.client, Color.red()) ])
    
    @show_all_servers.command(name='eggz')
    async def show_eggz_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72117)], self.client, Color.blue()) ])
    
    #this shit going to take 1 houur 
    @app_commands.command(name="hello", description="Say hello!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, world!")


class Basic_Interview(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="apply")
    async def hello_message(self, ctx: commands.Context, member: discord.Member=None):
        member = member or ctx.message.author
        role = discord.utils.get(ctx.guild.roles, id=1302242138997653535)
        
        embed = discord.Embed(
            color = discord.Color.from_str("#000080"),
            description=f"i gave you {role} role add your information in this form \n https://docs.google.com/forms/d/e/1FAIpQLSdR87JKY4sbvaL1pfn_oyeSr4ykwMI2P9iLbeli7ymJVlXFaw/viewform"
        )

        try:
            if role not in member.roles:
                await member.add_roles(role)
                await ctx.reply(embed=embed)
            else:
                await ctx.reply("you already have")
        except ValueError or discord.Forbidden:
            await ctx.reply("cake bot fail/ too weak to give you that role")

class Basic_Commands(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(name="cmd")
    async def help(self, ctx: commands.Context):
        embed = discord.Embed(
            color = discord.Color.yellow(),
            title= "All the commands",
            description=
            "```$server <server-name>``` check the number of players in the game"
            "```$cmd``` ask for help from cake lel\n"
        )
        embed.set_footer(text = "more will come")
        embed.set_author(name='this is what cake said', icon_url=self.client.user.avatar.url)
        await ctx.reply(embed=embed)

async def setup(client: commands.Bot):
    await client.add_cog(ServerCommands(client))
    await client.add_cog(Basic_Commands(client))
    await client.add_cog(Basic_Interview(client))