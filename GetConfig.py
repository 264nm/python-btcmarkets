#!/usr/bin/env python3
import yaml
from typing import Dict
# GetConfig.py

# Class to load in necessary configuration params. Structured in a way
# that could be used to store config for multiple sites but defaulted
# to btc_markets key for this repo in case we wanted to interact with
# other APIs.

# TODO: Create retreival of config vars by other mechanisms such as
#       environment vars and create an order of precidence.

class OpenConfig(object):
    """
    Open configuration file from yaml structure and return as a dictionary.
    The path configured as the default is config.yml in the working directory.

    As mentioned earlier, multiple configuration sets can be stored in here
    seperated by a descriptor key which in this case is defaulted as
    "btc_markets".

    To over-ride these defaults we would obviously instantiate the object like
    x = OpenConfig("different-config.yml", "binance")

    """
    def __init__(self, config_file: str ="config.yml", site: str="btc_markets") -> None:
        self.config_file = config_file
        self.site = site
        self.config_dict: Dict[str, str]

    def get_config_file(self) -> str:
        return self.config_file

    def get_site(self) -> str:
        return self.site

    def get_config_values(self) -> Dict[str, str]:
        with open (self.config_file) as f:
            config_dict = yaml.load(f)
            self.config_dict = config_dict[self.site]
        return self.config_dict

class GetConfig(OpenConfig):
    """
    Using a property and setter approach, this class inherits OpenConfig and
    calls get_config_values method via super() in order to access the
    configuration values as a dictionary and declare them individually.
    Config vars can be used by classes inheriting i.e. NewClass(GetConfig):
        ...and access them via self. i.e. self.api_username
    To interact with the object directly, the standard pattern is
        config = GetConfig()
        print (config.api_username)
    """
    def __init__(self, config_file: str="config.yml", site: str="btc_markets") -> None:
         super().__init__(config_file="config.yml", site="btc_markets")
         super().get_config_values()
         self._api_host: str
         self._api_username: str
         self._api_key_public: str
         self._api_key_secret: str

    @property
    def api_host(self) -> str:
        self._api_host = self.config_dict['api_host']
        return self._api_host

    @api_host.setter
    def api_host(self, api_host):
        self._api_host = api_host

    @property
    def api_username(self) -> str:
        self._api_username = self.config_dict['api_username']
        return self._api_username

    @api_username.setter
    def api_username(self, api_username):
        self._api_username = api_username

    @property
    def api_key_public(self) -> str:
        self._api_key_public = self.config_dict['api_key_public']
        return self._api_key_public

    @api_key_public.setter
    def api_key_public(self, api_key_public):
        self._api_key_public = api_key_public

    @property
    def api_key_secret(self) -> str:
        self._api_key_secret = self.config_dict['api_key_secret']
        return self._api_key_secret

    @api_key_secret.setter
    def api_key_secret(self, api_key_secret):
        self._api_key_secret = api_key_secret


def main():
    """
    Example of how to use the GetConfig class.

    Remember we have the potential to store multiple configuration sets.
    If we had another credential set for "binance" we could do something like
    this:

        btc_markets = GetConfig("other-config.yml", "btc_markets")
        binance = GetConfig("other-config.yml", "binance")
        print ("btcmarkets.net username: " + btc_markets.api_username)
        print ("binance.com username: " + binance.api_username)

    """
    config = GetConfig()
    print (config.api_host, config.api_username, config.api_key_public, config.api_key_secret)
    return config


if __name__ == '__main__':
    main()
