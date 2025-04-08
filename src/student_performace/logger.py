import os 
import logging
from datetime import datetime

## creating folder and file to save logs 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

## setting the log format 
logging.basicConfig(

    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger("student_performance_logger")
logger.info("Logger has been successfully configured.")