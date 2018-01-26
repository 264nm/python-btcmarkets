#!/usr/bin/env python3
import click
import time
import os
from APIClient import QueryAPI
from GetConfig import GetConfig

# GENERIC TICKER. PASS IN CURRENCY1 / CURRENCY2
# IN ORDER TO COMPARE

config = GetConfig()

def ticker(curr1,curr2):
    endpoint = "market" + "/" + curr1 + "/" + curr2 + "/tick"
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

@click.command()
@click.argument(
    'tick', nargs=2, type=(click.Tuple([str, str]))
)

def get_tick_option(tick):
    """
    This tool prints all the tickers available on BTCMarkets.net
    Options Available:

    BTCMarkets.net at this stage only allows trading using AUD and BTC as currency.

    Options Available:

    \b
    AUD:
        * BTC - BitCoin
        * LTC - LiteCoin
        * ETH - Ethereum
        * ETC - Ethereum Classic
        * XRP - Ripple
        * BCH - Bitcoin Cash

    \b
    BTC:
        * LTC - LiteCoin
        * ETH - Ethereum
        * ETC - Ethereum Classic
        * XRP - Ripple
        * BCH - Bitcoin Cash
    \b
    USAGE:
        ./ticker.py <coin> <currency>
    """

    valid_coins=['BTC', 'LTC', 'ETH', 'ETC', 'XRP', 'BCH']
    coin=tick[0]
    coin=([valid_coin for valid_coin in valid_coins if coin == valid_coin])
    if not coin:
        click.echo('Error invalid coin. See --help for correct options')
    else:
        coin = str(coin).strip('[]')

    valid_currencies=['BTC', 'AUD']
    currency=tick[1]
    currency=([valid_currency for valid_currency in valid_currencies if currency == valid_currency])
    if not currency:
         click.echo('Error - invalid currency. See --help for correct options')
         exit()
    else:
         currency = str(currency).strip('[]')

    res = ticker(curr1=tick[0], curr2=tick[1])
    click.echo(res)

if __name__ == '__main__':
    get_tick_option()
