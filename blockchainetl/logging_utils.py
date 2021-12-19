import logging


def logging_basic_config(filename=None):
    format = '%(asctime)s - %(name)s [%(levelname)s] - %(message)s'
    if filename is not None:
        logging.basicConfig(level=logging.INFO, format=format, filename=filename)
    else:
        logging.basicConfig(level=logging.INFO, format=format)

    logging.getLogger('ethereum_dasm.evmdasm').setLevel(logging.ERROR)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARN)
    logging.getLogger('sqlalchemy.pool').setLevel(logging.WARN)
    logging.getLogger('sqlalchemy.dialects').setLevel(logging.WARN)
    logging.getLogger('sqlalchemy.orm').setLevel(logging.WARN)
    logging.getLogger('ProgressLogger').setLevel(logging.WARN)
