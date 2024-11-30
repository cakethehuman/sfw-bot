from typing import Dict, TypedDict

api_url = 'https://api.scplist.kr/api/servers'
api_request_payload = {
    "search": "SFW",
    "countryFilter": [
        "SG"
    ],
    "hideEmptyServer": False,
    "hideFullServer": False,
    "friendlyFire": "null",
    "whitelist": "null",
    "modded": "null",
    "sort": "DISTANCE_ASC"
}
server_names = {
    72115: "Vanilla Dreams", 
    72116: "Yummy Dreams", 
    72117: "Eggzellent Dreams"
}

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

def get_server_name(id: int):
    return server_names.get(id, "Unknown")

def format_server_info(id: int) -> str:
    server = cache.get(id)
    check_box = "✅"
    emoji = "🦅"

    return (
        f"**{get_server_name(id)}** ({id})\n" +
        f"\tGame Version: **{server.get('version')}** {check_box}\n" +
        f"\tPlayer Counts: **{server.get('players')}** {emoji}"
    )