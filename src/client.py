import os
import discord
import requests
import random
from dotenv import load_dotenv
from discord.ext import commands, tasks
from discord import app_commands
from constants import cache, api_url, api_request_payload, get_server_name, ResponseAPIServers

"""
Looping for 30 secs thhen get the random caches
"""
class CakeHelper(commands.Bot):
    @tasks.loop(seconds=30)
    async def update_status(self):
        server = cache.get(random.choice([72115, 72116, 72117]))
        game = discord.Game(
            name=f"{get_server_name(server.get('serverId'))} ({server.get('players')})"
        )
        await self.change_presence(status=discord.Status.online, activity=game)


#looping for 5 sec to get a new response
    @tasks.loop(seconds=5)
    async def update_servers_cache(self):
        response = requests.post(api_url, json=api_request_payload)
        if (response.ok != True):
            raise Exception("Response returned Not OK")
        
        data: ResponseAPIServers = response.json()
        for server in data.get('servers'):
            cache[server.get('serverId')] = server

    @update_servers_cache.before_loop
    async def before_loop(self):
        await self.wait_until_ready()

    async def on_ready(self):
        self.update_servers_cache.start()
        self.update_status.start()
        await self.tree.sync(guild=discord.Object(id=822802844243460106))

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.presences = True

load_dotenv()
#prefix
client = CakeHelper(command_prefix="$", intents=intents)
client.help_command = None

@client.event
async def setup_hook():
    for filename in os.listdir('src/cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded Cog: {filename}")
        else:
            print("Unable to load pycache folder.")


client.run(token=os.getenv("TOKEN"))
