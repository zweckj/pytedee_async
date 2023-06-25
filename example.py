'''
Created on 01.11.2020

@author: joerg
'''
import time
from pytedee_async.TedeeClient import TedeeClient
from pytedee_async.Lock import Lock
from pytedee_async.TedeeClientException import TedeeClientException
import asyncio
import json

async def main():
    with open("config.json") as f:
        data = json.load(f)
    '''Tedee Credentials'''
    personalToken = data["personalToken"]

    client = await TedeeClient.create(personalToken)
    print ("Token: " + str(client._personalToken))
    locks = client.get_locks()
    for lock in locks:
        print("----------------------------------------------")
        print("Lock name: " + lock.name)
        print("Lock id: " + str(lock.id))
        print("Lock Battery: " + str(lock.battery_level))
        await client.get_state()
        print("Is Locked: " + str(client.is_locked(lock.id)))
        print("Is Unlocked: " + str(client.is_unlocked(lock.id)))
        await client.lock(lock.id)
        await asyncio.sleep(7)
        await client.unlock(lock.id)
        # await asyncio.sleep(10)
        # await client.open(lock.id)

asyncio.run(main())