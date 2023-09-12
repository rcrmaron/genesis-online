"""Genesis Online API Wrapper.

The genesisonline python package allows for simple access to the database of the
Federal Statistical Office of Germany by wrapping its official RESTful/JSON API. 
"""

from .client import GenesisOnline
from .utils import configure_logger
import logging

__version__ = "0.1.0"

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
