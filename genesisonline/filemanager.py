import os
from pathlib import Path
from typing import Union, Any
import pickle
import logging
import json
from genesisonline.constants import PACKAGE_NAME
from genesisonline.exceptions import ValueError

logger = logging.getLogger(__name__)


class FileManager:
    """
    A utility class for managing file operations in a specified directory.

    This class provides methods for handling file operations, such as saving
    and retrieving files in a designated directory.

    Attributes
    ----------
    directory : pathlib.Path
        The path to the directory where files will be stored.
    supported_file_types : list
        Contains names of currently supported file types.
    """

    def __init__(self, directory: Union[Path, str] = None):
        """Initialize a FileManager instance.

        Parameters:
        -----------
        directory : pathlib.Path
            The path to the directory where files will be stored.
            If not provided, a default directory called 'genesisonline' is
            created in the user's home directory.
        """
        self.directory = directory
        self.supported_file_types = ["pkl", "json"]

    @property
    def directory(self) -> Path:
        return self._directory

    @directory.setter
    def directory(self, new_directory: Union[Path, str] = None):
        if new_directory:
            self._directory = Path(new_directory)
        else:
            self._directory = Path(os.path.expanduser("~")) / PACKAGE_NAME

        self._directory.mkdir(parents=True, exist_ok=True)
        logger.info(f"Initialized directory '{self._directory}'")

    def save(self, content: Any, file_name: str) -> None:
        """Save `content` to a file called `file_name`.

        The file type depends on the provided suffix in `file_name`.

        Parameters
        ----------
        content : Any
            The content to be saved to the file.
        file_name : str
            The name of the file the content is saved to.
        """
        destination = self.directory / file_name
        file_type = destination.suffix
        logger.info(f"Saving file '{destination}'")

        if file_type == ".pkl":
            self._save_pickle(content, destination)
        elif file_type == ".json":
            self._save_json(content, destination)
        else:
            raise ValueError(
                f"Unsupported file type '{file_type}'. Currently support: {self.supported_file_types}"
            )

    def load(self, file_name: str) -> Any:
        """Load content from `file_name`.

        Parameters
        ----------
        file_name : str
            The name of the file the content is retrieved from.
        """
        destination = self.directory / file_name
        file_type = destination.suffix
        logger.info(f"Loading file '{destination}'")

        if file_type == ".pkl":
            return self._load_pickle(destination)
        elif file_type == ".json":
            return self._load_json(destination)
        else:
            raise ValueError(
                f"Unsupported file type '{file_type}'. Currently support {self.supported_file_types}"
            )

    def _save_json(self, content, destination) -> None:
        with open(destination, "w") as f:
            json.dump(content, f)

    def _load_json(self, destination) -> Any:
        with open(destination, "r") as f:
            return json.load(f)

    def _save_pickle(self, content, destination) -> None:
        with open(destination, "wb") as f:
            pickle.dump(content, f)

    def _load_pickle(self, destination) -> Any:
        with open(destination, "rb") as f:
            return pickle.load(f)
