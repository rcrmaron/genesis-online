class UnexpectedParameterWarning(UserWarning):
    pass


class GenesisOnlineError(Exception):
    """Base exception for GenesisOnline"""

    pass


class HTTPError(GenesisOnlineError):
    """Exception for HTTP errors"""

    pass


class ConnectionError(GenesisOnlineError):
    """Exception for connection errors"""

    pass


class TimeoutError(GenesisOnlineError):
    """Exception for timeout errors"""

    pass


class RequestError(GenesisOnlineError):
    """Exception for request errors"""

    pass


class UnexpectedContentError(GenesisOnlineError):
    """Exception for unexpected content type"""

    pass


class StandardizationError(GenesisOnlineError):
    """Exception for"""

    pass


class ValueError(GenesisOnlineError):
    """Exception for invalid/unexpected value"""

    pass
