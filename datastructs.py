from typing import Tuple, NamedTuple
from PIL import Image


class ImageData(NamedTuple):
    file_name: str
    image: Image.Image


class ParsedString(NamedTuple):
    """
    It will be consists of parsed info
    currently it is just text
    """
    text: str
