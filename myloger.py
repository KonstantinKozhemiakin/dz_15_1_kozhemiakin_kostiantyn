import logging
import sys


# import logging.config


def init_my_loger():
    logger = logging.getLogger('my_loger')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setLevel(logging.INFO)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    filehandlerwarnings = logging.FileHandler('mylogswarnings.log')
    filehandlerwarnings.setLevel(logging.WARNING)
    filehandlerwarnings.setFormatter(formatter)
    logger.addHandler(filehandlerwarnings)

    filehandlererror = logging.FileHandler('mylogserror.log')
    filehandlererror.setLevel(logging.ERROR)
    filehandlererror.setFormatter(formatter)
    logger.addHandler(filehandlererror)
    return logger
# init_my_loger()
# logger.info('dkglwdgk')