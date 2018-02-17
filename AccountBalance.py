#!/usr/bin/env python3

from APIClient import QueryAPI

def main():
    """ Build the request headers and pass to APIClient with below endpoint
    TODO: Add in functionality to pass options for the CLI.
    """
    endpoint = "account/balance"

    r = (QueryAPI(endpoint, "get"))
    print (r)

if __name__ == "__main__":
    main()
