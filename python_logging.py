import logging

logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w', format="%(asctime)s - %(levelname)s - %("
                                                                                 "message)s")

name = 'Tosin'
logging.info(f'my name is {name}')
logging.info('info')
logging.warning('warnings')
logging.error('error')
logging.critical('critical')

try:
    1/0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError", exc_info=True)
    logging.exception('Test')

# Customer logger
logger = logging.getLogger(__name__)
handler = logging.FileHandler('test.log')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
logger.info("test the custom logger")