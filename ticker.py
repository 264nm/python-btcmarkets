#!/usr/bin/env python3
import click
import time
from APIClient import BuildRequest
from GetConfig import GetConfig

config = GetConfig()

class MarketURI(object):
    """
    Basic class to build the API Endpoint for the "market" API. Requires the arguments
    for the currency and the instrument.
    'tail' is also given as an option but is currently defaulted to 'tick'.
    To extend in future, other options are:
        * tick
        * orderbook
        * trades
    To use for the ticker (as originally intended) we simply do this:
        x = MarketURI("ETH", "BTC") will return the value of ETH in BTC
        endpoint = (x.get_endpoint())
        >> market/ETH/BTC/tick
    """
    def __init__(self, instrument="BTC", currency="AUD", tail="tick"):
        self.currency = currency
        self.instrument = instrument
        self.tail = tail
        self.head = "market"

    def get_currency(self):
        return self.currency

    def get_instrument(self):
        return self.instrument

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def get_endpoint(self):
        self.endpoint = self.head + "/" + self.instrument + "/" + self.currency + "/" + self.tail
        return self.endpoint

def ticker_human(r):
    currency = r["currency"]
    instrument = r["instrument"]
    endpoint = MarketURI(instrument, currency).get_endpoint()
    ask = r["bestAsk"]
    bid = r["bestBid"]
    last = r["lastPrice"]
    tstamp = r["timestamp"]
    ltime = time.ctime(tstamp)
    utime = time.asctime(time.gmtime(tstamp))


    p = """
        BTC Markets most recent {7} trade data:

        Best ask price (buy at):   {0} {6}
        Best bid price (sell at):  {1} {6}

        Last trade price:  {2} {6}

        Accurate at:

        {3} (local time)
        {4} UTC

        Source:  {5}
        ------------------------------------------------------------

        """.format(ask, bid, last, ltime, utime, config.api_host + '/' +
                endpoint, currency, instrument)

    return p

def ticker_raw(instrument, currency):
    endpoint = MarketURI(instrument, currency).get_endpoint()
    query_api = BuildRequest(endpoint, "get",
            request_body=None)
    r = query_api.get_results()
    return r

@click.command()
@click.argument(
    'tick', nargs=2, default=[None] * 2, type=(click.Tuple([str, str]))
)

@click.option(
    '--human', '-h', 'formatting', flag_value='human', default=True,
    help="Output the ticker results in a human readable format"
)

@click.option(
    '--raw', '-r', 'formatting', flag_value='raw',
    help="Output the ticker results as raw json response body"
)


def get_tick(tick, formatting):
    """
    This tool prints all the tickers available on BTCMarkets.net
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
        ./ticker.py <instrument> <currency>
    """

    valid_coins=['BTC', 'LTC', 'ETH', 'ETC', 'XRP', 'BCH']
    coin=tick[0]
    coin=([valid_coin for valid_coin in valid_coins if coin == valid_coin])
    if not coin:
        click.echo('Error invalid coin. See --help for correct options')
        exit()
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

    if formatting == 'human':
        res = ticker_raw(instrument=tick[0], currency=tick[1])
        res = ticker_human(res)
    if formatting == 'raw':
        res = ticker_raw(instrument=tick[0], currency=tick[1])

    click.echo(res)

if __name__ == '__main__':
    get_tick()
