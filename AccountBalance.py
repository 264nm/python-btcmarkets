#!/usr/bin/env python3

import time
import hashlib
import hmac
import base64
from APIClient import QueryAPI
from collections import OrderedDict
from GetConfig import GetConfig

class BuildHeaders(GetConfig):
    def __init__(self, endpoint):
        super().__init__()
        self.endpoint = endpoint
        self.url = self.api_host + '/' + endpoint
        self.headers = {}

    def get_endpoint(self):
        return self.endpoint

    def get_url(self):
        return self.url

    def get_headers(self):
        pkey = self.api_key_public.encode("utf-8")
        askey = self.api_key_secret.encode("utf-8")
        skey = base64.standard_b64decode(askey)

        # Build timestamp
        tstamp = time.time()
        ctstamp = int(tstamp * 1000)  # or int(tstamp * 1000) or round(tstamp * 1000)
        sctstamp = str(ctstamp)

        # Build and sign to construct body
        sbody = '/' + endpoint + "\n" + sctstamp + "\n"
        rbody = sbody.encode("utf-8")
        rsig = hmac.new(skey, rbody, hashlib.sha512)
        bsig = base64.standard_b64encode(rsig.digest()).decode("utf-8")

        # Construct header list of key value pairs
        headers_list = OrderedDict([("Accept", "application/json"),
                      ("Accept-Charset", "UTF-8"),
                      ("Content-Type", "application/json"),
                      ("apikey", pkey),
                      ("timestamp", sctstamp),
                      ("signature", bsig)])

        # Load list into dictionary
        self.headers = dict(headers_list)
        return self.headers

def main():
    """ Build the request headers and pass to APIClient with below endpoint
    TODO: Add in functionality to pass options for the CLI.
    """
    # Define Global Vars
    config = GetConfig()
    endpoint = "account/balance"



    x = BuildHeaders(endpoint)
    res = x.get_headers()
    r = (QueryAPI(config.api_host, endpoint, "get", res))
    print (r)

if __name__ == "__main__":
    main()
