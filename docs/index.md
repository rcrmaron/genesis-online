# Welcome to genesisonline
*a python wrapper for interacting with the public GENESIS-Online API*

![tests workflow](https://github.com/rcrmaron/genesis-online/actions/workflows/testing.yaml/badge.svg)
![docs workflow](https://github.com/rcrmaron/genesis-online/actions/workflows/docs.yaml/badge.svg)
![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)
![Windows](https://img.shields.io/badge/OS-Windows-blue.svg)
![Linux](https://img.shields.io/badge/OS-Linux-blue.svg)



## About genesisonline

The **genesisonline** package is a lightweight python wrapper around the [GENESIS-Online API](https://www-genesis.destatis.de/genesis/online?operation=sprachwechsel&language=en) which provides access to the database of the German Federal Statistical Office. Its primary function is to:

- provide a one-to-one mapping of the RESTful/JSON web services specified in the
[official user documentation](https://www-genesis.destatis.de/genesis/misc/GENESIS-Webservices_Introduction.pdf). 

- always return a standardized JSON response, regardless of the underlying API's response structure.


## Prerequisites

In order to use this wrapper, one has to be a registered user of the [GENESIS-Online API](https://www-genesis.destatis.de/genesis/online?operation=sprachwechsel&language=en). New users can sign up for an account [here](https://www-genesis.destatis.de/genesis/online?Menu=Anmeldung#abreadcrumb).


## Installing

To install with pip, use: 
```bash
pip install genesisonline
```

For a developer install, first clone the repository and then carry out an editable install:
```bash
git clone https://github.com/rcrmaron/genesis-online.git
cd genesis-online
pip install -e .[dev]
```

## Example usage

Set up wrapper and verify it is working correctly:

```python
from genesisonline import GenesisOnline

# initialize the API wrapper object
go = GenesisOnline(username="your_username", password="your_password")

# check if the API is online
go.check_api()
>>> {'User-Agent': 'python-requests/2.31.0'}

# check if the API login was successfull
go.check_login()
>>> {'Status': 'You have been logged in and out successfully!', 'Username': 'your_username'}
```

Fetch data from various services and endpoints:

```python
# data/table/ endpoint
response = go.data.table(name="51000-0012")

# find/find endpoint
response = go.find.find(term="waste", category="cubes", pagelength="1")

# metadata/cube endpoint
response = go.metadata.cube(name="12411BJ001", area="all")
```

