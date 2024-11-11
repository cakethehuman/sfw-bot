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
            print("no")


eggz = 72117

vannila = 72116

yummy = 72115



server_pick_eggz = get_server_info(eggz)
server_pick_vannila = get_server_info(vannila)
server_pick_yummy = get_server_info(yummy)

if server_pick_eggz:
    eggz_players = f"eggz have {server_pick_eggz['players']} players"
    print(eggz_players)

if server_pick_vannila:
    vannila_players = f"vannila  have {server_pick_vannila['players']} players"
    print(vannila_players)

if server_pick_yummy:
    yummy_players = f"yummy have {server_pick_yummy['players']} players"
    print(yummy_players)
