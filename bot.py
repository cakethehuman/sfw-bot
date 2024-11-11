import discord
import requests
from requests_cache import CachedSession
import requests_cache
from threading import Thread
import time

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

    vanilla = 72116

    yummy = 72115

    if message.author == client.user:
        return

    if message.content.startswith('$eggz'):
        eggz_players = get_server_info(eggz)
        embed = discord.Embed (
            color= discord.Color.blue(),
            description = f'this is your player count cake said: {eggz_players["players"]}',
            title= "total players on eggz"
            )
        embed.set_footer(text = "api might be a little slow sometimes")
        await message.channel.send(embed=embed)
    
    if message.content.startswith('$vanilla'):
        vanilla_players = get_server_info(vanilla)
        embed = discord.Embed (
            color= discord.Color.green(),
            description = f'this is your player count cake said: {vanilla_players["players"]}',
            title= "total players on vanilla"
            )
        embed.set_footer(text = "api might be a little slow sometimes")
        await message.channel.send(embed=embed)
    
    if message.content.startswith('$yummy'):
        yummy_players = get_server_info(yummy)
        embed = discord.Embed (
            color= discord.Color.red(),
            description = f'this is your player count cake said: {yummy_players["players"]}',
            title= "total players on yummy"
            
        )
        embed.set_footer(text = "api might be a little slow sometimes")
        await message.channel.send(embed=embed)

    if message.content.startswith('$cake'):
        embed = discord.Embed (
            color= discord.Color.pink(),
            title= "cake"
            
        )
        embed.set_image(url='https://scp-wiki.wdfiles.com/local--files/scp-871/Cake.jpg')#fix
        await message.channel.send(embed=embed)
        
    if message.content.startswith('$all'):
        eggz_players = get_server_info(eggz)
        vanilla_players = get_server_info(vanilla)
        yummy_players = get_server_info(yummy)

        embed = discord.Embed (
            color= discord.Color.pink(),
            title="all server player list",
            description= (
            f'this is eggz: {eggz_players["players"]} \n'
            f'this is vanilla: {vanilla_players["players"]} \n'
            f'this is yummy: {yummy_players["players"]}')
        )
        embed.set_footer(text = "api might be a little slow sometimes")
        await message.channel.send(embed=embed)
        
token__cake_will_send = ""
client.run(token__cake_will_send)

