import os ## for path
import sys ## for logging and exception

from src.logger import logging
from src.exception import CustomException


import pandas as pd ## for reading data
from sklearn.model_selection import train_test_split

from dataclasses import dataclass



## Initialaization the data ingestion config.

@dataclass ## using data class allows me to directly create class variables below without __init__
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts','train.csv')  ## in artifacts the test data will be stored in the file names train.csv
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

## data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig() ## this is class variable assigned to DataIngestionconfig
        
    def initiate_data_ingestion(self):
        logging.info("The Data Ingestion method Starts")
        
        try:
            df=pd.read_csv(os.path.join('Notebooks/data','gemstone.csv'))
            logging.info("Dataset Read as panda dataframe")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True) ## exist_ok=True means if there already exists a folder so dont create new
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            
            ## upto here we read data and forwaded it into raw data folder using variable ingestion_config
                
            logging.info("Raw data is created")
            
            ## Now train test split
            
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("Ingestion Of Data is completed")
            
            return(  ## returning as from data ingestion we need test data and train data
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path     
                
            )
                
        
        except Exception as e:
            logging.info('Exception Occured At Data Ingestion Step')
            raise CustomException(e,sys)

