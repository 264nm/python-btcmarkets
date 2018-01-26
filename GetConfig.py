#!/usr/bin/env python3

import requests
import time
import json
import yaml
import os

class OpenConfig(object):
    def __init__(self, config_file="config.yml", site="btc_markets"):
        self.config_file = config_file
        self.site = site
        self.config_dict = {}

    def getConfigFile(self):
        return self.config_file

    def getSite(self):
        return self.site

    def getConfigValues(self):
        with open (self.config_file) as f:
            self.config_dict = yaml.load(f)
        self.config_dict = self.config_dict[self.site]
        return self.config_dict

class GetConfig(OpenConfig):
    def __init__(self):
         super().__init__()
         super().getConfigValues()
         self._api_host = None
         self._api_username = None
         self._api_key_public = None
         self._api_key_secret = None

    @property
    def api_host(self):
        self._api_host = self.config_dict['api_host']
        return self._api_host

    @api_host.setter
    def api_host(self, api_host):
        self._api_host = api_host

    @property
    def api_username(self):
        self._api_username = self.config_dict['api_username']
        return self._api_username

    @api_username.setter
    def api_username(self, api_username):
        self._api_username = api_username

    @property
    def api_key_public(self):
        self._api_key_public = self.config_dict['api_key_public']
        return self._api_key_public

    @api_key_public.setter
    def api_key_public(self, api_key_public):
        self._api_key_public = api_key_public

    @property
    def api_key_secret(self):
        self._api_key_secret = self.config_dict['api_key_secret']
        return self._api_key_secret

    @api_key_secret.setter
    def api_key_secret(self, api_key_secret):
        self._api_key_secret = api_key_secret


def main():

    config = GetConfig()
    print (config.api_host, config.api_username, config.api_key_public, config.api_key_secret)
    return config

if __name__ == '__main__':
    main()
