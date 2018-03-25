#!/usr/bin/env python3

from APIClient import BuildRequest
import click



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

def balance_human_read(res):
    balance_human_list = []
    for g in res:
        currency = g["currency"]
        balance = g["balance"]
        balance_human = AmountToJSON(balance)
        pendingFunds = g["pendingFunds"]
        pendingFunds_human = AmountToJSON(pendingFunds)
        acc_bal_hum = (str(currency) + " : " + str(balance_human) + " (Pending: " +
            str(pendingFunds_human) + ")")
        balance_human_list.append(acc_bal_hum)
    return balance_human_list

@click.command()

@click.option(
    '--human', '-h', 'formatting', flag_value='human', default=True,
    help="Output account balances in a human readable format"
)

@click.option(
    '--raw', '-r', 'formatting', flag_value='raw',
    help="Output the account balances as raw json response body"
)

def get_account_balance(formatting):
    r = build_request()
    if formatting == 'human':
        balances = balance_human_read(r)
        output = "\n".join(balance for balance in balances)
    if formatting == 'raw':
        output = r

    click.echo(output)

if __name__ == "__main__":
    get_account_balance()
