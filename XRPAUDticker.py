#!/usr/bin/env python3

import time
from GetConfig import GetConfig
from APIClient import QueryAPI

config = GetConfig()
endpoint = "market/XRP/AUD/tick"

r = (QueryAPI(config.api_host, endpoint, "get"))

ask = r["bestAsk"]
bid = r["bestBid"]
last = r["lastPrice"]
tstamp = r["timestamp"]
ltime = time.ctime(tstamp)
utime = time.asctime(time.gmtime(tstamp))


p = """
    BTC Markets most recent BTC trade data:

    Best ask price (buy at):   {0} AUD
    Best bid price (sell at):  {1} AUD

    Last trade price:  {2} AUD

    Accurate at:

    {3} (local time)
    {4} UTC

    Source:  {5}

    """.format(ask, bid, last, ltime, utime, config.api_host + '/' + endpoint)

print(p)
