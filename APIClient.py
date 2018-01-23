#!/usr/bin/env python3
import re
import json
import requests
from requests.exceptions import ConnectionError


class BuildRequest:
    def __init__(self, host, api_endpoint, request_type, request_headers=None, request_body=None):
        self.host = host
        self.api_endpoint = api_endpoint
        self.request_type = request_type
        self.request_body = request_body
        self.request_headers = request_headers
        self.url = self.host + "/" + self.api_endpoint

    def getHost(self):
        return self.host

    def getAPIEndpoint(self):
        return self.api_endpoint

    def getRequestURL(self, host, api_endpoint):
        return self.url

    def getRequestType(self):
        return self.request_type

    def getRequestBody(self):
        return self.request_body

    def getRequestHeaders(self):
        return self.request_headers

    def results(self):
        if self.request_type == "get":
            return requests.get(self.url, headers=self.request_headers)
        elif self.request_type == "put":
            return requests.put(self.url, data=self.request_body)
        elif self.request_type == "post":
            return requests.post(self.url, data=self.request_body)

    def get_results(self):
        try:
            request = self.results()
        except (ConnectionError) as err:
            print(err)
            request = "No response"
        return json.loads(request.text)


def QueryAPI(host, endpoint, req_type, request_headers=None, request_body=None):
    query_api = BuildRequest(host, endpoint, req_type, request_headers=None,
            request_body=None)
    return query_api.get_results()
