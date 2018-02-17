#!/usr/bin/env python3

from APIClient import BuildRequest

def main():
    """ Build the request headers and pass to APIClient with below endpoint
    TODO: Add in functionality to pass options for the CLI.
    """
    endpoint = "account/balance"

    query_api = BuildRequest(endpoint, "get",
            request_body=None)
    r = query_api.get_results()
    print (r)

if __name__ == "__main__":
    main()
