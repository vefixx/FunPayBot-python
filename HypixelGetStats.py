import requests
import json
import time

while True:    
    r = requests.get('https://api.hypixel.net/skyblock/profile?key=(TOKEN)').json()
    coin_purse = round(r['profile']['members']['f14ac11e474d4bc3bcc8a10dd4a5e2a0']['coin_purse'], 0)
    rounded_number = int(coin_purse)
    first_two_digits = int(str(coin_purse)[:2])
    with open('data.txt', 'w') as f:
        f.write(str(first_two_digits-4))

    print(rounded_number)
    print(first_two_digits-4)
    time.sleep(90)
