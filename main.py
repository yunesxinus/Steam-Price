import requests
import json
from colorama import Fore, init
init()
# url = requests.get('https://www.cheapshark.com/api/1.0/stores')
# x = url.json()

# for store in x:
#     print(store['storeID'], store['storeName'])

# You can change the storeID, Price, and Sort by name
url = requests.get(
    'https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15')

x = url.json()
for game in x:
    print(Fore.WHITE+'game id: ' + game['gameID'])
    print('Name: '+Fore.GREEN + game['title'])
    print('SalePrice: '+Fore.RED + game['salePrice'])
    print('Normal Price: '+Fore.BLUE + game['normalPrice'])
    print('Steam Rating: '+Fore.YELLOW + str(game['steamRatingPercent']))
    print('Metacritic Score: '+Fore.CYAN + str(game['metacriticScore']))
    print('Steam AppID: '+Fore.MAGENTA + str(game['steamAppID']))
    print('Thumb: '+Fore.WHITE + game['thumb'])
    print('---------------------------------------------------')
