import requests
from discord.ext import tasks
from constants import api_url, api_request_payload, cache, ResponseAPIServers

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