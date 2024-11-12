from discord import Message
from client import client, CakeHelper

@client.event
async def on_ready(self: CakeHelper):
    print(f"Ready on client {self.user}")

@client.event
async def on_message(self: CakeHelper, message: Message):
    return