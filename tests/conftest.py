from datetime import date, datetime
from io import BytesIO
from pathlib import Path
from uuid import uuid4

import pytest
from PIL import Image


@pytest.fixture
def sample_data():
    return {
        "str": "string",
        "int": 1,
        "float": 1.0,
        "bool": True,
        "none": None,
    }


@pytest.fixture
def binary_data():
    return {
        "binary": bytes([1, 2, 3]),
        "bytesio": BytesIO(b"test data"),
    }


@pytest.fixture
def image_data():
    return {
        "image": Image.new("RGB", (100, 100), color="red"),
    }


@pytest.fixture
def datetime_data():
    return {
        "datetime": datetime.now(),
        "date": date.today(),
        "time": datetime.now().time(),
    }


@pytest.fixture
def uuid_data():
    return {
        "uuid": uuid4(),
    }


@pytest.fixture
def path_data():
    return {
        "path": Path("/tmp/test"),
    }
