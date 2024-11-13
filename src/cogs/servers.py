from discord.ext import commands
from constants import format_server_info, cache
from discord import Color, Embed
import discord
from discord.ext import commands
from discord import app_commands
from tables import interview_data

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
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72115) ], self.client, Color.green()) ])
    
    @show_all_servers.command(name='yummy')
    async def show_yummy_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72116) ], self.client, Color.red()) ])
    
    @show_all_servers.command(name='eggz')
    async def show_eggz_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72117) ], self.client, Color.blue()) ])
    
    #this shit going to take 1 houur 
    @app_commands.command(name="hello", description="Say hello!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello, world!")
    #fix the shitty table
    @commands.command(name="interview")
    async def hello_message(self, ctx: commands.Context):
        await ctx.reply(f"{interview_data}")

async def setup(client: commands.Bot):
    await client.add_cog(ServerCommands(client))