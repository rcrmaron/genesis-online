# Welcome to genesisonline
*genesisonline provides an interface to seamlessly interact with the public GENESIS-Online API.*
***

## Installing
***
TODO

## About genesisonline
***
The **genesisonline** package is designed to be a lightweight python wrapper around the GENESIS-Online API
that offers a one-to-one mapping of the RESTful/JSON web services specified in the
[official user documentation](https://www-genesis.destatis.de/genesis/misc/GENESIS-Webservices_Introduction.pdf). 


Each service of the GENESIS-Online API is encapsulated as a distinct class, with its respective endpoints
represented as class methods. Users can seamlessly access and interact with these services and their 
associated methods through the central `GenesisOnline` object which returns a standaradized JSON response. 

