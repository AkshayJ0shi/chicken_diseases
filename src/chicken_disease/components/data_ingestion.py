import os
from pathlib import Path
import urllib.request as request
import zipfile
from src.chicken_disease.logging import logger
from src.chicken_disease.utils.common import get_size
from src.chicken_disease.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config : DataIngestionConfig):
        self.config = config

    # we are storing DataIngestionConfig object in "config"
    # we need to download the file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"{self.config.local_data_file} already exists, Size : {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the zip file to the specified folder
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

