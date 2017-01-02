import os
import logging
from mux import MuxStreamHandler, mux_format

logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info("start project magic")
try:
    os.mkdir('./magic')
except OSError as e:
    logger.exception('{path} already exist'.format(
        path=mux_format(os.getcwd(), 'green', 'underline')))
logger.info('start project magic done')