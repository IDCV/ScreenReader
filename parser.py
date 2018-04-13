import pyocr
from PIL import Image

import config
from datastructs import ImageData, ParsedString


def get_image(file_name: str) -> ImageData:
    return ImageData(file_name.split('/')[1], Image.open(file_name))


def preprocess(img_data: ImageData, save_option: bool=False) -> ImageData:
    img_converted = img_data.image.convert('L')
    if save_option:
        img_converted.save(config.PATH_TO_CONVERTED.format(img_data.file_name))
    return ImageData(img_data.file_name, img_converted)


def pars(img_data: ImageData, lang='eng') -> ParsedString:
    tool = pyocr.get_available_tools()[0]
    text = tool.image_to_string(img_data.image, lang)
    return ParsedString(text)