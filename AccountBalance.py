#!/usr/bin/env python3

from APIClient import BuildRequest

def AmountToJSON(amount):
    return float(amount / 1e8)

def build_request():
    """ Build the request headers and pass to APIClient with below endpoint
    TODO: Add in functionality to pass options for the CLI.
    """
    endpoint = "account/balance"

    query_api = BuildRequest(endpoint, "get",
            request_body=None)
    r = query_api.get_results()
    return r

def main():
    r = build_request()
    for g in r:
        currency = g["currency"]
        balance = g["balance"]
        balance_human = AmountToJSON(balance)
        pendingFunds = g["pendingFunds"]
        pendingFunds_human = AmountToJSON(pendingFunds)
        print (str(currency) + " : " + str(balance_human) + " (" +
                str(pendingFunds_human) + ")")

if __name__ == "__main__":
    main()
