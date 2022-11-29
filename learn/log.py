#logging
import logging

#create and configure logger
log_format ="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="lotan.log", level=logging.DEBUG, format=log_format)
logger = logging.getLogger()

#test the logger
logger.info("Our first message")


