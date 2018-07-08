#!/usr/bin/env python3

# Module-ish import for doing the actual API calls.
# Doesn't do anything fancy and interact via requests library

import json
import requests
import time
import hashlib
import hmac
import base64
from requests.exceptions import ConnectionError
from collections import OrderedDict
from GetConfig import GetConfig
from typing import Dict, List, Any, Union, Optional

class BuildHeaders(GetConfig):
    """
    Argument: endpoint
        i.e BuildHeaders("market/balance")

    Builds the headers for authentication with the btcmarkets.net API. Uses our
    GetConfig class to grab user variables from YAML (or however expressed in
    order of precedence once extended to use ENV vars etc)

    This object has been modified to be inherited into the BuildRequest class
    via super().get_headers() but can obviously be imported for direct use i.e.

        In [1]: from APIClient import BuildHeaders
        In [2]: x = BuildHeaders("example/endpoint")
        In [3]: x.get_headers()
        Out[3]:
        {'Accept': 'application/json',
         'Accept-Charset': 'UTF-8',
         'Content-Type': 'application/json',
         'apikey': b'9dda5ac5-e303-4e75-bc13-94115f489d23',
         'signature': 'dsjklsdkflkslklsdfkklnlsdfnklsdklfklksdf',
         'timestamp': '1518830733142'}
    """

    def __init__(self, endpoint) -> None:
        super().__init__()
        self.endpoint: str = endpoint
        self.url: str = self.api_host + '/' + endpoint
        self.headers: Dict[str, str] = {}

    def get_endpoint(self) -> str:
        return self.endpoint

    def get_url(self) -> str:
        return self.url

    def get_headers(self) -> Dict[str, str]:
        headers_list: OrderedDict[str, Any]

        pkey = self.api_key_public.encode("utf-8")
        askey = self.api_key_secret.encode("utf-8")
        skey = base64.standard_b64decode(askey)

        # Build timestamp
        tstamp = time.time()
        # or int(tstamp * 1000) or round(tstamp * 1000)
        ctstamp = int(tstamp * 1000)
        sctstamp = str(ctstamp)

        # Build and sign to construct body
        sbody = '/' + self.endpoint + "\n" + sctstamp + "\n"
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


class BuildRequest(BuildHeaders, GetConfig):
    """
    Performs HTTP request via requests module.
    Access the headers from BuildHeaders via inheritence using Super().
    Takes the following args:
        api_endpoint
        request_type i.e. get, put, post
    If using put/post you must also pass a request_body
    """

    def __init__(self, api_endpoint: str, request_type: str, request_body: Dict[str, str]=None) -> None:
        super().__init__(api_endpoint)
        super().get_headers()
        self.api_endpoint = api_endpoint
        self.request_type = request_type
        self.request_body = request_body
        self.url: str = self.api_host + "/" + api_endpoint

    def get_api_endpoint(self) -> str:
        return self.api_endpoint

    def get_request_type(self) -> str:
        return self.request_type

    def get_request_body(self) -> Optional[Dict[str, str]]:
        return self.request_body

    def results(self) -> Any:
        if self.request_type == "get":
            return requests.get(self.url, headers=self.headers)
        elif self.request_type == "put":
            return requests.put(self.url, headers=self.headers,
                                data=self.request_body)
        elif self.request_type == "post":
            return requests.post(self.url, headers=self.headers,
                                 data=self.request_body)

    def get_results(self) -> Any:
        try:
            request = self.results()
        except (ConnectionError) as err:
            print(err)
            request = "No response"
        return json.loads(request.text)
