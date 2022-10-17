from unicodedata import name
import psutil
from pypresence import Presence
import time

client_id = '123456789'  # Fake ID, put your real one here
RPC = Presence(client_id, pipe=0)  # Initialize the client class
RPC.connect()  # Start the handshake loop

# details = 2nd line
# state = 3rd line
# large_image = large img
# small_image = small img
# buttons = buttons


print(RPC.update(state="Lookie Lookie", details="A test of qwertyquerty's Python Discord RPC wrapper, pypresence!",
      large_image="piximg", small_image="piximg", start=2, buttons=[{"label": "My Website", "url": "https://qtqt.cf"}]))  # Set the presence

while True:  # The presence will stay on as long as the program is running
    time.sleep(1)  # Can only update rich presence every 15 seconds
