"""Constants for the Genesis Online API."""
from .endpoints import Endpoints
from enum import IntEnum

BASE_URL = "https://www-genesis.destatis.de/genesisWS/rest/2020/"
API_VERSION = "4.3"


class JsonKeys:
    """Contains the most commonly encountered JSON keys"""

    # for identification of the service
    IDENT = "Ident"
    SERVICE = "Service"
    METHOD = "Method"

    # information on the processing of the request
    STATUS = "Status"
    CODE = "Code"
    CONTENT = "Content"
    TYPE = "Type"

    # parameters from the request used for processing
    PARAMETER = "Parameter"

    # actual object(s) which were requested, found and returned
    CONTENT = "Content"  # custom
    LIST = "List"  # catalogoue services
    OBJECT = "Object"  # data and metadata services
    STATISTICS = "Statistics"  # find service (optional)
    TABLES = "Tables"  # find service (optional)
    TIMESERIES = "Timeseries"  # find service (optional)
    VARIABLES = "Variables"  # find service (optional)
    CUBES = "Cubes"  # find service (optional)

    # copyright information of the publisher
    COPYRIGHT = "Copyright"

    # custom
    MESSAGE = "Message"
    RESULTID = "ID"


class JsonStrings:
    """Contains the most commonly encountered JSON strings"""

    NA = "NA"


class ResponseStatus(IntEnum):
    MATCH = 0
    PARTLY_MATCH = 22  # i.e. at least one parameter contains invalid values. It was changed to perform the service
    BACKGROUND_REQ = 89  # i.e. background-processing required due to size
    BACKGROUND_RUN = 99  # i.e. background-processing running
    NO_MATCH = 104  # i.e. there are no objects matching your selection
