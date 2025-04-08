from src.student_performace.logger import logging
from src.student_performace.exception import CustomeException
import sys 

if __name__=="__main__":
    logging.info("The execution is started")
    try:
        a=1/0
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomeException(e,sys)
    