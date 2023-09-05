import pytest
import os
from pathlib import Path
from genesisonline.filemanager import FileManager
from genesisonline.constants import PACKAGE_NAME

TEST_DIRECTORY = Path("temp")


def cleanup(directory: Path) -> None:
    """Utility function for deleting files and directories"""
    for file in directory.iterdir():
        file.unlink()
    directory.rmdir()


@pytest.fixture
def file_manager():
    yield FileManager(directory=TEST_DIRECTORY)
    cleanup(TEST_DIRECTORY)


def test_default_directory_created():
    default_dir = Path(os.path.expanduser("~")) / PACKAGE_NAME
    _ = FileManager()

    assert os.path.exists(default_dir)

    cleanup(default_dir)


def test_change_directory(file_manager):
    old_dir = file_manager.directory
    new_dir = Path(os.path.expanduser("~")) / PACKAGE_NAME
    file_manager.directory = new_dir

    assert os.path.exists(old_dir)
    assert os.path.exists(new_dir)

    cleanup(new_dir)


@pytest.mark.parametrize(
    "file_name, content",
    [
        ("file.json", {"name": "Alice", "age": 30}),
        ("file.pkl", {"name": "Bob", "age": 25}),
    ],
)
def test_save_and_load(file_manager, file_name, content):
    file_manager.save(content, file_name)
    loaded_data = file_manager.load(file_name)

    assert loaded_data == content
