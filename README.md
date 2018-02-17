Python-BTCMarkets
=================

Python toolkit/scripts for accessing the btcmarkets.net RESTful API.

Configuration
--------------

$ cp config.yml.tmpl config.yml

Then modify config.yml to contain the necessary fields i.e.

```
btc_markets:
  api_username: "example@gmail.com"
  api_key_public: "+WfRNrcOw3BxqueMtSDSGuodnzBFCPBM"
  api_key_secret: "+GdkWW7kPzIV2C6A0fTkoi/A42qXx2pBFUWmH7ZEMQ8EVfkLiJ97pNl0Oz0O36KZ"
  api_host: "https://api.btcmarkets.net"
```

Obviously use your own public and private keys obtained from your account page

Ticker
-------

Usage:

```
./ticker.py <currency> <instrument> <--human|raw> (human default)
```

Account Balance
---------------

Usage:

```
./AccountBalance.py
```

TODO: Create proper Click interface and human readable formatting

Licensing
---------

This code is freely available under the terms of the GNU General Public License version 3, or any later version.

If you wish to use my code in a library or other application and the GPL is unsuitable for that purpose, I will consider multi-licensing it under the LGPL or one of the BSD variants (a modified 3-clause is the most likely).  Some other licenses may be considered, please contact me directly to discuss those terms.


Requirements
------------

This code is written for Python 3.2 and above, but developed with Python 3.6.

Pipenv: A Pipfile has been created for easy development http://pipenv.readthedocs.io/en/latest/install

To install dependencies simply enter the working directory and run:

```
pipenv install
```

If you have no desire to check out Pipenv I have generated a requirements.txt file you can use to install the packages via standard `pip install -r requirements.txt`

P.S the command to export requirements from Pipfile.lock is:

```pipenv lock --requirements > requirements.txt```


Project Status
--------------

This is a fork of https://github.com/adversary-org/python-btcmarkets. Originally I had contributed a PR upstream but recently I have been refactoring with a desire to learn how to create reusable code and it has diverged considerably enough to warrant my own fork. Thanks go out to the original project particularly for the pretty human readable ticker formatting which I have retained during the rework.

