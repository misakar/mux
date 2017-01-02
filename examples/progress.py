import os
import time
import logging
from mux import MuxStreamHandler, mux_progressbar, mux_format

logger = logging.getLogger(__name__)
handler = MuxStreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

@mux_progressbar
def init():
    time.sleep(4)

if __name__ == '__main__':
    logger.info('start task')
    init()
    logger.info('task done')