import os
import sys
#from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        
        df = pd.read_csv('notebook/data/stud.csv')
        logging.info('Read the dataset as dataframe')

        # Creating directories for the artifacts
        os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

        # Saving the raw data
        df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

        # Splitting the data into train and test sets
        logging.info("Train test split initiated")
        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

        # Saving train and test sets
        train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
        test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

        logging.info("Ingestion of the data is completed")

        return (
            self.ingestion_config.train_data_path,
            self.ingestion_config.test_data_path
        )
        

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
