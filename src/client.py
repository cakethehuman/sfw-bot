import os
import discord
import requests
from dotenv import load_dotenv
from discord.ext import commands, tasks
from constants import cache, ResponseAPIServers

api_url = 'https://api.scplist.kr/api'
api_request_payload = {
    "search": "SFW",
    "countryFilter": ["SG"],
    "friendlyFire": "null",
    "hideEmptyServer": False,
    "hideFullServer": False,
    "modded": "null",
    "whitelist": "null",
    "sort": "DISTANCE_ASC"
}

class CakeHelper(commands.Bot):
    @tasks.loop(seconds=5)
    async def update_servers_cache():
        try:
            response = requests.post(api_url, api_request_payload)

            if (response.ok != True):
                raise Exception("Response returned Not OK")
            
            data: ResponseAPIServers = response.json()
            for server in data.servers:
                cache[server.serverId] = server
            
        except:
            print(f"Failed to get servers info")

    @update_servers_cache.before_loop
    async def update_before_loop(self):
        await self.wait_until_ready()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.presences = True

load_dotenv()
client = CakeHelper(command_prefix="$", intents=intents)
client.help_command = None

cog_files = [
    'cogs.servers'
]

for cog_file in cog_files:
    client.load_extension(cog_file)
    print("%s loaded" % cog_file)

client.run(token=os.getenv("TOKEN"))