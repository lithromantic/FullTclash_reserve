import asyncio

import aiohttp
from aiohttp.client_exceptions import ClientResponseError

from cleaner import ClashCleaner

proxies = "http://127.0.0.1:1111"

url = "https://kaxinzx.cc/api/v1/client/subscribe?token=69fb3bc166b3b8e9c35d3821820107ab"


def main():
    from cleaner import ConfigManager
    co = ConfigManager()
    admin = co.getAdmin()
    print(admin)
    co.add_admin("aa")
    co.save()



if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    main()
