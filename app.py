from src.data_science_project.logger import logging
from src.data_science_project.exception import CustomException
import sys



if __name__=="__main__":
    logging.info("Starting the data science project application.")
    
    try:
        a=1/0
    except Exception as e:
         logging.info("Custom exception occurred.")
         raise CustomException(e, sys)