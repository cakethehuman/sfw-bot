import discord
import requests
from requests_cache import CachedSession
import requests_cache
from threading import Thread

base_url = 'https://api.scplist.kr/api'
session = requests_cache.CachedSession('scplist_cache', expire_after=5)

data = None
def get_server_info(server_id):
    url = f"{base_url}/servers/{server_id}"
    response = session.get(url)
    
    if (
    response.status_code == 200 ):
        try:
            data = response.json()
            return data
        except ValueError:
            print(F"no {response.status_code}")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    
    eggz = 72117

    vannila = 72116

    yummy = 72115

    if message.author == client.user:
        return

    if message.content.startswith('$eggz'):
        eggz_players = get_server_info(eggz)
        await message.channel.send(f'this is your player count cake said: {eggz_players["players"]}')
    
    if message.content.startswith('$vannila'):
        vannila_players = get_server_info(vannila)
        await message.channel.send(f'Hello! {vannila_players} <--- the players')
    
    if message.content.startswith('$yummy'):
        yummy_players = get_server_info( yummy)
        await message.channel.send(f'Hello! {yummy_players} idk what to say lol')
        

token__cake_will_send = "put token here"
client.run(token__cake_will_send)

