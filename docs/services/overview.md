# Overview
***
The **genesisonline** package is designed to offer a one-to-one mapping of the GENESIS-Online web services.
Each service in the GENESIS-Online API is encapsulated as a distinct class, with its respective endpoints 
represented as class methods. Users can seamlessly access and interact with these services and their
associated methods through the central `GenesisOnline` object.

## Services
***
- [`TestService`](test.md): maps methods from the *HelloWorld* service  for a first test of the API.
- [`FindService`](test.md): maps methods from the *Find* service to find information.
- [`CatalogueService`](test.md): maps methods from the *Catalogue* service to list objects.
- [`DataService`](data.md): maps methods from the *Data* service to download data.
- [`MetadataService`](test.md): maps methods from the *Metadata* service to download metadata.

## Accessing endpoints through [`GenesisOnline`](../client.md)
***
The `GenesisOnline` object serves as the primary interface to interact with the GENESIS-Online web services.
Each service is exposed as an attribute of this object, allowing users to directly access and utilize
the methods associated with each service.


```python
from genesisonline import GenesisOnline

# initialize the GenesisOnline object
go = GenesisOnline(username="your_username", password="your_password")

# accessing the HelloWorld service and its endpoints 
response = go.test.whoami()

# accessing the Find service and its endpoints
response = go.find.find()

# accessing the Catalogue service and its endpoints
response = go.catalogue.cubes()

# accessing the Data service and its endpoints
response = go.data.chart2results()

# accessing the Metadata service and its endpoints
response = go.metadata.cube()
```