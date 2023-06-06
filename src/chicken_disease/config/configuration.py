from src.chicken_disease.constants import *
from src.chicken_disease.utils.common import create_directories, read_yaml
from src.chicken_disease.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        # These point to constants dir
        # where config.yaml and params.yaml are located

        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # artifacts_root come from config/config.yaml which returns "artifacts
        # hence a directory will be created names "artifacts"
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_configuration(self) -> DataIngestionConfig:
        # we are saving config for data ingestion found in config.yaml in "config" variable
        config = self.config.data_ingestion

        # config.root_dir = artifacts/data_ingestion as per config.yaml
        create_directories([config.root_dir])

        # this is creating the config object from
        # DataIngestionConfig class above
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file, 
            unzip_dir = config.unzip_dir 
        )
        return data_ingestion_config