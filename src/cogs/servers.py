from discord.ext import commands
from constants import format_server_info, cache
from discord import Color, Embed

embed_server_colors = {
    72115: Color.red(),
    72116: Color.green(),
    72117: Color.pink()
}

def create_embed_response(description_text: list[str], client: commands.Bot):
    embed = Embed()
    embed.color = Color.pink()
    embed.description = "\n".join(description_text)
    embed.set_author(name='this is what cake said', icon_url=client.user.avatar.url)

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
    async def show_eggz_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72115) ], self.client) ])
    
    @show_all_servers.command(name='yummy')
    async def show_eggz_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72116) ], self.client) ])
    
    @show_all_servers.command(name='eggzellent')
    async def show_eggz_server(self, ctx: commands.Context):
        await ctx.reply(embeds=[ create_embed_response([ format_server_info(72117) ], self.client) ])

def setup(client: commands.Bot):
    client.add_cog(ServerCommands(client))