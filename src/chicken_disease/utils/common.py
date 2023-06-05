import os
from box.exceptions import BoxValueError
import yaml
from src.chicken_disease import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# ensure_annotation prevents errors in function parameter datatypes
# without ensure_annotations, 2 * "2" = 22,
# with ensure_annotations, this operation will throw an error
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)

            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")

# during training, we will get loss and accuracy metrics
# we will save that usingg this function
@ensure_annotations
def save_json(path : Path, data : dict):
    """saves json file

    Args:
        path (Path): path like input
        data (dict): data to be saved
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    """loads json file

    Args:
        path (Path): path like input

    Returns:
        ConfigBox: ConfigBox type
    """
    with open(path) as f:
        data = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(data)

@ensure_annotations
def save_bin(data : Any, path : Path):
    """saves bin file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)

    logger.info(f"bin file saved at: {path}")

@ensure_annotations
def load_bin(path : Path) -> Any:
    """loads bin file

    Args:
        path (Path): path to binary file

    Returns:
        Any: loaded data
    """
    logger.info(f"bin file loaded from: {path}")
    return joblib.load(path)

@ensure_annotations
def get_size(path : Path) -> str:
    """gets size of file

    Args:
        path (Path): path to file

    Returns:
        str: size of file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"size: {size_in_kb} Kb"

def encode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)

    with open(filename, 'wb') as f:
            f.write(imgdata)
            f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string
