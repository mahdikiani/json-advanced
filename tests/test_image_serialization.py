from PIL import Image

from json_advanced.json_encoder import dumps, loads


def test_image_serialization(image_data):
    json_string = dumps(image_data)
    deserialized = loads(json_string)

    assert isinstance(deserialized["image"], Image.Image)
    # Compare image attributes
    original = image_data["image"]
    decoded = deserialized["image"]
    assert original.size == decoded.size
    assert original.mode == decoded.mode
