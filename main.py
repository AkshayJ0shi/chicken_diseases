from src.chicken_disease.logging import logger
from src.chicken_disease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = DataIngestionTrainingPipeline()

        obj.main()
        logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
