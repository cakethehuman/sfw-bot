from typing import Dict, TypedDict

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
server_names = {
    72115: "Vanilla Dreams", 
    72116: "Yummy Dreams", 
    72117: "Eggzellent Dreams"
}

def get_server_name(id: int):
    return server_names.get(id, "Unknown")

# Types
class ServerInfo(TypedDict):
    accountId: int
    serverId: int
    ip: str
    port: int
    online: bool
    version: str
    friendlyFire: bool
    modded: bool
    whitelist: bool
    isoCode: str
    players: str
    info: str
    techList: list
    pastebin: str
    official: int
    distance: int

class ResponseAPIServers(TypedDict):
    onlineUserCount: int
    onlineServerCount: int
    displayUserCount: int
    displayServerCount: int
    offlineServerCount: int
    servers: list[ServerInfo]

cache: Dict[int, ServerInfo] = {}

developers = [
    "586050818369781771", # notcake
    "502968724207304714" # relevantzone
]