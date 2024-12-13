import os
import logging

def create_logger(app):
    logger = logging.getLogger('portfolio')
    logger.setLevel(app.config['LOG_LEVEL'])
    formatter = logging.Formatter('{"time": "%(asctime)s", "name": "%(name)s", "level": "%(levelname)s", "lineno": "%(lineno)d", "message": "%(message)s"}')

    log_dir = os.path.join(os.path.dirname(__file__),'..','..','..','logs')
    log_file = os.path.join(log_dir,'portfolio.log')

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger
