import requests
import json

HEADERS = {"X-API-Key":'53310a548d4e4e8794493c30ed8a321c'}

# xur_url = "https://www.bungie.net/Platform/Destiny2/Advisors/Xur/"
# print("\n\n\nConnecting to Bungie: " + xur_url + "\n")
# print("Fetching data for: Xur's Inventory!")
# res = requests.get(xur_url, headers=HEADERS)
# print(res.json())

player_url = "https://www.bungie.net/Platform/Destiny2/SearchDestinyPlayer/3/comet/"
print("\n\n\nConnecting to Bungie: " + player_url + "\n")
# print("Fetching data for: Xur's Inventory!")
res = requests.get(player_url, headers=HEADERS)
print(res.json())