import datetime
import os
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from constants import cache, get_server_name, developers
from tasks import update_servers_cache
from commands import general_commands

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

cog_files = ['commands.general_commands']
async def load():
    for cog_file in cog_files:
        await client.load_extension(cog_file)
        print("%s loaded" % cog_file)

load()
client.run(token=os.getenv("TOKEN"))