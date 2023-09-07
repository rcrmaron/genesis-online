import pytest
import os
from pathlib import Path
from .conftest import TEST_DIR, delete_dir
from genesisonline.filemanager import FileManager
from genesisonline import exceptions


@pytest.fixture
def file_manager():
    return FileManager()


def test_default_directory_created():
    default_dir = TEST_DIR
    _ = FileManager()

    assert os.path.exists(default_dir)


def test_change_directory(file_manager):
    old_dir = TEST_DIR
    new_dir = TEST_DIR / "subdir"
    file_manager.directory = new_dir

    assert os.path.exists(old_dir)
    assert os.path.exists(new_dir)

    delete_dir(new_dir)


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


def test_save_value_error(file_manager):
    with pytest.raises(exceptions.ValueError):
        file_manager.save({"test": "test"}, "file.invalid")


def test_load_value_error(file_manager):
    with pytest.raises(exceptions.ValueError):
        file_manager.load({"test": "test"}, "file.invalid")


@pytest.fixture(scope="session", autouse=True)
def cleanup_after_tests():
    yield
    delete_dir(TEST_DIR)
