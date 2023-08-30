import logging
from typing import Union
from pathlib import Path


def get_api_params(func_args: dict, exclude: list = list()) -> dict:
    exclude.extend(["self", "__class__"])
    api_params = func_args.pop("kwargs", dict())
    for k, v in func_args.items():
        if k not in exclude:
            api_params[k] = v
    return api_params


def configure_logger(
    log_level=logging.INFO,
    log_to_console: bool = True,
    log_to_file: Union[Path, str] = None,
) -> None:
    """
    Configures the logger for the 'genesisonline' package.

    Parameters
    ----------
    log_level : int, optional
        The level of the logger. This determines the level of detail of the logs.
        The available levels are: logging.DEBUG, logging.INFO, logging.WARNING,
        logging.ERROR, and logging.CRITICAL. Default is logging.INFO.
    log_to_console : bool, optional
        Whether to log the messages to the console. Default is True.
    log_to_file : Union[Path, str], optional
        The file to log the messages to.
        If not specified, the messages will not be logged to a file.
        Default is None.

    Returns
    -------
    None

    Examples
    --------
    >>> configure_logger(log_level=logging.DEBUG, log_to_console=False, log_to_file='logfile.log')

    This will configure the logger to log messages at DEBUG level and higher, will not log messages to
    the console, and will log messages to a file named 'logfile.log'.
    """
    logger = logging.getLogger()
    logger.setLevel(log_level)
    formatter = logger.handlers[0].formatter

    # remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # log to console
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # log to file
    if log_to_file:
        file_handler = logging.FileHandler(log_to_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
