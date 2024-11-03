import logging


# def sample_logger(filename, filemode, level=logging.DEBUG):
#     logging.basicConfig(level=level,
#                         filename=filename,
#                         filemode=filemode,
#                         format="%(asctime)s - %(levelname)s : %(message)s",
#                         datefmt='%m/%d/%Y %I:%M:%S %p')
#     logger = logging.getLogger("custom_logger")
#     return logger


def sample_logger(filename, mode, name, level=logging.DEBUG):
    logger = logging.getLogger(name=name)
    logger.setLevel(level=level)
    formatter = logging.Formatter(datefmt='%m-%d-%Y %I:%M:%S %p',
                                  fmt="%(asctime)s - %(name)s - %(filename)s | %(levelname)s : %(message)s")
    file_handler = logging.FileHandler(filename=filename,
                                       mode=mode)
    file_handler.setFormatter(fmt=formatter)
    logger.addHandler(file_handler)
    return logger


if __name__ == '__main__':
    logger_yosra = sample_logger(filename='../Logs/yosra_logs.log', mode='w')
    # logger.setLevel(logging.DEBUG)
    logger_yosra.debug('This message should go to the log file')
    logger_yosra.info('So should this')
    logger_yosra.warning('And this, too')
    logger_yosra.error('And non-ASCII stuff, too, like Øresund and Malmö')