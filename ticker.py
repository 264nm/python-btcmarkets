#!/usr/bin/env python3

import time
import os
from APIClient import QueryAPI
from GetConfig import GetConfig

# GENERIC TICKER. PASS IN CURRENCY1 / CURRENCY2
# IN ORDER TO COMPARE

config = GetConfig()

def ticker(curr1,curr2):
    endpoint = "market/" + curr1 + "/" + curr2 + "/tick"
    r = (QueryAPI(config.api_host, endpoint, "get"))

    ask = r["bestAsk"]
    bid = r["bestBid"]
    last = r["lastPrice"]
    tstamp = r["timestamp"]
    ltime = time.ctime(tstamp)
    utime = time.asctime(time.gmtime(tstamp))


    p = """
        BTC Markets most recent BTC trade data:

        Best ask price (buy at):   {0} {6}
        Best bid price (sell at):  {1} {6}

        Last trade price:  {2} {6}

        Accurate at:

        {3} (local time)
        {4} UTC

        Source:  {5}
        ------------------------------------------------------------

        """.format(ask, bid, last, ltime, utime, config.api_host + '/' + endpoint, curr2)

    return p


def main():
    print (ticker("XRP", "AUD"))
    print (ticker("XRP", "BTC"))
    print (ticker("BTC", "AUD"))
if __name__== "__main__":
    main()
